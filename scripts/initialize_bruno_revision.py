#!/usr/bin/env python3.11
"""Create and validate the reproducible Bruno-revision control records."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs" / "bruno-revision-integration-plan-20261109.md"
MATRIX = ROOT / "docs" / "bruno-revision-response-matrix-20261109.json"
BASELINE = ROOT / "docs" / "bruno-revision-preedit-baseline-20261109.json"

FILES = (
    "chapters/04-research-c.tex",
    "appendices/d-qdesn-technical.tex",
    "chapters/05-research-d.tex",
    "appendices/e-mti-technical.tex",
    "chapters/01-introduction.tex",
    "frontmatter/abstract.tex",
    "chapters/06-synthesis.tex",
    "frontmatter/acknowledgments.tex",
    "notation.tex",
    "references.bib",
    "source-manifest.json",
)

EXPECTED = {"B4": 40, "B5": 65, "BE": 11}
COMMITS = {
    "SRC-QDESN": "aa613b056b054edd9347eeb4739bd4bce0c92818",
    "SRC-RQR": "4223c6a3a44f376255bacdca91db71cdf4f3afde",
    "SRC-MTI-EXT": "f345d946aa5a81b94795838bec58d874a0fdd0c9",
}

EXACT_SOURCE = {
    "B4-012": ("SRC-QDESN", "main.tex", "lines 180--182"),
    "B4-016": ("SRC-QDESN", "main.tex", "lines 277--281"),
    "B4-019": ("SRC-QDESN", "main.tex", "lines 291--312"),
    "B4-033": ("SRC-QDESN", "qdesn-supplement.tex", "lines 246--278"),
    "B4-040": ("SRC-QDESN", "main.tex and qdesn-supplement.tex", "complete affected definitions"),
    "B5-042": ("SRC-RQR", "main.tex", "lines 662--684"),
    "B5-043": ("SRC-RQR", "main.tex and rqr-gibbs-supplement.tex", "main lines 662--684 and convex profile derivation"),
    "B5-045": ("SRC-RQR", "rqr-gibbs-supplement.tex", "lines 1147--1186"),
    "B5-046": ("SRC-RQR", "rqr-gibbs-supplement.tex", "lines 1147--1186"),
    "B5-047": ("SRC-RQR", "rqr-gibbs-supplement.tex", "lines 1147--1186"),
    "B5-048": ("SRC-RQR", "main.tex", "fixed-target and calibrated-selection specification"),
    "B5-049": ("SRC-RQR", "main.tex", "fixed-target and calibrated-selection specification"),
    "B5-050": ("SRC-RQR", "rqr-gibbs-supplement.tex", "lines 1147--1186"),
    "B5-053": ("SRC-RQR", "rqr-gibbs-supplement.tex", "lines 1242--1267"),
    "B5-054": ("SRC-RQR", "rqr-gibbs-supplement.tex", "lines 1242--1267"),
    "B5-059": ("SRC-RQR", "rqr-gibbs-supplement.tex", "lines 1357--1397"),
    "B5-060": ("SRC-RQR", "rqr-gibbs-supplement.tex", "lines 1357--1397"),
}


def target(item_id: str) -> tuple[str, str, str]:
    number = int(item_id.split("-")[1])
    if item_id.startswith("B4"):
        if number <= 13:
            return "C1", "chapters/04-research-c.tex", "qdesn2026:sec:intro; pre-edit lines 1--137"
        if number <= 29:
            return "C1", "chapters/04-research-c.tex", "qdesn2026:sec:model; pre-edit lines 138--316"
        if number <= 36:
            return "C1", "chapters/04-research-c.tex", "qdesn2026:sec:inference; pre-edit lines 317--371"
        return "C1", "chapters/04-research-c.tex", "qdesn2026:sec:forecast; pre-edit lines 372--502"
    if item_id.startswith("BE"):
        return "C2/C3", "appendices/e-mti-technical.tex", "Appendix E; pre-edit lines 1--357"
    if number <= 17:
        return "C2", "chapters/05-research-d.tex", "rqr2026:sec:introduction--rqr2026:sec:interval-functionals; pre-edit lines 1--126"
    if number <= 38:
        return "C2", "chapters/05-research-d.tex", "rqr2026:sec:mpi-loss--rqr2026:sec:mti-loss; pre-edit lines 127--459"
    if number <= 51:
        return "C3", "chapters/05-research-d.tex", "rqr2026:sec:static-theory-statements--rqr2026:sec:mti-tolerance; pre-edit lines 460--597"
    return "C3", "chapters/05-research-d.tex", "rqr2026:sec:evaluation; pre-edit lines 598--736"


def source(item_id: str) -> dict[str, str]:
    if item_id in EXACT_SOURCE:
        source_id, path, locator = EXACT_SOURCE[item_id]
        return {
            "classification": "exact_fixed_source",
            "source_id": source_id,
            "commit": COMMITS[source_id],
            "path": path,
            "locator": locator,
        }
    source_id = "SRC-QDESN" if item_id.startswith("B4") else "SRC-RQR"
    return {
        "classification": "fixed_source_consistency_or_not_source_dependent",
        "source_id": source_id,
        "commit": COMMITS[source_id],
        "path": "main.tex and supplement as applicable",
        "locator": "record an exact locator before closing the item when wording changes a scientific statement",
    }


def parse_plan() -> list[dict[str, object]]:
    row = re.compile(r"^\| (B4|B5|BE)-(\d{3}) \| ([^|]+) \| ([A-Z_]+) \| (.+) \|$")
    items: list[dict[str, object]] = []
    for line in PLAN.read_text(encoding="utf-8").splitlines():
        match = row.match(line)
        if not match:
            continue
        prefix, number, review_page, plan_status, resolution = match.groups()
        item_id = f"{prefix}-{number}"
        commit_unit, destination, anchor = target(item_id)
        disposition = {
            "SATISFIED_CURRENT": "preserve_and_verify",
            "PARTIAL": "clarify_or_restructure",
            "OPEN_EDIT": "edit",
            "SOURCE_RESOLVED_EDIT": "source_resolved_edit",
            "CONTROL_GATE": "verify_only",
        }[plan_status]
        final_status = {
            "SATISFIED_CURRENT": "PRESERVATION_PENDING_VALIDATION",
            "CONTROL_GATE": "CONTROL_PENDING",
        }.get(plan_status, "IMPLEMENTATION_PENDING")
        items.append(
            {
                "id": item_id,
                "review_page": review_page.strip(),
                "issue_and_acceptance": resolution.strip(),
                "plan_status": plan_status,
                "commit_unit": commit_unit,
                "pre_edit_target": {"file": destination, "anchor": anchor},
                "source": source(item_id),
                "disposition": disposition,
                "selected_resolution": resolution.strip(),
                "alternative_control": "Use the bounded current-source resolution; do not restore the reviewed 221-page wording or copy an article section wholesale.",
                "changed_files": [],
                "validation_evidence": [],
                "final_status": final_status,
                "final_commit": None,
                "unresolved_decision": "Identify the possible additional comparator before inclusion." if item_id == "B5-058" else None,
            }
        )
    return items


def extract(pattern: str, text: str) -> list[str]:
    return re.findall(pattern, text, flags=re.MULTILINE)


def snapshot(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    citations: list[str] = []
    for group in extract(r"\\cite\w*\{([^}]*)\}", text):
        citations.extend(key.strip() for key in group.split(",") if key.strip())
    return {
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "lines": text.count("\n") + (0 if text.endswith("\n") else 1),
        "numeric_tokens": extract(r"(?<![A-Za-z])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", text),
        "citation_keys": citations,
        "labels": extract(r"\\label\{([^}]+)\}", text),
        "input_paths": extract(r"\\(?:input|include)\{([^}]+)\}", text),
        "graphic_paths": extract(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", text),
        "equation_environments": extract(r"\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|split)\}", text),
    }


def validate(items: list[dict[str, object]]) -> None:
    ids = [str(item["id"]) for item in items]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate response-matrix IDs")
    for prefix, expected in EXPECTED.items():
        actual_ids = sorted(item_id for item_id in ids if item_id.startswith(prefix + "-"))
        expected_ids = [f"{prefix}-{number:03d}" for number in range(1, expected + 1)]
        if actual_ids != expected_ids:
            raise SystemExit(f"{prefix} coverage mismatch")
    if len(items) != sum(EXPECTED.values()):
        raise SystemExit("response-matrix total is not 116")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("initialize", "validate"))
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    if args.command == "initialize":
        if (MATRIX.exists() or BASELINE.exists()) and not args.force:
            raise SystemExit("control record exists; use --force only before manuscript editing")
        items = parse_plan()
        validate(items)
        matrix = {
            "schema_version": 1,
            "recorded_at": "2026-11-09",
            "status": "IMPLEMENTATION_PREFLIGHT",
            "plan": str(PLAN.relative_to(ROOT)),
            "baseline_commit": "ac00a38a6fbbec9ac57ffb157fe7de99673f7540",
            "authority_commits": COMMITS,
            "review_boundary": "Bruno Sanso reviewed Chapter 4 only through Section 4.4; Chapter 5 and Appendix E comments are itemized from the received annotation.",
            "items": items,
        }
        baseline = {
            "schema_version": 1,
            "recorded_at": "2026-11-09",
            "purpose": "Immutable pre-edit sequences for detecting unintended scientific or structural drift during the Bruno revision.",
            "files": {relative: snapshot(ROOT / relative) for relative in FILES},
        }
        MATRIX.write_text(json.dumps(matrix, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        BASELINE.write_text(json.dumps(baseline, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"initialized {len(items)} response items and {len(FILES)} baseline files")
        return

    data = json.loads(MATRIX.read_text(encoding="utf-8"))
    validate(data["items"])
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    if set(baseline["files"]) != set(FILES):
        raise SystemExit("pre-edit baseline file set mismatch")
    print("Bruno revision controls: PASS (116 items; pre-edit baseline present)")


if __name__ == "__main__":
    main()
