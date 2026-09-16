#!/usr/bin/env python3.11
"""Validate editorial issue, display, and bibliography decision records."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ISSUES = ROOT / "docs" / "editorial-issues.json"
DISPLAYS = ROOT / "docs" / "display-ledger.json"
BIBLIOGRAPHY = ROOT / "docs" / "bibliography-map.json"
CHAPTERS = {
    "ch02-exdqlm": ROOT / "chapters" / "02-research-a.tex",
    "ch03-environ": ROOT / "chapters" / "03-research-b.tex",
    "ch04-qdesn": ROOT / "chapters" / "04-research-c.tex",
    "ch05-mti": ROOT / "chapters" / "05-research-d.tex",
}


def fail(errors: list[str]) -> int:
    if not errors:
        return 0
    print("Editorial-audit validation: FAIL", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    return 1


def load(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")
        return {}


def current_display_labels() -> set[str]:
    seen: set[Path] = set()
    labels: set[str] = set()

    def visit(path: Path) -> None:
        path = path.resolve()
        if path in seen or not path.is_file():
            return
        seen.add(path)
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(
            r"\\begin\{(?:figure\*?|table\*?|longtable)\}(.*?)"
            r"\\end\{(?:figure\*?|table\*?|longtable)\}",
            text,
            re.DOTALL,
        ):
            label = re.search(r"\\label\{([^}]+)\}", match.group(1))
            if label:
                labels.add(label.group(1))
        for argument in re.findall(r"\\input\{([^}]+)\}", text):
            if argument.startswith("\\"):
                continue
            dependency = ROOT / argument
            if not dependency.suffix:
                dependency = Path(f"{dependency}.tex")
            visit(dependency)

    for chapter in CHAPTERS.values():
        visit(chapter)
    return labels


def bibliography_keys() -> set[str]:
    text = (ROOT / "references.bib").read_text(encoding="utf-8")
    return {
        match.group(1)
        for match in re.finditer(r"(?m)^@[A-Za-z]+\s*[({]\s*([^,\s]+)\s*,", text)
    }


def main() -> int:
    errors: list[str] = []
    issues = load(ISSUES, errors)
    displays = load(DISPLAYS, errors)
    bibliography = load(BIBLIOGRAPHY, errors)

    issue_ids: set[str] = set()
    for index, record in enumerate(issues.get("records", [])):
        where = f"docs/editorial-issues.json:records[{index}]"
        issue_id = record.get("id")
        if not isinstance(issue_id, str) or not issue_id.startswith("ED-"):
            errors.append(f"{where}: invalid issue id")
        elif issue_id in issue_ids:
            errors.append(f"{where}: duplicate issue id {issue_id}")
        issue_ids.add(str(issue_id))
        if record.get("severity") not in {"blocking", "major", "moderate", "minor"}:
            errors.append(f"{where}: invalid severity")
        for field in (
            "chapter",
            "locator",
            "issue_type",
            "evidence",
            "proposed_action",
            "source_provenance",
            "validation",
        ):
            if not record.get(field):
                errors.append(f"{where}: missing {field}")
        if not isinstance(record.get("author_input_required"), bool):
            errors.append(f"{where}: author_input_required must be boolean")

    display_ids: set[str] = set()
    disposition_counts = {key: 0 for key in ("KEEP", "MERGE", "TEXT-SUMMARY", "OMIT")}
    for index, record in enumerate(displays.get("records", [])):
        where = f"docs/display-ledger.json:records[{index}]"
        display_id = record.get("id")
        if not isinstance(display_id, str) or not display_id:
            errors.append(f"{where}: invalid display id")
            continue
        if display_id in display_ids:
            errors.append(f"{where}: duplicate display id {display_id}")
        display_ids.add(display_id)
        disposition = record.get("disposition")
        if disposition not in disposition_counts:
            errors.append(f"{where}: invalid disposition {disposition!r}")
        else:
            disposition_counts[disposition] += 1
        implementation = record.get("implementation_status")
        if implementation not in {"PENDING", "IMPLEMENTED"}:
            errors.append(f"{where}: invalid implementation status")
        for field in ("chapter", "type", "source_file", "claim_role", "rationale"):
            if not record.get(field):
                errors.append(f"{where}: missing {field}")

    current = current_display_labels()
    unrecorded = sorted(current - display_ids)
    if unrecorded:
        errors.append("unrecorded current displays: " + ", ".join(unrecorded))
    for record in displays.get("records", []):
        if record.get("implementation_status") == "PENDING" and record.get("id") not in current:
            errors.append(f"pending display is absent: {record.get('id')}")
        if record.get("disposition") == "KEEP" and record.get("id") not in current:
            errors.append(f"KEEP display is absent: {record.get('id')}")

    bib_keys = bibliography_keys()
    mapped_replacements: set[str] = set()
    canonical_keys: set[str] = set()
    for index, record in enumerate(bibliography.get("records", [])):
        where = f"docs/bibliography-map.json:records[{index}]"
        canonical = record.get("canonical_key")
        replacements = record.get("replace_keys")
        if not isinstance(canonical, str) or not canonical:
            errors.append(f"{where}: invalid canonical key")
        else:
            canonical_keys.add(canonical)
            if canonical not in bib_keys:
                errors.append(f"{where}: canonical key missing from references.bib")
        if not isinstance(replacements, list) or not replacements:
            errors.append(f"{where}: replace_keys must be nonempty")
        else:
            for replacement in replacements:
                if replacement in mapped_replacements:
                    errors.append(f"{where}: duplicate replacement mapping {replacement}")
                mapped_replacements.add(replacement)
        if not record.get("action") or not record.get("basis"):
            errors.append(f"{where}: action and basis are required")

    result = fail(errors)
    if result:
        return result
    print(
        "Editorial-audit validation: PASS\n"
        f"- {len(issue_ids)} prioritized issues\n"
        f"- {len(display_ids)} displays: "
        + ", ".join(f"{key}={value}" for key, value in disposition_counts.items())
        + "\n"
        f"- {len(bibliography.get('records', []))} bibliography reconciliation groups"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
