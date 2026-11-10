#!/usr/bin/env python3.11
"""Validate the 10 November author-comment response contract."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "docs" / "author-comments-preedit-baseline-20261110.json"
MATRIX = ROOT / "docs" / "author-comments-response-matrix-20261110.json"

EXPECTED_ADVISOR_HASHES = {
    "docs/bruno-revision-response-matrix-20261109.json": "8f600eed1a96f7ac86b8830ca76b49c02a996195a23ac2c793895be325bbbc02",
    "docs/bruno-revision-preedit-baseline-20261109.json": "090f11ef8371a25ce8da6a20587c4a1de680acef1da8a3c6a938384f9a9c84e7",
}

ALLOWED_STATUS = {
    "OPEN",
    "SOURCE_VERIFIED",
    "IMPLEMENTED_PENDING_VALIDATION",
    "IMPLEMENTED_VALIDATED",
    "DEFERRED_WITH_REASON",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(input_root: Path | None = None, require_complete: bool = False) -> None:
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    items = matrix.get("items", [])
    expected_ids = [f"AR-{number:03d}" for number in range(1, 23)]
    ids = [item.get("id") for item in items]
    if ids != expected_ids:
        raise SystemExit("author response matrix must contain AR-001 through AR-022 in order")
    if len(ids) != len(set(ids)):
        raise SystemExit("author response matrix contains duplicate IDs")

    for item in items:
        missing = [
            field
            for field in (
                "source_comment",
                "issue",
                "targets",
                "selected_resolution",
                "acceptance",
                "status",
                "changed_files",
                "validation",
            )
            if field not in item
        ]
        if missing:
            raise SystemExit(f"{item['id']} lacks fields: {', '.join(missing)}")
        if item["status"] not in ALLOWED_STATUS:
            raise SystemExit(f"{item['id']} has invalid status {item['status']}")
        if item["status"] == "DEFERRED_WITH_REASON" and not item.get("deferred_reason"):
            raise SystemExit(f"{item['id']} is deferred without a reason")

    complete = require_complete or matrix.get("status") == "IMPLEMENTED_VALIDATED"
    if complete:
        incomplete = [
            item["id"]
            for item in items
            if item["status"] != "IMPLEMENTED_VALIDATED"
        ]
        if incomplete:
            raise SystemExit("author response items remain incomplete: " + ", ".join(incomplete))
        for item in items:
            if not item["changed_files"] or not item["validation"]:
                raise SystemExit(f"{item['id']} lacks implementation evidence")

    for relative, expected in EXPECTED_ADVISOR_HASHES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise SystemExit(f"immutable advisor control changed: {relative}")

    if input_root is not None:
        for record in baseline["input_records"]:
            path = input_root / record["local_name"]
            if not path.is_file():
                raise SystemExit(f"missing author input: {path}")
            if sha256(path) != record["sha256"]:
                raise SystemExit(f"author input hash mismatch: {path.name}")

    display = json.loads((ROOT / "docs/display-ledger.json").read_text(encoding="utf-8"))
    dispositions = Counter(record["disposition"] for record in display["records"])
    if len(display["records"]) != 35 or dispositions != Counter({"KEEP": 33, "OMIT": 2}):
        raise SystemExit("display ledger must retain 35 records: 33 KEEP and 2 OMIT")

    if complete:
        active_text = "\n".join(
            path.read_text(encoding="utf-8", errors="replace")
            for group in ("frontmatter", "chapters", "appendices", "tables")
            for path in sorted((ROOT / group).rglob("*.tex"))
        )
        if "tab:intro-interval-objects" in active_text:
            raise SystemExit("the authorized introductory interval table label remains")
        forbidden = (
            "Yan and coauthors",
            "Barata and coauthors",
            "The available records do not assign",
            "The common lesson is that computational similarity",
        )
        present = [phrase for phrase in forbidden if phrase in active_text]
        if present:
            raise SystemExit("superseded prose remains: " + "; ".join(present))

        table = (ROOT / "tables/ch03-environ/corrected3/main_calibration.tex").read_text(
            encoding="utf-8"
        )
        required_percentages = (
            "123/140 (87.9\\%)",
            "132/140 (94.3\\%)",
            "29/40 (72.5\\%)",
            "35/40 (87.5\\%)",
        )
        if any(value not in table for value in required_percentages):
            raise SystemExit("hydrology coverage table lacks required count-percentage pairs")

    print(
        "author-comment revision: PASS; "
        f"22 items; statuses={dict(sorted(Counter(item['status'] for item in items).items()))}"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-root", type=Path)
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()
    validate(args.input_root, args.require_complete)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
