#!/usr/bin/env python3.11
"""Create the initial figure accessibility ledger from the active TeX graph.

Existing ``\figalt`` text is preferred.  Otherwise the full caption supplies a
conservative draft description and is explicitly marked for author review.
The ledger is a source-control aid; it does not claim that the generated PDF is
tagged or that an external WCAG checker has passed it.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from validate_structure import ROOT, active_tex_files, uncomment


OUTPUT = ROOT / "docs" / "accessibility-ledger.json"


def braced_argument(text: str, command: str) -> str | None:
    match = re.search(rf"\\{command}(?:\[[^\]]*\])?\s*\{{", text)
    if not match:
        return None
    start = match.end() - 1
    depth = 0
    for index in range(start, len(text)):
        if text[index] == "{" and (index == 0 or text[index - 1] != "\\"):
            depth += 1
        elif text[index] == "}" and (index == 0 or text[index - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return text[start + 1 : index]
    return None


def plain(text: str) -> str:
    text = re.sub(r"(?<!\\)%.*", " ", text)
    text = re.sub(r"\\(?:input|include)\{([^}]+)\}", r"supporting source \1", text)
    text = re.sub(r"\\(?:ref|eqref|cite|citep|citet)\{([^}]+)\}", r"\1", text)
    text = re.sub(r"\\(?:texttt|textit|textbf|emph|pkg|code|proglang)\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = text.replace("{", "").replace("}", "")
    text = text.replace("$", "").replace("~", " ")
    text = re.sub(r"\\%", " percent ", text)
    text = re.sub(r"\\[&_#]", " ", text)
    text = re.sub(r"\\[(),;!]", " ", text)
    return " ".join(text.split()).strip()


def main() -> int:
    if OUTPUT.exists():
        raise SystemExit("refusing to overwrite docs/accessibility-ledger.json")
    files, _ = active_tex_files()
    records: list[dict[str, object]] = []
    for path in sorted(files):
        text = uncomment(path.read_text(encoding="utf-8"))
        for block in re.findall(
            r"\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}", text, re.DOTALL
        ):
            graphics = re.findall(
                r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", block
            )
            label_match = re.search(r"\\label\{([^}]+)\}", block)
            label = label_match.group(1) if label_match else None
            if not graphics and label:
                graphics = [f"label:{label}"]
            if not graphics:
                continue
            explicit = braced_argument(block, "figalt")
            caption = braced_argument(block, "caption")
            description = plain(explicit or caption or "")
            if not description:
                description = f"Visual identified by {label or graphics[0]}; description requires author review."
            for graphic in graphics:
                records.append(
                    {
                        "source_path": str(path.relative_to(ROOT)),
                        "graphic": graphic.strip(),
                        "figure_label": label,
                        "alt_text": description,
                        "description_source": "figalt" if explicit else "caption",
                        "status": "REVIEWED" if explicit else "AUTHOR_REVIEW_REQUIRED",
                    }
                )
    payload = {
        "schema_version": 1,
        "recorded_at": "2026-10-08",
        "scope": "Every active figure or included graphic in the compiler-recorded thesis graph.",
        "conformance_boundary": (
            "This ledger provides source descriptions only. The muscat TeX Live 2018 PDF is untagged; "
            "WCAG 2.1 AA and PDF/UA conformance require a modern tagged build and external checker plus manual review."
        ),
        "production_pdf_status": "UNTAGGED_BASELINE_NOT_ACCESSIBILITY_CONFORMANT",
        "graphics": records,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"accessibility ledger written: {len(records)} active visual records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
