#!/usr/bin/env python3.11
"""Validate the local, manuscript-first dissertation conversion.

The default checks require only the dissertation checkout.  Supplying the
temporary audit-clone root also verifies every recorded source hash against
the immutable Git blob at the manifest's commit.  No research code is run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_MANIFESTS = {
    "ch02-exdqlm": "docs/imports/ch02-exdqlm.json",
    "ch03-environ": "docs/imports/ch03-environ.json",
    "ch04-qdesn": "docs/imports/ch04-qdesn.json",
    "ch05-mti": "docs/imports/ch05-mti.json",
}
REVISION_LEDGER = PROJECT_ROOT / "docs" / "revision-ledger.json"
BASELINE_ID = "manuscript-first-20260915"
BASELINE_COMMIT = "79dbb9cc8348d9cc0ece2f23d5ade33570275055"
SOURCE_CLONES = {
    "SRC-EXDQLM-ARTICLE": "exdqlm-article",
    "SRC-ENVIRON": "environmetrics",
    "SRC-QDESN": "qdesn",
    "SRC-RQR": "rqr",
    "SRC-MTI-EXT": "mti-extensions",
}
CHAPTER_FILES = tuple(
    PROJECT_ROOT / path
    for path in (
        "chapters/02-research-a.tex",
        "chapters/03-research-b.tex",
        "chapters/04-research-c.tex",
        "chapters/05-research-d.tex",
    )
)
ALLOWED_DESTINATION_SUFFIXES = {".tex", ".pdf", ".png", ".jpg", ".jpeg"}
ALLOWED_MATERIAL_TYPES = {
    "manuscript_prose_and_equations",
    "display_tex_fragment",
    "figure_asset",
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob(repo: Path, commit: str, source_path: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(repo), "show", f"{commit}:{source_path}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace").strip())
    return result.stdout


def tex_files() -> list[Path]:
    files = list(CHAPTER_FILES)
    for directory in (PROJECT_ROOT / "tables", PROJECT_ROOT / "figures"):
        if directory.exists():
            files.extend(directory.rglob("*.tex"))
    return sorted(set(files))


def dependency_candidates(argument: str, graphics: bool) -> list[Path]:
    if argument.startswith("\\"):
        return []
    path = PROJECT_ROOT / argument
    if path.suffix:
        return [path]
    suffixes = (".pdf", ".png", ".jpg", ".jpeg", ".tex") if graphics else (".tex",)
    return [Path(f"{path}{suffix}") for suffix in suffixes]


def bibliography_keys(text: str) -> set[str]:
    return {
        match.group(1).strip().lower()
        for match in re.finditer(r"(?m)^@[A-Za-z]+\s*[({]\s*([^,\s]+)\s*,", text)
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--audit-root",
        type=Path,
        help="optional root containing the five immutable audit clones",
    )
    args = parser.parse_args()

    errors: list[str] = []
    manifests: list[dict[str, object]] = []
    item_count = 0
    document_count = 0
    section_count = 0
    source_check_count = 0
    baseline_destinations: dict[str, str] = {}

    try:
        revision_ledger = json.loads(REVISION_LEDGER.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        revision_ledger = {}
        errors.append(f"invalid revision ledger docs/revision-ledger.json: {exc}")
    if revision_ledger.get("schema_version") != 1:
        errors.append("docs/revision-ledger.json: unsupported schema_version")
    ledger_baseline = revision_ledger.get("baseline", {})
    if not isinstance(ledger_baseline, dict) or ledger_baseline.get("id") != BASELINE_ID:
        errors.append("docs/revision-ledger.json: baseline id is inconsistent")
    if ledger_baseline.get("integration_commit") != BASELINE_COMMIT:
        errors.append("docs/revision-ledger.json: integration commit is inconsistent")
    ledger_artifacts: dict[str, dict[str, object]] = {}
    for index, artifact in enumerate(revision_ledger.get("artifacts", [])):
        where = f"docs/revision-ledger.json:artifacts[{index}]"
        if not isinstance(artifact, dict) or not artifact.get("path"):
            errors.append(f"{where}: invalid artifact")
            continue
        artifact_path = str(artifact["path"])
        if artifact_path in ledger_artifacts:
            errors.append(f"{where}: duplicate artifact path {artifact_path}")
        ledger_artifacts[artifact_path] = artifact
        current_path = PROJECT_ROOT / artifact_path
        if not current_path.is_file():
            errors.append(f"{where}: missing artifact {artifact_path}")
            continue
        current_hash = digest(current_path.read_bytes())
        if current_hash != artifact.get("current_sha256"):
            errors.append(f"{where}: current hash does not match {artifact_path}")
        state = artifact.get("state")
        revision_ids = artifact.get("revision_ids")
        if state not in {"BASELINE_UNREVISED", "EDITED"}:
            errors.append(f"{where}: invalid state {state!r}")
        if not isinstance(revision_ids, list):
            errors.append(f"{where}: revision_ids must be an array")
        elif state == "EDITED" and not revision_ids:
            errors.append(f"{where}: edited artifact requires a revision ID")
        elif state == "BASELINE_UNREVISED" and revision_ids:
            errors.append(f"{where}: unrevised artifact cannot list revisions")
        if state == "BASELINE_UNREVISED" and current_hash != artifact.get("baseline_sha256"):
            errors.append(f"{where}: unrevised artifact differs from its baseline")

    revision_ids: set[str] = set()
    for index, revision in enumerate(revision_ledger.get("revisions", [])):
        where = f"docs/revision-ledger.json:revisions[{index}]"
        if not isinstance(revision, dict):
            errors.append(f"{where}: revision is not an object")
            continue
        revision_id = revision.get("id")
        if not isinstance(revision_id, str) or not revision_id.startswith("REV-"):
            errors.append(f"{where}: invalid revision id")
            continue
        if revision_id in revision_ids:
            errors.append(f"{where}: duplicate revision id {revision_id}")
        revision_ids.add(revision_id)
        for field in ("date", "paths", "summary", "evidence", "validation"):
            if not revision.get(field):
                errors.append(f"{where}: missing {field}")

    for expected_chapter, relative_path in EXPECTED_MANIFESTS.items():
        path = PROJECT_ROOT / relative_path
        if not path.is_file():
            errors.append(f"missing manifest: {relative_path}")
            continue
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"invalid manifest {relative_path}: {exc}")
            continue
        manifests.append(manifest)
        if manifest.get("schema_version") != 2:
            errors.append(f"{relative_path}: unsupported schema_version")
        if manifest.get("chapter") != expected_chapter:
            errors.append(f"{relative_path}: chapter does not match filename")
        baseline = manifest.get("baseline", {})
        if not isinstance(baseline, dict) or baseline.get("id") != BASELINE_ID:
            errors.append(f"{relative_path}: invalid baseline id")
        if baseline.get("integration_commit") != BASELINE_COMMIT:
            errors.append(f"{relative_path}: invalid integration commit")
        derivative = manifest.get("editorial_derivative", {})
        if not isinstance(derivative, dict) or derivative.get("revision_ledger") != "docs/revision-ledger.json":
            errors.append(f"{relative_path}: missing revision-ledger linkage")
        distribution = manifest.get("distribution", {})
        if not isinstance(distribution, dict) or distribution.get("rights_effect") != "NONE":
            errors.append(f"{relative_path}: distribution must be separated from rights")
        policy = manifest.get("policy", {})
        if not isinstance(policy, dict) or "unverified" not in str(policy.get("rights", "")):
            errors.append(f"{relative_path}: missing unverified-rights boundary")
        documents = manifest.get("documents", [])
        if not isinstance(documents, list) or not documents:
            errors.append(f"{relative_path}: no source-document dispositions")
        else:
            for doc_index, document in enumerate(documents):
                document_count += 1
                where = f"{relative_path}:documents[{doc_index}]"
                if not isinstance(document, dict):
                    errors.append(f"{where}: document is not an object")
                    continue
                dispositions = document.get("section_dispositions", [])
                if not isinstance(dispositions, list) or not dispositions:
                    errors.append(f"{where}: no section dispositions")
                else:
                    for disposition in dispositions:
                        section_count += 1
                        if not isinstance(disposition, dict):
                            errors.append(f"{where}: invalid section disposition")
                            continue
                        state = disposition.get("disposition")
                        if state not in {
                            "integrated",
                            "integrated_selected_subsections",
                            "omitted",
                        }:
                            errors.append(f"{where}: unresolved disposition {state!r}")
                        if state == "omitted" and not disposition.get("reason"):
                            errors.append(f"{where}: omitted section lacks a reason")
                        if (
                            state == "integrated_selected_subsections"
                            and not disposition.get("included_subsections")
                        ):
                            errors.append(f"{where}: partial section lacks subsection list")
                if document.get("rights_status") != "UNVERIFIED":
                    errors.append(f"{where}: rights status is not unverified")
        items = manifest.get("items", [])
        if not isinstance(items, list) or not items:
            errors.append(f"{relative_path}: no import items")
            continue

        for index, item in enumerate(items):
            item_count += 1
            where = f"{relative_path}:items[{index}]"
            if not isinstance(item, dict):
                errors.append(f"{where}: item is not an object")
                continue
            required = {
                "source_id",
                "commit",
                "source_path",
                "material_type",
                "destination",
                "source_sha256",
                "destination_sha256",
                "rights_status",
            }
            missing = sorted(required - item.keys())
            if missing:
                errors.append(f"{where}: missing {', '.join(missing)}")
                continue
            destination_string = str(item["destination"])
            destination_path = Path(destination_string)
            destination = PROJECT_ROOT / destination_path
            if destination_path.is_absolute() or ".." in destination_path.parts:
                errors.append(f"{where}: unsafe destination {destination_string!r}")
                continue
            if destination.suffix.lower() not in ALLOWED_DESTINATION_SUFFIXES:
                errors.append(f"{where}: forbidden destination type {destination.suffix}")
            if item["material_type"] not in ALLOWED_MATERIAL_TYPES:
                errors.append(f"{where}: unexpected material type {item['material_type']}")
            if item["rights_status"] != "UNVERIFIED":
                errors.append(f"{where}: rights status is not unverified")
            baseline_hash = str(item["destination_sha256"])
            previous_hash = baseline_destinations.setdefault(destination_string, baseline_hash)
            if previous_hash != baseline_hash:
                errors.append(f"{where}: inconsistent baseline hashes for {destination_string}")
            if not destination.is_file():
                errors.append(f"{where}: missing destination {destination_string}")
            else:
                current_hash = digest(destination.read_bytes())
                if current_hash != baseline_hash:
                    artifact = ledger_artifacts.get(destination_string)
                    if artifact is None:
                        errors.append(
                            f"{where}: edited destination lacks revision-ledger entry"
                        )
                    elif artifact.get("baseline_sha256") != baseline_hash:
                        errors.append(
                            f"{where}: revision-ledger baseline hash mismatch"
                        )
                    elif artifact.get("current_sha256") != current_hash:
                        errors.append(
                            f"{where}: revision-ledger current hash mismatch"
                        )
                    elif artifact.get("state") != "EDITED":
                        errors.append(
                            f"{where}: changed destination is not marked EDITED"
                        )

            if args.audit_root:
                source_id = str(item["source_id"])
                clone = SOURCE_CLONES.get(source_id)
                if clone is None:
                    errors.append(f"{where}: no clone mapping for {source_id}")
                    continue
                repo = args.audit_root / clone
                if not (repo / ".git").exists():
                    errors.append(f"{where}: audit clone missing: {clone}")
                    continue
                try:
                    data = git_blob(repo, str(item["commit"]), str(item["source_path"]))
                except RuntimeError as exc:
                    errors.append(f"{where}: source blob unavailable: {exc}")
                    continue
                source_check_count += 1
                if digest(data) != item["source_sha256"]:
                    errors.append(f"{where}: source Git-blob hash mismatch")

    files = tex_files()
    labels: list[str] = []
    cited: set[str] = set()
    forbidden_patterns = {
        "absolute server path": re.compile(r"/(?:data|home|tmp)/[A-Za-z0-9_.@/-]+"),
        "private key": re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
        "GitHub token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b"),
        "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    }
    for path in files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(PROJECT_ROOT)
        labels.extend(re.findall(r"\\label\{([^}]+)\}", text))
        for match in re.finditer(
            r"\\(?:cite|citep|citet|citealp|citeauthor|citeyear|citeyearpar|nocite)"
            r"(?:\[[^\]]*\])?(?:\[[^\]]*\])?\{([^}]+)\}",
            text,
        ):
            cited.update(key.strip().lower() for key in match.group(1).split(","))
        for command, argument in re.findall(
            r"\\(input|includegraphics)(?:\[[^\]]*\])?\{([^}]+)\}", text
        ):
            candidates = dependency_candidates(argument.strip(), command == "includegraphics")
            if candidates and not any(candidate.is_file() for candidate in candidates):
                errors.append(f"{relative}: missing dependency {argument}")
        for label, pattern in forbidden_patterns.items():
            if pattern.search(text):
                errors.append(f"{relative}: contains {label}")

    counts = Counter(labels)
    for label, count in sorted(counts.items()):
        if count > 1:
            errors.append(f"duplicate label {label!r} appears {count} times")

    bib_path = PROJECT_ROOT / "references.bib"
    keys = bibliography_keys(bib_path.read_text(encoding="utf-8"))
    missing_citations = sorted(cited - keys)
    if missing_citations:
        errors.append("missing bibliography keys: " + ", ".join(missing_citations))

    manifest_text = "\n".join(
        json.dumps(manifest, sort_keys=True) for manifest in manifests
    )
    for label, pattern in forbidden_patterns.items():
        if pattern.search(manifest_text):
            errors.append(f"import manifests contain {label}")

    for path, artifact in ledger_artifacts.items():
        for revision_id in artifact.get("revision_ids", []):
            if revision_id not in revision_ids:
                errors.append(f"{path}: unknown revision ID {revision_id}")

    if errors:
        print("Manuscript-import validation: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    source_note = (
        f"; {source_check_count} immutable source blobs rechecked"
        if args.audit_root
        else "; source-blob recheck skipped (no --audit-root)"
    )
    print(
        "Manuscript-import validation: PASS\n"
        f"- {len(manifests)} chapter manifests; {document_count} source documents; "
        f"{section_count} section dispositions\n"
        f"- {item_count} imported records{source_note}\n"
        f"- {len(files)} imported TeX files; {len(labels)} unique labels\n"
        f"- {len(cited)} cited keys; all present in references.bib\n"
        "- baseline provenance, editable-derivative ledger, dependency, rights, file-type, path, and secret checks passed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
