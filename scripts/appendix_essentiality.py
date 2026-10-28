#!/usr/bin/env python3.11
"""Shared validation helpers for the essential-appendix inclusion record."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


DISPOSITIONS = {"RETAIN", "CONDENSE", "SUMMARIZE", "DEACTIVATE"}
INCLUSION_STATES = {"ACTIVE", "INACTIVE"}
RECORD_STATES = {"PROPOSED", "APPROVED", "IMPLEMENTED", "VERIFIED"}
IMPLEMENTED_STATES = {"IMPLEMENTED", "VERIFIED"}
UNIT_TYPES = {
    "SECTION",
    "THEOREM_PROOF",
    "ALGORITHM",
    "EQUATION_GROUP",
    "DISPLAY_FAMILY",
}


def _slug(text: str) -> str:
    text = re.sub(r"\\[A-Za-z@]+\*?", " ", text)
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return text or "untitled"


def appendix_unit_inventory(root: Path, appendix_paths: list[str]) -> set[str]:
    """Inventory reader-facing appendix units that require a map disposition."""

    keys: set[str] = set()
    for relative in appendix_paths:
        path = root / relative
        text = path.read_text(encoding="utf-8")
        heading_counts: dict[str, int] = {}
        for line in text.splitlines():
            match = re.match(
                r"\\(section|subsection|subsubsection)\{(.+)\}\s*$", line.strip()
            )
            if match:
                base = f"{relative}::heading::{match.group(1)}::{_slug(match.group(2))}"
                heading_counts[base] = heading_counts.get(base, 0) + 1
                keys.add(f"{base}::occurrence::{heading_counts[base]}")
        for label in re.findall(r"\\label\{([^}]+)\}", text):
            if re.search(r"(?::eq:|:EQ:|:alg(?::|$)|:fig:|:tab:|:thm:|:prop:|:lem:|:cor:)", label):
                keys.add(f"{relative}::label::{label}")
    return keys


def load_optional(path: Path) -> dict:
    """Load an optional JSON record without changing legacy validation."""

    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def normalized_sha256(text: str) -> str:
    """Hash a source span after normalizing line endings and trailing space."""

    normalized = "\n".join(line.rstrip() for line in text.replace("\r\n", "\n").split("\n"))
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def implemented_inactive_records(payload: dict) -> list[dict]:
    return [
        record
        for record in payload.get("records", [])
        if record.get("status") in IMPLEMENTED_STATES
        and record.get("current_inclusion") == "INACTIVE"
    ]


def approved_inactive_display_ids(payload: dict) -> set[str]:
    """Return historical display IDs with an implemented inactive decision."""

    result: set[str] = set()
    for record in implemented_inactive_records(payload):
        recovery = record.get("recovery", {})
        if not recovery.get("source_path") or not recovery.get("git_commit"):
            continue
        if not recovery.get("no_loss_location"):
            continue
        result.update(str(value) for value in record.get("display_ids", []) if value)
    return result


def inactive_labels(payload: dict) -> set[str]:
    result: set[str] = set()
    for record in implemented_inactive_records(payload):
        result.update(str(value) for value in record.get("labels", []) if value)
    return result


def validate_payload(
    payload: dict,
    root: Path,
    *,
    active_labels: set[str] | None = None,
    body_references: set[str] | None = None,
    active_unit_keys: set[str] | None = None,
) -> list[str]:
    """Validate schema, recovery, coverage, and active-reference invariants."""

    errors: list[str] = []
    if payload.get("schema_version") != 1:
        errors.append("appendix essentiality map must use schema_version 1")
    if not payload.get("plan_id"):
        errors.append("appendix essentiality map is missing plan_id")
    approval = payload.get("approval")
    if not isinstance(approval, dict) or approval.get("status") != "APPROVED":
        errors.append("appendix essentiality map lacks an APPROVED approval record")
    for field in ("baseline", "links", "protected_conclusions", "records"):
        if not isinstance(payload.get(field), (dict if field in {"baseline", "links"} else list)):
            errors.append(f"appendix essentiality map has invalid {field}")

    protected = payload.get("protected_conclusions", [])
    protected_ids: set[str] = set()
    for index, item in enumerate(protected if isinstance(protected, list) else []):
        where = f"protected_conclusions[{index}]"
        ident = item.get("id")
        if not isinstance(ident, str) or not ident.startswith("APPX-CONC-"):
            errors.append(f"{where}: invalid id")
            continue
        if ident in protected_ids:
            errors.append(f"{where}: duplicate id {ident}")
        protected_ids.add(ident)
        if not item.get("statement"):
            errors.append(f"{where}: missing statement")
        if not item.get("final_locations"):
            errors.append(f"{where}: missing final_locations")

    record_ids: set[str] = set()
    target_keys: set[tuple[str, str]] = set()
    assigned_conclusions: set[str] = set()
    covered_units: set[str] = set()
    for index, record in enumerate(payload.get("records", [])):
        where = f"records[{index}]"
        ident = record.get("id")
        if not isinstance(ident, str) or not ident.startswith("APPX-ESS-"):
            errors.append(f"{where}: invalid id")
            continue
        if ident in record_ids:
            errors.append(f"{where}: duplicate id {ident}")
        record_ids.add(ident)
        for field in ("appendix", "chapter", "source_path", "anchor", "rationale", "risk", "reviewer"):
            if not record.get(field):
                errors.append(f"{where}: missing {field}")
        source_path = root / str(record.get("source_path", ""))
        if not source_path.is_file():
            errors.append(f"{where}: missing source_path")
        if record.get("unit_type") not in UNIT_TYPES:
            errors.append(f"{where}: invalid unit_type")
        if record.get("disposition") not in DISPOSITIONS:
            errors.append(f"{where}: invalid disposition")
        if record.get("current_inclusion") not in INCLUSION_STATES:
            errors.append(f"{where}: invalid current_inclusion")
        if record.get("status") not in RECORD_STATES:
            errors.append(f"{where}: invalid status")

        target = record.get("target", {})
        if not isinstance(target, dict) or not target.get("path"):
            errors.append(f"{where}: missing target path")
        else:
            target_label = str(target.get("label", ""))
            key = (str(target.get("path")), target_label)
            if target_label and key in target_keys:
                errors.append(f"{where}: duplicate target {key!r}")
            target_keys.add(key)

        recovery = record.get("recovery", {})
        if record.get("current_inclusion") == "INACTIVE":
            required = ("baseline_pdf_pages", "source_path", "git_commit", "no_loss_location")
            missing = [field for field in required if not recovery.get(field)] if isinstance(recovery, dict) else list(required)
            if missing:
                errors.append(f"{where}: inactive unit missing recovery fields {', '.join(missing)}")
        if record.get("disposition") == "DEACTIVATE" and not record.get("replacement_or_no_loss"):
            errors.append(f"{where}: DEACTIVATE unit lacks replacement_or_no_loss")

        conclusions = record.get("protected_conclusion_ids", [])
        if not isinstance(conclusions, list):
            errors.append(f"{where}: protected_conclusion_ids must be a list")
        else:
            unknown = set(conclusions) - protected_ids
            if unknown:
                errors.append(f"{where}: unknown protected conclusions {sorted(unknown)!r}")
            assigned_conclusions.update(conclusions)
        keys = record.get("coverage_keys", [])
        if not isinstance(keys, list) or not keys:
            errors.append(f"{where}: coverage_keys must be a nonempty list")
        else:
            for key in keys:
                if key in covered_units:
                    errors.append(f"{where}: duplicate coverage key {key}")
                covered_units.add(str(key))

        if record.get("status") in IMPLEMENTED_STATES:
            implementation = record.get("implementation", {})
            for field in ("commit", "final_sha256", "validation"):
                if not isinstance(implementation, dict) or not implementation.get(field):
                    errors.append(f"{where}: implemented unit missing implementation.{field}")
            final_path = root / str(target.get("path", "")) if isinstance(target, dict) else None
            if final_path and final_path.is_file() and isinstance(implementation, dict):
                expected = implementation.get("final_sha256")
                actual = hashlib.sha256(final_path.read_bytes()).hexdigest()
                if expected and expected != actual:
                    errors.append(f"{where}: final_sha256 does not match {target.get('path')}")

    missing_conclusions = protected_ids - assigned_conclusions
    if missing_conclusions:
        errors.append("protected conclusions lack a responsible record: " + ", ".join(sorted(missing_conclusions)))
    if active_unit_keys is not None:
        coverage = payload.get("coverage", {})
        baseline_units = set(coverage.get("baseline_unit_keys", [])) if isinstance(coverage, dict) else set()
        missing_units = active_unit_keys - covered_units
        extra_units = covered_units - active_unit_keys - baseline_units
        if missing_units:
            errors.append("active appendix units missing from map: " + ", ".join(sorted(missing_units)))
        if extra_units:
            errors.append("map coverage keys not active: " + ", ".join(sorted(extra_units)))
    if body_references is not None:
        bad = body_references & inactive_labels(payload)
        if bad:
            errors.append("body references inactive appendix labels: " + ", ".join(sorted(bad)))
    if active_labels is not None:
        unexpectedly_active = active_labels & inactive_labels(payload)
        if unexpectedly_active:
            errors.append("inactive labels remain active: " + ", ".join(sorted(unexpectedly_active)))
    return errors
