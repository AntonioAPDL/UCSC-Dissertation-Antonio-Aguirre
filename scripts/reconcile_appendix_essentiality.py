#!/usr/bin/env python3.11
"""Reconcile one implemented appendix phase with the essentiality map."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from appendix_essentiality import appendix_unit_inventory
from validate_editorial_audit import current_display_labels
from validate_structure import active_tex_files, uncomment


ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "docs" / "appendix-essentiality-map.json"
APPENDIX_PATHS = {
    "A": "appendices/a-shared-conventions.tex",
    "B": "appendices/b-exdqlm-technical.tex",
    "C": "appendices/c-hydrology-technical.tex",
    "D": "appendices/d-qdesn-technical.tex",
    "E": "appendices/e-mti-technical.tex",
}


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def active_labels() -> set[str]:
    import re

    files, _ = active_tex_files()
    labels: set[str] = set()
    for path in files:
        labels.update(re.findall(r"\\label\{([^}]+)\}", uncomment(path.read_text(encoding="utf-8"))))
    return labels


def route(appendix: str, key: str) -> str:
    lower = key.lower()
    rules = {
        "A": [("", "app:shared-conventions")],
        "B": [("ldvb", "app:exdqlm-ldvb"), ("synthesis", "app:exdqlm-synthesis"), ("forecast", "app:exdqlm-synthesis"), ("posterior", "app:exdqlm-posterior")],
        "C": [("source-indexed-mcmc", "app:hydrology-mcmc"), ("laplace-delta", "app:hydrology-vb"), ("variational", "app:hydrology-vb"), ("source-specific", "env:app:sourceparams")],
        "D": [("glofas", "app:qdesn-glofas-support"), ("pricefm", "app:qdesn-pricefm-support"), ("gaussian", "app:qdesn-gaussian-baseline"), ("empirical", "app:qdesn-simulation-support"), ("simulation", "app:qdesn-simulation-support"), ("forecast", "app:qdesn-simulation-support"), ("computation", "app:qdesn-computation"), ("mcmc", "app:qdesn-computation"), ("variational", "app:qdesn-computation"), ("posterior", "app:qdesn-posterior"), ("model", "app:qdesn-posterior")],
        "E": [("extension", "app:mti-extensions"), ("dynamic", "app:mti-extensions"), ("application", "app:mti-application-sensitivity"), ("pharma", "app:mti-application-sensitivity"), ("calibration", "app:mti-calibration"), ("validation", "app:mti-calibration"), ("computation", "app:mti-profile-computation"), ("profile", "app:mti-profile-computation"), ("proof", "app:mti-proofs"), ("theory", "app:mti-proofs")],
    }
    for needle, label in rules[appendix]:
        if needle in lower:
            return label
    return f"app:{appendix.lower()}-technical"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--appendix", choices=sorted(APPENDIX_PATHS), required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--validation", required=True)
    args = parser.parse_args()

    payload = json.loads(MAP.read_text(encoding="utf-8"))
    paths = list(APPENDIX_PATHS.values())
    current_units = appendix_unit_inventory(ROOT, paths)
    labels = active_labels()
    displays = current_display_labels()
    appendix_records = [record for record in payload["records"] if record["appendix"] == args.appendix]
    baseline_units = set(payload["coverage"].get("baseline_unit_keys", []))

    for record in payload["records"]:
        record["coverage_keys"] = [
            key
            for key in record.get("coverage_keys", [])
            if key in baseline_units or key in current_units or key.startswith("display::")
        ]

    if args.appendix == "C":
        for record in appendix_records:
            if record.get("required_body_bridge") == "app:hydrology-parameters":
                record["required_body_bridge"] = "env:app:sourceparams"
                record["recovery"]["no_loss_location"] = "env:app:sourceparams"

    for record in appendix_records:
        if record["unit_type"] == "DISPLAY_FAMILY":
            active = any(ident in displays for ident in record.get("display_ids", []))
        elif record["unit_type"] in {"THEOREM_PROOF", "ALGORITHM", "EQUATION_GROUP"}:
            active = any(label in labels for label in record.get("labels", []))
        else:
            active = record.get("disposition") != "DEACTIVATE"
        record["current_inclusion"] = "ACTIVE" if active else "INACTIVE"
        record["status"] = "IMPLEMENTED"
        target = ROOT / record["target"]["path"]
        record["implementation"] = {
            "commit": args.commit,
            "final_sha256": file_sha256(target),
            "validation": args.validation,
        }

    covered = {key for record in payload["records"] for key in record.get("coverage_keys", [])}
    new_keys = sorted(
        key for key in current_units if key.startswith(f"{APPENDIX_PATHS[args.appendix]}::") and key not in covered
    )
    for key in new_keys:
        destination = route(args.appendix, key)
        candidates = [
            record
            for record in appendix_records
            if record["unit_type"] == "SECTION"
            and record["current_inclusion"] == "ACTIVE"
            and record.get("required_body_bridge") == destination
        ]
        if not candidates:
            candidates = [
                record
                for record in appendix_records
                if record["unit_type"] == "SECTION" and record["current_inclusion"] == "ACTIVE"
            ]
        if not candidates:
            raise SystemExit(f"no active section record can cover {key}")
        candidates[0]["coverage_keys"].append(key)

    pseudo_displays = {
        key
        for record in payload["records"]
        if record["unit_type"] == "DISPLAY_FAMILY" and record["current_inclusion"] == "ACTIVE"
        for key in record.get("coverage_keys", [])
        if key.startswith("display::")
    }
    payload["coverage"]["current_unit_keys"] = sorted(current_units | pseudo_displays)
    chapter_by_appendix = {
        "A": "chapters/01-introduction.tex",
        "B": "chapters/02-research-a.tex",
        "C": "chapters/03-research-b.tex",
        "D": "chapters/04-research-c.tex",
        "E": "chapters/05-research-d.tex",
    }
    for bridge in payload.get("body_bridge_inventory", []):
        if bridge["source_path"] == chapter_by_appendix[args.appendix]:
            bridge["status"] = "IMPLEMENTED"
            bridge["implementation_commit"] = args.commit
            bridge["final_location"] = bridge.get("target_label") or "body evidence at the former bridge location"

    MAP.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"reconciled Appendix {args.appendix}: {len(appendix_records)} records, {len(new_keys)} new unit keys")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
