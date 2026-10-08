#!/usr/bin/env python3.11
"""Validate the active thesis graph, appendix migration, and accessibility ledger."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "main.tex"
MIGRATION = ROOT / "docs" / "appendix-migration-map.json"
ACCESSIBILITY = ROOT / "docs" / "accessibility-ledger.json"
APPENDICES = (
    "appendices/a-shared-conventions",
    "appendices/b-exdqlm-technical",
    "appendices/c-hydrology-technical",
    "appendices/d-qdesn-technical",
    "appendices/e-mti-technical",
)


def uncomment(text: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", line) for line in text.splitlines())


def active_tex_graph(
    root: Path = ROOT, main_file: Path = MAIN
) -> tuple[set[Path], set[str], set[str]]:
    seen: set[Path] = set()
    dynamic_inputs: set[str] = set()
    missing_inputs: set[str] = set()

    def visit(path: Path) -> None:
        path = path.resolve()
        if path in seen or not path.is_file():
            return
        seen.add(path)
        text = uncomment(path.read_text(encoding="utf-8"))
        for argument in re.findall(r"\\(?:input|include)\{([^}]+)\}", text):
            argument = argument.strip()
            if "\\" in argument:
                dynamic_inputs.add(argument)
                continue
            candidate = root / argument
            if not candidate.suffix:
                candidate = Path(f"{candidate}.tex")
            if candidate.is_file():
                visit(candidate)
                continue
            lookup = argument if Path(argument).suffix else f"{argument}.tex"
            resolved = subprocess.run(
                ["kpsewhich", lookup],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
                check=False,
            )
            if resolved.returncode != 0 or not resolved.stdout.strip():
                missing_inputs.add(argument)

    visit(main_file)
    fls = root / "build" / "main.fls"
    if fls.is_file():
        for line in fls.read_text(encoding="utf-8", errors="replace").splitlines():
            if not line.startswith("INPUT "):
                continue
            candidate = Path(line[6:]).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                continue
            if candidate.suffix == ".tex" and candidate.is_file():
                seen.add(candidate)
    return seen, dynamic_inputs, missing_inputs


def active_tex_files() -> tuple[set[Path], set[str]]:
    files, dynamic_inputs, _ = active_tex_graph()
    return files, dynamic_inputs


def duplicate_labels(files: set[Path]) -> dict[str, int]:
    labels: list[str] = []
    for path in files:
        text = uncomment(path.read_text(encoding="utf-8"))
        labels.extend(re.findall(r"\\label\{([^}]+)\}", text))
    return {label: count for label, count in Counter(labels).items() if count > 1}


def load(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")
        return {}


def graphic_records(files: set[Path]) -> set[tuple[str, str]]:
    records: set[tuple[str, str]] = set()
    for path in files:
        text = uncomment(path.read_text(encoding="utf-8"))
        relative = str(path.relative_to(ROOT))
        for argument in re.findall(
            r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", text
        ):
            records.add((relative, argument.strip()))
        # TikZ/input-only figures are still visual content.  Their figure label
        # is the stable ledger key when no includegraphics call exists.
        for block in re.findall(
            r"\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}", text, re.DOTALL
        ):
            if "\\includegraphics" not in block:
                label = re.search(r"\\label\{([^}]+)\}", block)
                if label:
                    records.add((relative, f"label:{label.group(1)}"))
    return records


def main() -> int:
    errors: list[str] = []
    files, dynamic_inputs, missing_inputs = active_tex_graph()
    relative_files = {str(path.relative_to(ROOT)) for path in files}

    for argument in sorted(missing_inputs):
        errors.append(f"active graph has unresolved input {argument!r}")

    main_text = uncomment(MAIN.read_text(encoding="utf-8"))
    appendix_at = main_text.find(r"\appendix")
    bibliography_at = main_text.find(r"\bibliography{references}")
    if appendix_at < 0 or bibliography_at < 0 or appendix_at >= bibliography_at:
        errors.append("main.tex must place appendices before the final bibliography")
    cursor = appendix_at
    for appendix in APPENDICES:
        needle = rf"\input{{{appendix}}}"
        position = main_text.find(needle, cursor)
        if position < 0:
            errors.append(f"main.tex missing or misorders {needle}")
        else:
            cursor = position + len(needle)
        if f"{appendix}.tex" not in relative_files:
            errors.append(f"active graph does not contain {appendix}.tex")
    if "appendices/a-format-demonstration.tex" in relative_files:
        errors.append("inactive formatting demonstration entered the active graph")

    labels: list[str] = []
    forbidden = re.compile(r"/(?:data|home)/[A-Za-z0-9_.@/\-]+")
    for path in files:
        text = uncomment(path.read_text(encoding="utf-8"))
        labels.extend(re.findall(r"\\label\{([^}]+)\}", text))
        if forbidden.search(text):
            errors.append(f"{path.relative_to(ROOT)} contains an absolute server path")
    for label, count in duplicate_labels(files).items():
        errors.append(f"duplicate active label {label!r} appears {count} times")

    migration = load(MIGRATION, errors)
    if migration.get("schema_version") != 1:
        errors.append("appendix migration map must use schema_version 1")
    migration_ids: set[str] = set()
    for index, record in enumerate(migration.get("records", [])):
        where = f"docs/appendix-migration-map.json:records[{index}]"
        ident = record.get("id")
        if not isinstance(ident, str) or not ident.startswith("MIG-"):
            errors.append(f"{where}: invalid id")
            continue
        if ident in migration_ids:
            errors.append(f"{where}: duplicate id {ident}")
        migration_ids.add(ident)
        for field in (
            "source_path",
            "source_heading",
            "source_unit_sha256",
            "disposition",
            "semantic_class",
            "destination_path",
            "appendix_label",
            "risk",
            "review_status",
        ):
            if not record.get(field):
                errors.append(f"{where}: missing {field}")
        destination = ROOT / str(record.get("destination_path", ""))
        if not destination.is_file():
            errors.append(f"{where}: missing destination")
        elif f"% migration-id: {ident}" not in destination.read_text(encoding="utf-8"):
            errors.append(f"{where}: destination lacks migration marker")
        source = ROOT / str(record.get("source_path", ""))
        if not source.is_file():
            errors.append(f"{where}: missing source derivative")
        elif str(record.get("appendix_label")) not in source.read_text(encoding="utf-8"):
            errors.append(f"{where}: body bridge lacks appendix reference")
        if record.get("disposition") != "MOVE_APPENDIX":
            errors.append(f"{where}: unsupported disposition")

    accessibility = load(ACCESSIBILITY, errors)
    if accessibility.get("schema_version") != 1:
        errors.append("accessibility ledger must use schema_version 1")
    ledger_keys: set[tuple[str, str]] = set()
    for index, record in enumerate(accessibility.get("graphics", [])):
        where = f"docs/accessibility-ledger.json:graphics[{index}]"
        key = (str(record.get("source_path", "")), str(record.get("graphic", "")))
        if key in ledger_keys:
            errors.append(f"{where}: duplicate graphic record")
        ledger_keys.add(key)
        if not record.get("alt_text"):
            errors.append(f"{where}: missing alt_text")
        if record.get("status") not in {"REVIEWED", "AUTHOR_REVIEW_REQUIRED"}:
            errors.append(f"{where}: invalid status")
    active_graphics = graphic_records(files)
    missing_graphics = sorted(active_graphics - ledger_keys)
    stale_graphics = sorted(ledger_keys - active_graphics)
    if missing_graphics:
        errors.append("active graphics missing from accessibility ledger: " + repr(missing_graphics))
    if stale_graphics:
        errors.append("inactive graphics in accessibility ledger: " + repr(stale_graphics))

    if errors:
        print("Structure validation: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        "Structure validation: PASS\n"
        f"- {len(files)} active TeX files ({len(dynamic_inputs)} compiler-resolved macro inputs)\n"
        f"- {len(labels)} unique active labels; {len(migration_ids)} migration records\n"
        f"- {len(active_graphics)} active graphic/visual records covered by the accessibility ledger"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
