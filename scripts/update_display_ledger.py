#!/usr/bin/env python3.11
"""Check or refresh display locations without discarding editorial decisions."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json

from validate_editorial_audit import ROOT, current_display_labels


LEDGER = ROOT / "docs" / "display-ledger.json"


def locate(label: str) -> tuple[str, int]:
    needle = rf"\label{{{label}}}"
    roots = (
        ROOT / "chapters",
        ROOT / "appendices",
        ROOT / "tables",
        ROOT / "figures",
    )
    for directory in roots:
        for path in sorted(directory.rglob("*.tex")):
            source = path.read_text(encoding="utf-8", errors="replace")
            if needle in source:
                return (
                    str(path.relative_to(ROOT)),
                    source[: source.index(needle)].count("\n") + 1,
                )
    raise SystemExit(f"could not locate active display label {label}")


def chapter_for(path: str) -> str:
    if "ch02-exdqlm" in path or path.endswith("02-research-a.tex") or "b-exdqlm" in path:
        return "ch02-exdqlm"
    if "ch03-environ" in path or path.endswith("03-research-b.tex") or "c-hydrology" in path:
        return "ch03-environ"
    if "ch04-qdesn" in path or path.endswith("04-research-c.tex") or "d-qdesn" in path:
        return "ch04-qdesn"
    if "ch05-mti" in path or path.endswith("05-research-d.tex") or "e-mti" in path:
        return "ch05-mti"
    return "cross-chapter"


def display_type(label: str) -> str:
    return "figure" if ":fig:" in label else "table"


def new_record(label: str, source: str, line: int) -> dict[str, object]:
    placement = "technical appendix" if source.startswith("appendices/") else "reading chapter"
    return {
        "id": label,
        "chapter": chapter_for(source),
        "type": display_type(label),
        "source_file": source,
        "baseline_line": line,
        "disposition": "KEEP",
        "claim_role": f"current manuscript evidence retained in the {placement}",
        "rationale": (
            "Retained by the current manuscript-first source projection as an active "
            "main-text or claim-relevant supporting display."
        ),
        "status": "CURRENT_SOURCE_REFRESH",
        "implementation_status": "IMPLEMENTED",
    }


def rendering_derivative() -> dict[str, str]:
    original = (
        ROOT
        / "figures/ch04-qdesn/pricefm_application/pricefm_regional_aql_editorial_20261013.pdf"
    )
    derivative = original.with_name(
        "pricefm_regional_aql_editorial_20261013_fontsafe.pdf"
    )
    if not original.is_file() or not derivative.is_file():
        raise SystemExit("PriceFM source or font-safe derivative is missing")
    return {
        "source": str(original.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(original.read_bytes()).hexdigest(),
        "destination": str(derivative.relative_to(ROOT)),
        "destination_sha256": hashlib.sha256(derivative.read_bytes()).hexdigest(),
        "transformation": (
            "Ghostscript pdfwrite 9.27 with NoOutputFonts; source plot "
            "lettering converted to vector outlines without changing "
            "plotted data, dimensions, caption, or claim"
        ),
        "reason": (
            "The immutable current-source PDF embeds DejaVuSans as a Type "
            "3 font; the derivative removes that filing-format defect "
            "while preserving source provenance."
        ),
        "rights_status": "UNVERIFIED; inherited from source asset",
    }


def refreshed_payload(existing: dict[str, object]) -> dict[str, object]:
    active = set(current_display_labels())
    existing_records = list(existing.get("records", []))
    by_id = {str(record["id"]): record for record in existing_records}
    if len(by_id) != len(existing_records):
        raise SystemExit("display ledger contains duplicate IDs")

    missing_keep = sorted(
        label
        for label, record in by_id.items()
        if record.get("disposition") == "KEEP" and label not in active
    )
    if missing_keep:
        raise SystemExit(
            "active KEEP displays disappeared without an editorial disposition: "
            + ", ".join(missing_keep)
        )

    records: list[dict[str, object]] = []
    seen: set[str] = set()
    for old in existing_records:
        label = str(old["id"])
        record = dict(old)
        if label in active:
            source, line = locate(label)
            record.update(
                {
                    "chapter": chapter_for(source),
                    "type": display_type(label),
                    "source_file": source,
                    "baseline_line": line,
                }
            )
            if label == "qdesn2026:fig:supp-pricefm-r98-region-comparison":
                record["rendering_derivative"] = rendering_derivative()
        records.append(record)
        seen.add(label)

    for label in sorted(active - seen):
        source, line = locate(label)
        record = new_record(label, source, line)
        if label == "qdesn2026:fig:supp-pricefm-r98-region-comparison":
            record["rendering_derivative"] = rendering_derivative()
        records.append(record)

    payload = dict(existing)
    payload["records"] = records
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Check display source locations by default; use --apply to refresh "
            "locations while preserving OMIT records and editorial metadata."
        )
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    existing = json.loads(LEDGER.read_text(encoding="utf-8"))
    refreshed = refreshed_payload(existing)
    if refreshed == existing:
        print(
            f"display ledger current: {len(existing['records'])} records; "
            "editorial decisions preserved"
        )
        return 0

    if not args.apply:
        raise SystemExit(
            "display ledger locations are stale; inspect the manuscript diff, then run "
            "scripts/update_display_ledger.py --apply"
        )

    refreshed["recorded_at"] = dt.date.today().isoformat()
    LEDGER.write_text(
        json.dumps(refreshed, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    dispositions: dict[str, int] = {}
    for record in refreshed["records"]:
        value = str(record["disposition"])
        dispositions[value] = dispositions.get(value, 0) + 1
    summary = ", ".join(f"{key}={value}" for key, value in sorted(dispositions.items()))
    print(
        f"display ledger refreshed: {len(refreshed['records'])} records ({summary}); "
        "editorial metadata preserved"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
