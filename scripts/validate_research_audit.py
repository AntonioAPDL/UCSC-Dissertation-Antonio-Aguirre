#!/usr/bin/env python3
"""Validate the dissertation research-audit records without external packages."""

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Set


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "source-manifest.json"
CLAIMS = ROOT / "docs" / "claim-evidence.json"
LOCAL_MANIFEST = ROOT / "source-manifest.local.json"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
ABSOLUTE_PRIVATE_PATH = re.compile(r"(?<![A-Za-z0-9])/(?:data|home)/")
FORBIDDEN_PUBLIC_TERMS = ("password=", "token=", "authorization: bearer")
SOURCE_STATUSES = {
    "PENDING_AUTHOR_VERSION_DECISION",
    "SUPPORTING_SOURCE",
    "AUTHOR_CONFIRMED",
    "EXCLUDED",
}
RIGHTS_STATUSES = {
    "UNVERIFIED",
    "SOFTWARE_LICENSE_PRESENT",
    "APPROVED",
    "RESTRICTED",
    "NOT_APPLICABLE",
}
EVIDENCE_LEVELS = {"E0", "E1", "E2", "E3", "E4"}
RUN_RESULTS = {"PASS", "ISSUE_FOUND", "NOT_RUN", "BLOCKED"}


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing required file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition, message):
    if not condition:
        fail(message)


def validate_manifest(data):
    require(data.get("schema_version") == 2, "source manifest schema_version must be 2")
    require(data.get("status") == "AUDIT_COMPLETE_WITH_AUTHOR_DECISIONS_PENDING",
            "source manifest completion status is inconsistent")
    sources = data.get("sources")
    require(isinstance(sources, list) and sources, "source manifest must contain sources")
    ids = set()  # type: Set[str]
    document_ids = set()  # type: Set[str]
    snapshot_ids = set()  # type: Set[str]
    commits = {}  # type: Dict[str, Set[str]]
    audit_commits = {}  # type: Dict[str, str]
    snapshot_lookup = {}
    for source in sources:
        sid = source.get("id")
        require(isinstance(sid, str) and sid.startswith("SRC-"), "invalid source id")
        require(sid not in ids, f"duplicate source id: {sid}")
        ids.add(sid)
        audit_commits[sid] = str(source.get("audit_commit", ""))
        commits[sid] = {audit_commits[sid]}
        for field in ("discovery_commit", "audit_commit"):
            require(bool(HEX40.fullmatch(str(source.get(field, "")))), f"{sid}: invalid {field}")
        require(source.get("highest_bounded_evidence") in EVIDENCE_LEVELS,
                f"{sid}: invalid highest_bounded_evidence")
        require(source.get("inclusion_status") in SOURCE_STATUSES, f"{sid}: invalid inclusion status")
        require(source.get("rights_status") in RIGHTS_STATUSES, f"{sid}: invalid rights status")
        require(isinstance(source.get("imports"), list), f"{sid}: imports must be an array")
        documents = source.get("documents")
        require(isinstance(documents, list) and documents, f"{sid}: documents must be a nonempty array")
        for document in documents:
            did = document.get("id")
            require(isinstance(did, str) and did.startswith("DOC-"), f"{sid}: invalid document id")
            require(did not in document_ids, f"duplicate document id: {did}")
            document_ids.add(did)
            require(bool(document.get("path")), f"{did}: path is required")
        for snapshot in source.get("related_snapshots", []):
            snap_id = snapshot.get("id")
            snap_commit = str(snapshot.get("commit", ""))
            require(isinstance(snap_id, str) and snap_id.startswith("SNAP-"),
                    f"{sid}: invalid related snapshot id")
            require(snap_id not in snapshot_ids, f"duplicate related snapshot id: {snap_id}")
            snapshot_ids.add(snap_id)
            require(bool(HEX40.fullmatch(snap_commit)), f"{snap_id}: invalid commit")
            commits[sid].add(snap_commit)
            snapshot_lookup[snap_id] = (sid, snap_commit)

    run_ids = set()  # type: Set[str]
    runs = data.get("validation_runs")
    require(isinstance(runs, list) and runs, "validation_runs must be a nonempty array")
    for run in runs:
        rid = run.get("id")
        require(isinstance(rid, str) and rid.startswith("RUN-"), f"invalid run id: {rid}")
        require(rid not in run_ids, f"duplicate run id: {rid}")
        run_ids.add(rid)
        require(run.get("source_id") in ids, f"{rid}: unknown source_id")
        require(run.get("result") in RUN_RESULTS, f"{rid}: invalid result")
        require(run.get("evidence_level") in EVIDENCE_LEVELS, f"{rid}: invalid evidence level")
        require(bool(run.get("summary")), f"{rid}: summary is required")
    return ids, commits, audit_commits, snapshot_lookup


