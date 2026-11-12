#!/usr/bin/env python3.11
"""Validate final authorial voice, targeted prose decisions, and result curation."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from validate_structure import ROOT, active_tex_files, uncomment


MATRIX = ROOT / "docs" / "final-voice-exdqlm-mti-response-matrix-20261110.json"
MANIFEST = ROOT / "source-manifest.json"

SINGULAR = re.compile(
    r"(?<![A-Za-z-])(?:I|[Mm]e|[Mm]y|[Mm]ine|[Mm]yself)(?![A-Za-z-])"
)
THIRD_PERSON_SELF = re.compile(
    r"\b(?:the candidate|the dissertation author)(?:['’]s)?\b", re.IGNORECASE
)
MATH_ENVIRONMENTS = (
    "equation",
    "equation*",
    "align",
    "align*",
    "alignat",
    "alignat*",
    "gather",
    "gather*",
    "multline",
    "multline*",
    "displaymath",
    "math",
)
FORBIDDEN_PHRASES = (
    "software ecosystem",
    "composable model-construction interface",
    "end-to-end training",
    "should not be interpreted",
    "records this result",
    "This proposition concerns stationary points",
    "matters because",
)
REMOVED_LABELS = {
    "rqr2026:prop:mean-tilt",
    "rqr2026:cor:recovery-tilts",
    "rqr2026:prop:supp-convex-order",
    "rqr2026:lem:supp-profile-radius",
    "rqr2026:thm:supp-fractional-balance",
}
RETAINED_LABELS = {
    "rqr2026:prop:population-characterization",
    "rqr2026:thm:quantile-window",
    "rqr2026:thm:profiled-mean-tilt",
}


def prose_only(text: str) -> str:
    """Remove comments and mathematical regions while retaining prose arguments."""
    cleaned = uncomment(text)
    cleaned = re.sub(
        r"^\s*\\(?:providecommand|newcommand|renewcommand|DeclareMathOperator)\b.*$",
        " ",
        cleaned,
        flags=re.MULTILINE,
    )
    cleaned = re.sub(
        r"\\(?:cite|citep|citet|citealp|citeauthor|citeyear|ref|eqref|pageref|autoref|label)"
        r"(?:\[[^]]*\])?\{[^}]*\}",
        " ",
        cleaned,
    )
    for environment in MATH_ENVIRONMENTS:
        cleaned = re.sub(
            rf"\\begin\{{{re.escape(environment)}\}}.*?"
            rf"\\end\{{{re.escape(environment)}\}}",
            " ",
            cleaned,
            flags=re.DOTALL,
        )
    cleaned = re.sub(r"\\\[.*?\\\]", " ", cleaned, flags=re.DOTALL)
    cleaned = re.sub(r"\\\(.*?\\\)", " ", cleaned, flags=re.DOTALL)
    cleaned = re.sub(r"(?<!\\)\$\$.*?(?<!\\)\$\$", " ", cleaned, flags=re.DOTALL)
    cleaned = re.sub(r"(?<!\\)\$.*?(?<!\\)\$", " ", cleaned, flags=re.DOTALL)
    return cleaned


def singular_pronoun_hits(files: set[Path]) -> list[str]:
    hits: list[str] = []
    for path in sorted(files):
        try:
            relative = path.relative_to(ROOT)
        except ValueError:
            relative = Path(path.name)
        prose = prose_only(path.read_text(encoding="utf-8"))
        for line_number, line in enumerate(prose.splitlines(), start=1):
            if SINGULAR.search(line):
                hits.append(f"{relative}:{line_number}: {line.strip()}")
    return hits


def third_person_self_hits(files: set[Path]) -> list[str]:
    """Report third-person references to the dissertation student in active prose."""
    hits: list[str] = []
    for path in sorted(files):
        try:
            relative = path.relative_to(ROOT)
        except ValueError:
            relative = Path(path.name)
        prose = prose_only(path.read_text(encoding="utf-8"))
        for line_number, line in enumerate(prose.splitlines(), start=1):
            if THIRD_PERSON_SELF.search(line):
                hits.append(f"{relative}:{line_number}: {line.strip()}")
    return hits


def main() -> int:
    errors: list[str] = []
    files, _ = active_tex_files()
    active_text = "\n".join(
        uncomment(path.read_text(encoding="utf-8")) for path in sorted(files)
    )

    for hit in singular_pronoun_hits(files):
        errors.append(f"first-person singular prose: {hit}")
    for hit in third_person_self_hits(files):
        errors.append(f"third-person self-reference: {hit}")

    folded = active_text.casefold()
    for phrase in FORBIDDEN_PHRASES:
        if phrase.casefold() in folded:
            errors.append(f"forbidden targeted phrase remains: {phrase}")

    labels = set(re.findall(r"\\label\{([^}]+)\}", active_text))
    references = set(
        re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}", active_text)
    )
    for label in sorted(RETAINED_LABELS - labels):
        errors.append(f"retained MTI result label missing: {label}")
    for label in sorted(REMOVED_LABELS & (labels | references)):
        errors.append(f"removed MTI result label remains active: {label}")

    try:
        matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"response matrix unavailable: {exc}")
        matrix = {}
    if matrix.get("status") != "IMPLEMENTED_VALIDATED":
        errors.append("response matrix is not IMPLEMENTED_VALIDATED")
    for item in matrix.get("items", []):
        if item.get("status") != "IMPLEMENTED_VALIDATED":
            errors.append(f"response item not closed: {item.get('id')}")

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"source manifest unavailable: {exc}")
        manifest = {}
    package = next(
        (
            item
            for item in manifest.get("sources", [])
            if item.get("id") == "SRC-EXDQLM-PKG"
        ),
        {},
    )
    snapshots = {
        item.get("id"): item.get("commit")
        for item in package.get("related_snapshots", [])
    }
    if snapshots.get("SNAP-EXDQLM-ORIGINAL011") != (
        "49cea5a48b2992d58eceb583e333bf08333e9be6"
    ):
        errors.append("original exdqlm 0.1.1 snapshot is missing or incorrect")
    if package.get("audit_commit") != "e51045a4324901cced27ca2aaa22569afbc8e0e6":
        errors.append("current exdqlm package authority changed unexpectedly")

    if errors:
        print("Final voice/style validation: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Final voice/style validation: PASS "
        f"({len(files)} active TeX files; {len(RETAINED_LABELS)} retained MTI results)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
