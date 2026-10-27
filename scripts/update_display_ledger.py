#!/usr/bin/env python3.11
"""Rebuild the display ledger for the active current-source dissertation graph."""

from __future__ import annotations

import json
import hashlib
from pathlib import Path

from validate_editorial_audit import ROOT, current_display_labels


def locate(label: str) -> tuple[str, int]:
    needle = rf"\label{{{label}}}"
    roots = (
        ROOT / "chapters", ROOT / "appendices", ROOT / "tables", ROOT / "figures"
    )
    for directory in roots:
        for path in sorted(directory.rglob("*.tex")):
            text = path.read_text(encoding="utf-8", errors="replace")
            if needle in text:
                return str(path.relative_to(ROOT)), text[: text.index(needle)].count("\n") + 1
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
    if ":fig:" in label:
        return "figure"
    return "table"


def main() -> int:
    labels = sorted(current_display_labels())
    records = []
    for label in labels:
        source, line = locate(label)
        placement = "technical appendix" if source.startswith("appendices/") else "reading chapter"
        record = {
            "id": label,
            "chapter": chapter_for(source),
            "type": display_type(label),
            "source_file": source,
            "baseline_line": line,
            "disposition": "KEEP",
            "claim_role": f"current manuscript evidence retained in the {placement}",
            "rationale": (
                "Retained by the 2026-10-26 manuscript-first refresh as an active "
                "main-text or claim-relevant supporting display."
            ),
            "status": "CURRENT_SOURCE_REFRESH",
            "implementation_status": "IMPLEMENTED",
        }
        if label == "qdesn2026:fig:supp-pricefm-r98-region-comparison":
            original = (
                ROOT / "figures/ch04-qdesn/pricefm_application/"
                "pricefm_regional_aql_editorial_20261013.pdf"
            )
            derivative = original.with_name(
                "pricefm_regional_aql_editorial_20261013_fontsafe.pdf"
            )
            if not original.is_file() or not derivative.is_file():
                raise SystemExit("PriceFM source or font-safe derivative is missing")
            record["rendering_derivative"] = {
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
        records.append(record)
    payload = {
        "schema_version": 1,
        "recorded_at": "2026-10-26",
        "scope": (
            "All labeled figure, table, and longtable environments transitively "
            "included by research Chapters 2--5 and their technical appendices "
            "after the current-source refresh."
        ),
        "decision_meanings": {
            "KEEP": "retain as a distinct thesis display",
            "MERGE": "combine with related displays",
            "TEXT-SUMMARY": "replace the float with an exact prose summary",
            "OMIT": "remove from the thesis body while retaining provenance",
        },
        "records": records,
    }
    path = ROOT / "docs/display-ledger.json"
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"display ledger written: {len(records)} active displays")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