def validate_claims(data, source_ids, source_commits, audit_commits, snapshot_lookup):
    require(data.get("schema_version") == 2, "claim evidence schema_version must be 2")
    records = data.get("records")
    require(isinstance(records, list), "claim evidence records must be an array")
    ids = set()  # type: Set[str]
    for record in records:
        cid = record.get("id")
        require(isinstance(cid, str) and cid.startswith(("CLM-", "ART-", "CON-")), f"invalid evidence id: {cid}")
        require(cid not in ids, f"duplicate evidence id: {cid}")
        ids.add(cid)
        require(record.get("source_id") in source_ids, f"{cid}: unknown source_id")
        require(bool(HEX40.fullmatch(str(record.get("commit", "")))), f"{cid}: invalid commit")
        require(record.get("commit") in source_commits[record.get("source_id")],
                f"{cid}: commit is not an audited or declared related snapshot")
        snapshot_id = record.get("snapshot_id")
        if snapshot_id:
            require(snapshot_lookup.get(snapshot_id) ==
                    (record.get("source_id"), record.get("commit")),
                    f"{cid}: snapshot_id does not identify its source and commit")
        else:
            require(record.get("commit") == audit_commits[record.get("source_id")],
                    f"{cid}: a related-snapshot claim requires snapshot_id")
        level = record.get("evidence_level")
        require(level in EVIDENCE_LEVELS, f"{cid}: invalid evidence level")
        wording = str(record.get("verification_status", "")).lower()
        if "reproduced" in wording:
            require(level == "E4", f"{cid}: 'reproduced' requires E4")
        require(bool(record.get("source_path")), f"{cid}: source_path is required")
        require(bool(record.get("locator")), f"{cid}: locator is required")


def validate_public_boundary():
    public_files = [
        MANIFEST,
        CLAIMS,
        ROOT / "docs" / "research-audit.md",
        ROOT / "docs" / "chapter-plan.md",
        ROOT / "docs" / "research-audit-validation.md",
        ROOT / "docs" / "research-decisions.md",
    ]
    for path in public_files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        require(not ABSOLUTE_PRIVATE_PATH.search(text), f"absolute server path in {path.relative_to(ROOT)}")
        lowered = text.lower()
        for term in FORBIDDEN_PUBLIC_TERMS:
            require(term not in lowered, f"credential-like term in {path.relative_to(ROOT)}")


def validate_ignored_local_records():
    if not LOCAL_MANIFEST.exists():
        return
    result = subprocess.run(
        ["git", "check-ignore", "-q", str(LOCAL_MANIFEST.relative_to(ROOT))],
        cwd=ROOT,
        check=False,
    )
    require(result.returncode == 0, "source-manifest.local.json must remain ignored")


def main():
    manifest = load_json(MANIFEST)
    claims = load_json(CLAIMS)
    source_ids, source_commits, audit_commits, snapshot_lookup = validate_manifest(manifest)
    validate_claims(claims, source_ids, source_commits, audit_commits, snapshot_lookup)
    validate_public_boundary()
    validate_ignored_local_records()
    print(f"research audit validation passed: {len(source_ids)} sources, {len(claims['records'])} evidence records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
