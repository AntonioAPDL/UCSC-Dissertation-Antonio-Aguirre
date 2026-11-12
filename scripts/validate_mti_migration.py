#!/usr/bin/env python3.11
"""Check the evidence and active prose of the Chapter 5 ECM/Gibbs migration.

These checks protect manuscript/source consistency, not sampler convergence or
the accuracy of application fits.  Numerical research evidence remains attached
to the immutable source manifests named in the migration record.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECORD = "docs/ch05-mti-ecm-gibbs-migration-20261111.json"
REQUIRED_LABELS = {
    "rqr2026:eq:mti-computational-loss",
    "rqr2026:eq:mti-generalized-posterior",
    "rqr2026:eq:mti-root-conditionals",
    "rqr2026:eq:mti-scale-conditional",
    "app:mti-computation",
    "alg:ch05-mti-gibbs",
    "alg:ch05-mti-ecm",
}
RETIRED_ACTIVE_LABELS = {
    "app:mti-profile-computation",
    "rqr2026:prop:supp-convex-intercept-profile",
}
STALE_PRODUCTION_PHRASES = (
    "strongly convex midpoint profile gives the penalized-loss minimizer",
    "endpoints by a convex profile calculation",
    "the profile objective-gap criterion is met",
    "profiled MTI attainment ranges from 95.1",
    "MTI has smaller mean width than Young--Mathew in 40 of 72",
)
UNSUPPORTED_GIBBS_PATTERNS = (
    r"Gibbs\s+(?:posterior\s+)?means?\s+(?:are|were|is|was)\s+"
    r"(?:(?:approximately|nearly)\s+)?(?:equal|comparable|similar)",
    r"ECM\s+(?:is|was)\s+\d+(?:\.\d+)?\s*(?:times|[x×])\s+faster",
)


def uncomment(text: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", line) for line in text.splitlines())


def normalized(text: str) -> str:
    return " ".join(uncomment(text).split())


def text_errors(chapter: str, appendix: str, context: str, record: dict) -> list[str]:
    errors: list[str] = []
    technical = uncomment(chapter + "\n" + appendix)
    labels = set(re.findall(r"\\label\{([^}]+)\}", technical))
    references = set(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", technical))
    for label in sorted(REQUIRED_LABELS - labels):
        errors.append(f"missing ECM/Gibbs method label: {label}")
    for label in sorted(RETIRED_ACTIVE_LABELS & (labels | references)):
        errors.append(f"retired computational profile label remains active: {label}")

    prose = normalized(technical + "\n" + context)
    for phrase in STALE_PRODUCTION_PHRASES:
        if phrase.casefold() in prose.casefold():
            errors.append(f"superseded computational/result statement: {phrase}")

    # With the response-unit retained-mean tilt, the endpoint linear term has
    # the negative sign in the loss and the positive sign in canonical H_j.
    compact = re.sub(r"\s+", "", technical)
    if not re.search(r"-q\\delta\(?a\+b-2y_i\)?", compact):
        errors.append("fixed-target computational loss lacks -q delta (a+b-2y_i)")
    if not re.search(r"\+\\omega_\{\\mathrm\{?R\}?\}nq\\delta", compact):
        errors.append("Gaussian root canonical parameter lacks +omega_R n q delta")

    if record.get("gibbs_empirical_status") == "NOT_REPORTED":
        for pattern in UNSUPPORTED_GIBBS_PATTERNS:
            if re.search(pattern, prose, re.IGNORECASE):
                errors.append("unverified Gibbs/ECM empirical equivalence or speed ratio")
    else:
        errors.append("this migration requires the authenticated NOT_REPORTED Gibbs boundary")
    if "ECM" not in appendix or "Gibbs" not in appendix:
        errors.append("technical appendix must describe both computations")
    return errors


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root: Path = ROOT, audit_root: Path | None = None) -> list[str]:
    errors: list[str] = []
    try:
        record = json.loads((root / RECORD).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"migration record unavailable: {exc}"]
    if record.get("schema_version") != 1:
        errors.append("Chapter 5 migration record must use schema_version 1")
    chapter = (root / "chapters/05-research-d.tex").read_text(encoding="utf-8")
    appendix = (root / "appendices/e-mti-technical.tex").read_text(encoding="utf-8")
    context = "\n".join(
        (root / relative).read_text(encoding="utf-8")
        for relative in (
            "frontmatter/abstract.tex",
            "frontmatter/acknowledgments.tex",
            "chapters/01-introduction.tex",
            "chapters/06-synthesis.tex",
        )
    )
    errors.extend(text_errors(chapter, appendix, context, record))
    for artifact in record.get("artifacts", []):
        path = root / artifact.get("path", "")
        if not path.is_file() or file_hash(path) != artifact.get("sha256"):
            errors.append(f"migration artifact hash mismatch: {artifact.get('path')}")
    if not record.get("artifacts"):
        errors.append("migration record lacks checked manuscript artifacts")
    for item in record.get("protected_history", []):
        path = root / item.get("path", "")
        if not path.is_file() or file_hash(path) != item.get("sha256"):
            errors.append(f"immutable historical control changed: {item.get('path')}")
    for source in record.get("source_artifacts", []):
        if not re.fullmatch(r"[0-9a-f]{40}", source.get("commit", "")):
            errors.append("migration source is not pinned to a full Git commit")
        if audit_root is not None:
            clone = audit_root / source.get("clone", "")
            result = subprocess.run(
                ["git", "-C", str(clone), "show", f"{source['commit']}:{source['path']}"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            if result.returncode or hashlib.sha256(result.stdout).hexdigest() != source.get("sha256"):
                errors.append(f"migration source blob mismatch: {source.get('source_id')}:{source.get('path')}")
    if not record.get("source_artifacts"):
        errors.append("migration record lacks immutable scientific source records")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit-root", type=Path)
    args = parser.parse_args()
    errors = validate(audit_root=args.audit_root)
    if errors:
        print("Chapter 5 ECM/Gibbs migration: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Chapter 5 ECM/Gibbs migration: PASS (source/prose controls; no new model fits)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
