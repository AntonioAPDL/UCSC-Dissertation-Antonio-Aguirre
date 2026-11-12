#!/usr/bin/env python3.11
"""Reconcile only the author-approved Chapter 5 ECM/Gibbs source migration.

This mechanical record update never edits manuscript prose or scientific
assets. It preserves original import hashes and historical advisor receipts.
Audit-clone paths are command-line inputs and never enter public records.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

from appendix_essentiality import appendix_unit_inventory


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-11-11"
REVISION = "REV-CH05-MTI-ECM-GIBBS-20261111"
RECORD = "docs/ch05-mti-ecm-gibbs-migration-20261111.json"
RQR = "cab844d0695fe13fa3f610615d282972112eba51"
OLD_RQR = "4223c6a3a44f376255bacdca91db71cdf4f3afde"
OLD_EXT = "f345d946aa5a81b94795838bec58d874a0fdd0c9"
BASELINE = "3f264eaf4fa9b398753945fc3cb20f70178e383d"
CHAPTER = "chapters/05-research-d.tex"
APPENDIX = "appendices/e-mti-technical.tex"
ROOT_PATHS = [
    "frontmatter/abstract.tex", "frontmatter/acknowledgments.tex",
    "chapters/01-introduction.tex", CHAPTER, "chapters/06-synthesis.tex", APPENDIX,
]
ASSETS = [
    "figures/ch05-mti/generated/fig04_tolerance_validation_primary.png",
    "figures/ch05-mti/generated/fig05_tolerance_validation_width_ranges.png",
    "figures/ch05-mti/generated/fig06_pharma_application_tensile_intervals.png",
    "tables/ch05-mti/tolerance_validation_article_scenario_ranges.tex",
    "tables/ch05-mti/pharma_application_primary_summary.tex",
    "tables/ch05-mti/pharma_application_numbers.tex",
    "tables/ch05-mti/pharma_source_numbers.tex",
    "tables/ch05-mti/tolerance_validation_mti_profile_policy.tex",
]
DERIVATIVE_GENERATOR = "scripts/generate_ch05_mti_ecm_figures.R"
DERIVATIVE_INPUTS = [
    ("tables/ch05-mti/ecm_family_case_summary_20261111.csv",
     "figures/data/mti_ecm_validation_20261111/family_case_summary.csv"),
    ("tables/ch05-mti/ecm_population_width_reference_20261111.csv",
     "figures/data/tolerance_population_shortest_content_oracle.csv"),
]
HISTORY = [
    "docs/bruno-revision-response-matrix-20261109.json",
    "docs/bruno-revision-preedit-baseline-20261109.json",
    "docs/author-comments-preedit-baseline-20261110.json",
    "docs/source-refresh-20261026.json",
    "docs/source-refresh-20261106.json",
]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_hash(relative: str) -> str:
    return digest((ROOT / relative).read_bytes())


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def git_blob(repo: Path, commit: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(repo), "show", f"{commit}:{path}"],
        check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout


def source_record(repo: Path, source: str, clone: str, commit: str, path: str) -> dict:
    return {"source_id": source, "clone": clone, "commit": commit,
            "path": path, "sha256": digest(git_blob(repo, commit, path))}


def snapshot(source: dict, ident: str, commit: str, role: str) -> None:
    if not any(item.get("id") == ident for item in source.setdefault("related_snapshots", [])):
        source["related_snapshots"].append({"id": ident, "ref": "prior dissertation authority",
                                            "commit": commit, "role": role})


def claim(ident: str, classification: str, text: str, path: str, locator: str,
          qualification: str, disposition: str = "current Chapter 5 evidence") -> dict:
    return {"id": ident, "classification": classification, "claim": text,
            "source_id": "SRC-RQR", "commit": RQR, "source_path": path,
            "locator": locator, "evidence_level": "E2",
            "verification_status": "frozen source statements and public tabular evidence inspected",
            "qualification": qualification, "dissertation_disposition": disposition}


def reconcile(args: argparse.Namespace) -> dict[str, dict]:
    artifacts = [{"path": path, "sha256": file_hash(path)} for path in
                 ROOT_PATHS + ASSETS + [DERIVATIVE_GENERATOR] + [item[0] for item in DERIVATIVE_INPUTS]]
    sources = [source_record(args.rqr, "SRC-RQR", "rqr", RQR, path) for path in (
        "main.tex", "rqr-gibbs-supplement.tex",
        "figures/data/mti_ecm_validation_20261111/provenance.json",
        "figures/data/mti_ecm_validation_20261111/family_case_summary.csv",
        "figures/data/mti_ecm_validation_20261111/paired_comparisons.csv",
        "figures/data/mti_ecm_validation_20261111/ecm_diagnostics.csv",
        "figures/data/pharma_mti_application_20261020/manifest.json",
        "figures/data/pharma_source_structure_ecm_20261111/manifest.json",
        "figures/data/tolerance_population_shortest_content_oracle.csv",
    )] + [source_record(args.extensions, "SRC-MTI-EXT", "mti-extensions", args.extensions_commit, path)
          for path in ("main.tex", "mti-extensions-supplement.tex")]
    protected = [{"path": path, "sha256": digest(git_blob(ROOT, BASELINE, path))}
                 for path in HISTORY]
    protected.append({"path": "figures/ch05-mti/generated/fig01_three_balance_principles.png",
                      "sha256": digest(git_blob(ROOT, BASELINE, "figures/ch05-mti/generated/fig01_three_balance_principles.png"))})
    record = {
        "schema_version": 1, "date": DATE, "baseline_commit": BASELINE,
        "status": "IMPLEMENTED_PENDING_RELEASE_VALIDATION",
        "authorization": "Author-directed Chapter 5 ECM/Gibbs migration and verified extension tilt-sign correction",
        "gibbs_empirical_status": "NOT_REPORTED",
        "gibbs_boundary": "Conditionals and algorithms are included; no completed Gibbs comparison or measured ECM/Gibbs speed ratio is asserted.",
        "scope": "Chapter 5, Appendix E, connected dissertation prose, eight result assets, and their source/validation records only",
        "supersedes": [
            {"record": "docs/final-voice-exdqlm-mti-response-matrix-20261110.json",
             "item": "MTI-001", "scope": "Retires the computational convex-profile proposition; retains the three population identification results and their proof arguments."},
            {"record": "docs/current-source-refresh-audit.md",
             "scope": "Replaces the active profiled-MTI results with the authentic finite-iteration MTI-ECM packet; historical audit is preserved."},
        ],
        "response_items": [
            {"id": "CH05-MIG-001", "request": "Replace the production convex-profile account with MTI-ECM and Gibbs computation.",
             "resolution": "Chapter 5 and Appendix E state the fixed-target generalized posterior, augmentation, Gaussian/GIG updates and distinct mode/sampling roles.",
             "targets": [CHAPTER, APPENDIX], "status": "IMPLEMENTED_PENDING_RELEASE_VALIDATION"},
            {"id": "CH05-MIG-002", "request": "Retain the essential MPI/MTI theory without obsolete algorithmic material.",
             "resolution": "Retain three population identification results and their profile-risk proofs; retire the computational convex-profile proposition.",
             "targets": [CHAPTER, APPENDIX, "scripts/validate_final_voice_style.py"], "status": "IMPLEMENTED_PENDING_RELEASE_VALIDATION"},
            {"id": "CH05-MIG-003", "request": "Explain tolerance construction and width/tilt selection.",
             "resolution": "Describe candidate content and tilt search, fixed-target ECM endpoints, direct DP content probability, separately calibrated cutoff, and independent validation.",
             "targets": [CHAPTER, APPENDIX], "status": "IMPLEMENTED_PENDING_RELEASE_VALIDATION"},
            {"id": "CH05-MIG-004", "request": "Replace figures and tables coherently with authenticated results.",
             "resolution": "Replace eight result assets as one ECM packet; preserve author-selected Figure 5.1 and the population placement map.",
             "targets": ASSETS, "status": "IMPLEMENTED_PENDING_RELEASE_VALIDATION"},
            {"id": "CH05-MIG-005", "request": "Provide an ECM/Gibbs comparison without treating expectations as observed findings.",
             "resolution": "Include both algorithms and their estimands but no unexecuted Gibbs numerical values, equality claim, or measured speed ratio.",
             "targets": [CHAPTER, APPENDIX, "scripts/validate_mti_migration.py"], "status": "IMPLEMENTED_PENDING_RELEASE_VALIDATION"},
            {"id": "CH05-MIG-006", "request": "Reconcile fixed-tilt signs and related extension theory.",
             "resolution": "Pin the corrected extension manuscript and preserve the negative retained-mean tilt in the loss and positive Gaussian canonical shift.",
             "targets": [CHAPTER, APPENDIX, "source-manifest.json"], "status": "IMPLEMENTED_PENDING_RELEASE_VALIDATION"},
            {"id": "CH05-MIG-007", "request": "Use the author's concise statistical style throughout the dissertation references.",
             "resolution": "Revise only the connected abstract, acknowledgments, introduction and synthesis with verified ECM findings and accurate contribution boundaries.",
             "targets": ROOT_PATHS, "status": "IMPLEMENTED_PENDING_RELEASE_VALIDATION"},
            {"id": "CH05-MIG-008", "request": "Preserve provenance and require a clean source-verified release.",
             "resolution": "Retain original baseline hashes and immutable advisor receipts; add current source/asset hashes, migration controls, and source-aware regression tests.",
             "targets": [RECORD, "docs/imports/ch05-mti.json", "docs/revision-ledger.json", "scripts/validate.sh"],
             "status": "IMPLEMENTED_PENDING_RELEASE_VALIDATION"},
        ],
        "artifacts": artifacts, "source_artifacts": sources, "protected_history": protected,
        "validation": {"source_and_asset_checks": "frozen source hashes recorded",
                       "release_build": "PENDING", "remote_publication": "NOT_PERFORMED"},
    }

    manifest = load("source-manifest.json")
    manifest["recorded_at"] = DATE
    manifest["status"] = "LOCAL_MANUSCRIPT_CONVERSION_COMPLETE_PENDING_SCIENTIFIC_AND_REUSE_REVIEW"
    manifest["lifecycle"].update({"scientific_review": "IN_PROGRESS", "github_sync": "NOT_SYNCED",
        "state_note": "The author-directed Chapter 5 ECM/Gibbs migration is implemented locally against immutable MTI sources. Its new release, merge, push, and Overleaf readback remain separate gates. Historical advisor/release records, other research chapters, and reuse/accessibility boundaries are preserved."})
    manifest["execution_record"]["ch05_mti_ecm_gibbs_migration"] = {
        "record": RECORD, "state": "IMPLEMENTED_PENDING_RELEASE_VALIDATION",
        "baseline_commit": BASELINE, "new_model_fits": 0,
        "rqr_source_commit": RQR, "extension_source_commit": args.extensions_commit,
    }
    by_id = {source["id"]: source for source in manifest["sources"]}
    rqr, ext = by_id["SRC-RQR"], by_id["SRC-MTI-EXT"]
    snapshot(rqr, "SNAP-RQR-PROFILED-20261026", OLD_RQR,
             "Historical profiled-MTI source superseded for active Chapter 5 computation and results")
    snapshot(ext, "SNAP-MTI-EXT-PRE-TILT-CORRECTION-20261111", OLD_EXT,
             "Original extension manuscript before the verified midpoint tilt-sign correction")
    for source, repo, commit, previous, description in (
        (rqr, args.rqr, RQR, OLD_RQR, "Frozen MTI-ECM article, supplement, public result summaries and provenance; no new research fits"),
        (ext, args.extensions, args.extensions_commit, OLD_EXT, "Corrected midpoint tilt-sign extension source; finite-dimensional Gibbs/ECM and proposed dynamic endpoint derivations"),
    ):
        source["audit_commit"] = commit
        source["discovery_commit"] = commit
        source["audit_scope"] = description
        inventory = source.get("inventory", {})
        historical = inventory.get("historical_discovery", {
            "commit": previous, "inventory": inventory,
            "meaning": "Earlier discovery inventory; not attributed to the new frozen source commit",
        })
        tree = subprocess.run(["git", "-C", str(repo), "ls-tree", "-r", "--name-only", commit],
                              check=True, stdout=subprocess.PIPE).stdout
        source["inventory"] = {"tracked_files": len(tree.splitlines()), "tracked_commit": commit,
            "remote_heads": 60 if source["id"] == "SRC-RQR" else 2,
            "remote_heads_checked_at": DATE,
            "remote_heads_verification": "Command-line Git ls-remote --heads against the canonical public repository; other remote inventory remains historical",
            "historical_discovery": historical}
        source["imports"][0].update({"status": "IMPLEMENTED_PENDING_RELEASE_VALIDATION",
                                      "scope": description, "refresh": RECORD})
    manifest["validation_runs"] = [item for item in manifest["validation_runs"]
                                    if item["id"] != "RUN-MTI-20261111-SOURCE-RECONCILIATION"] + [{
        "id": "RUN-MTI-20261111-SOURCE-RECONCILIATION", "source_id": "SRC-RQR",
        "result": "PASS", "evidence_level": "E2",
        "summary": "Frozen source and result-asset provenance inspected; no new ECM fit or Gibbs campaign was performed for the dissertation migration.",
    }]

    imports = load("docs/imports/ch05-mti.json")
    imports["editorial_derivative"]["status"] = "IMPLEMENTED_PENDING_RELEASE_VALIDATION"
    imports["distribution"].update({"github": "PENDING_CURRENT_REVISION", "overleaf": "NOT_PERFORMED_CURRENT_REVISION"})
    projection = {"source_id": "SRC-RQR", "commit": RQR,
                  "status": "IMPLEMENTED_SOURCE_VERIFIED", "migration_record": RECORD,
                  "documents": [], "projected_items": []}
    for path in ("main.tex", "rqr-gibbs-supplement.tex"):
        projection["documents"].append({"source_path": path, "source_sha256": digest(git_blob(args.rqr, RQR, path))})
    for destination, source_path in DERIVATIVE_INPUTS:
        source_hash = digest(git_blob(args.rqr, RQR, source_path))
        if source_hash != file_hash(destination):
            raise ValueError(f"frozen derivative input differs from source: {destination}")
        projection["documents"].append({"source_path": source_path,
            "source_sha256": source_hash, "local_reproduction_input": destination,
            "local_input_sha256": file_hash(destination)})
    for destination in ASSETS:
        source_path = destination.replace("figures/ch05-mti/", "figures/").replace("tables/ch05-mti/", "tables/")
        if source_path.endswith("tolerance_validation_mti_profile_policy.tex"):
            source_path = "tables/tolerance_validation_mti_ecm_selected_policy_summary.tex"
        projected = {"source_path": source_path,
            "source_sha256": digest(git_blob(args.rqr, RQR, source_path)),
            "destination": destination, "destination_sha256": file_hash(destination),
            "handling": "Frozen source copied; the ECM policy table preserves the dissertation cross-reference label."}
        if Path(destination).name in {"fig04_tolerance_validation_primary.png", "fig05_tolerance_validation_width_ranges.png"}:
            projected["handling"] = "Editorial presentation derivative of frozen source summaries; scientific numbers and comparisons are unchanged, but image bytes and layout differ from the original source figure."
            projected["derivation"] = {"generator": DERIVATIVE_GENERATOR,
                "generator_sha256": file_hash(DERIVATIVE_GENERATOR),
                "frozen_input_paths": [item[0] for item in DERIVATIVE_INPUTS],
                "model_refits": 0}
        projection["projected_items"].append(projected)
    imports["current_projection"] = projection

    claims = load("docs/claim-evidence.json")
    claims["recorded_at"] = DATE
    for item in claims["records"]:
        if item.get("source_id") == "SRC-RQR" and item.get("commit") == OLD_RQR:
            if item["id"] in {"CLM-RQR-001", "CLM-RQR-002"}:
                item["commit"] = RQR
                item["verification_status"] = "population statement and supporting proof retained in the frozen ECM article"
            else:
                item["snapshot_id"] = "SNAP-RQR-PROFILED-20261026"
                item["dissertation_disposition"] = "historical source provenance; not the active Chapter 5 ECM results"
        if item.get("source_id") == "SRC-MTI-EXT" and item.get("commit") in {OLD_EXT, args.extensions_commit}:
            item["commit"] = args.extensions_commit
            item["verification_status"] = "corrected source checked; midpoint and root losses agree in tilt sign"
            if item["id"] == "CON-MTI-003":
                item["claim"] = "The corrected MTI extensions source includes manuscript algebra regression tests but no fitted static/dynamic application evidence or numerical validation campaign."
                item["locator"] = "manuscript, README, and scoped tilt-sign regression-test inventory"
                item["qualification"] = "Algebra regression tests verify the corrected tilt convention; they do not establish application performance or tolerance validity for the proposed extensions."
    new_claims = [
        claim("CLM-MTI-ECM-001", "numerical_implementation_claim",
              "MPI and fixed-tilt MTI under proper Gaussian root priors admit Gaussian root and GIG latent-scale full conditionals; finite-iteration ECM uses the same augmentation to estimate a mode.",
              "main.tex", "Empirical Balance and Fixed-Target Computation",
              "Conditional conjugacy is not a jointly Gaussian posterior; the residual-floor and finite-iteration ECM calculation is not a global mode certificate."),
        claim("ART-MTI-ECM-001", "empirical_result",
              "The frozen ECM validation has smaller mean width than Young--Mathew in 39 of 72 distribution-setting cells; tolerance attainment and width are assessed jointly.",
              "figures/data/mti_ecm_validation_20261111/paired_comparisons.csv", "72 paired family-setting comparisons",
              "Finite-iteration ECM results replace the older convex-profile packet; no new fit was performed for this migration."),
        claim("CON-MTI-ECM-001", "empirical_result",
              "Simultaneous validation intervals have lower bounds above 0.95 in 53 MTI-ECM distribution-setting cases and include 0.95 in the other 19 cases.",
              "figures/data/mti_ecm_validation_20261111/family_case_summary.csv", "MTI-ECM simultaneous_lower and simultaneous_upper columns",
              "These are validation-attainment statements, not convergence classifications. Separately, 42116 ECM fits meet the frozen stopping threshold and 29884 reach the iteration cap; neither establishes a distribution-free tolerance guarantee."),
        claim("CON-MTI-GIBBS-001", "definition_or_setup",
              "Gibbs algorithms and their fixed-target posterior interpretation are included, but completed Gibbs/ECM empirical agreement and measured speed comparisons are not reported.",
              "tables/mti_gibbs_comparison_main.tex", "source comparison placeholder boundary",
              "No placeholder Gibbs values are imported into the dissertation.", "explicit empirical evidence boundary"),
        claim("ART-MTI-PHARMA-001", "empirical_result",
              "The frozen pharmaceutical MTI-ECM analysis uses 187 product-23 batches and 1000 paired 100/87 random splits; tensile width and stationarity findings are not uniformly favorable.",
              "figures/data/pharma_mti_application_20261020/manifest.json", "frozen MTI-ECM pharmaceutical application",
              "Partitions reuse the finite historical dataset; endpoints, empirical content, iteration caps, and width must be read together."),
    ]
    new_ids = {item["id"] for item in new_claims}
    claims["records"] = [item for item in claims["records"] if item["id"] not in new_ids] + new_claims

    revision = load("docs/revision-ledger.json")
    revision["recorded_at"] = DATE
    changed = {item["path"] for item in artifacts}
    for artifact in revision["artifacts"]:
        if artifact["path"] in changed:
            artifact["current_sha256"] = file_hash(artifact["path"])
            artifact["state"] = "EDITED"
            if REVISION not in artifact["revision_ids"]:
                artifact["revision_ids"].append(REVISION)
    existing_paths = {item["path"] for item in revision["artifacts"]}
    for path in sorted(changed - existing_paths):
        revision["artifacts"].append({"path": path, "baseline_sha256": None,
            "current_sha256": file_hash(path), "state": "DERIVED_NEW", "revision_ids": [REVISION]})
    revision["revisions"] = [item for item in revision["revisions"] if item["id"] != REVISION] + [{
        "id": REVISION, "date": DATE, "paths": sorted(changed),
        "summary": "Migrates Chapter 5 and Appendix E to authenticated finite-iteration MTI-ECM results and the conditionally conjugate Gibbs/ECM derivation; preserves population theory, selected Figure 5.1, immutable history, and the unreported Gibbs comparison boundary.",
        "evidence": RECORD,
        "validation": "Source/asset hashes and migration regression tests; clean build and rendered release inspection remain separate recorded gates.",
    }]

    migration = load("docs/appendix-migration-map.json")
    for item in migration["records"]:
        if item["id"] in {"MIG-CH05-CURRENT-RQR", "MIG-CH05-CURRENT-MTI-EXT"}:
            ext_source = item["id"].endswith("MTI-EXT")
            item["source_unit_sha256"] = next(source["sha256"] for source in sources
                if source["source_id"] == ("SRC-MTI-EXT" if ext_source else "SRC-RQR")
                and source["path"] == ("mti-extensions-supplement.tex" if ext_source else "rqr-gibbs-supplement.tex"))
            item["source_heading"] = "Corrected MTI endpoint extensions" if ext_source else "MTI population proofs, augmented Gibbs/ECM computation, and calibration"
            item["semantic_class"] = "generalized-Bayes derivations and preserved population proofs"
            item["source_file_sha256_after"] = file_hash(CHAPTER)
            item["destination_file_sha256_after"] = file_hash(APPENDIX)

    displays = load("docs/display-ledger.json")
    displays["recorded_at"] = DATE
    for item in displays["records"]:
        if item.get("chapter") == "ch05-mti" and item["disposition"] == "KEEP":
            if "tolerance-validation" in item["id"] or "pharma-application" in item["id"] or "profile-policy" in item["id"]:
                item["claim_role"] = "Frozen MTI-ECM result or policy; not the superseded convex-profile packet"
                item["rationale"] = "Retains the same dissertation display role with authenticated finite-iteration ECM inputs, including adverse findings and numerical stopping qualifications."
                item["status"] = "CH05_ECM_SOURCE_MIGRATION"

    accessibility = load("docs/accessibility-ledger.json")
    accessibility["recorded_at"] = DATE
    for item in accessibility["graphics"]:
        if item.get("figure_label") == "rqr2026:fig:tolerance-validation-primary":
            item["alt_text"] = "One horizontal panel groups nine sample-size and required-content settings. Green, pink and black segments show the range of content-attainment rates across eight distributions for MTI-ECM, Young--Mathew and Wilks. A vertical reference marks nominal tolerance confidence 0.95. The segments are across-distribution ranges, not uncertainty intervals. The accompanying text reports 53 simultaneous validation intervals wholly above 0.95 and 19 including 0.95."
        elif item.get("figure_label") == "rqr2026:fig:tolerance-validation-width-ranges":
            item["alt_text"] = "Nine design panels arranged in three rows compare mean widths and empirical 2.5--97.5 percent width ranges for frozen MTI-ECM, Young--Mathew and Wilks across eight distributions. A shared left column gives the distribution names. Each panel uses a logarithmic width axis and population shortest-contiguous reference markers. MTI-ECM is narrower than Young--Mathew in 39 of 72 distribution-setting comparisons, not uniformly."
        elif item.get("figure_label") == "rqr2026:fig:pharma-application-primary":
            item["alt_text"] = "Four panels summarize the pharmaceutical tensile metric on 187 batches with 1000 paired random partitions. The representative actual MTI-ECM interval uses split 479. Paired width and held-out-content differences compare ECM with Young--Mathew and Wilks; separate tail omissions and partition ranges characterize interval placement. Numerical stationarity is assessed separately from content."

    essentiality = load("docs/appendix-essentiality-map.json")
    appendix_paths = [f"appendices/{name}" for name in (
        "a-shared-conventions.tex", "b-exdqlm-technical.tex", "c-hydrology-technical.tex",
        "d-qdesn-technical.tex", "e-mti-technical.tex")]
    active_units = appendix_unit_inventory(ROOT, appendix_paths)
    labels = set(re.findall(r"\\label\{([^}]+)\}", (ROOT / APPENDIX).read_text(encoding="utf-8")))
    baseline_units = set(essentiality["coverage"]["baseline_unit_keys"])
    for item in essentiality["records"]:
        # Retain baseline recovery coverage, but stale intermediate derivative
        # headings cannot masquerade as current appendix units.
        if item.get("appendix") == "E":
            item["coverage_keys"] = [key for key in item["coverage_keys"]
                                     if key in baseline_units or key in active_units or key.startswith("display::")]
            if not item["coverage_keys"]:
                raise ValueError(f"{item['id']}: recovery coverage needs an explicit review; original baseline keys must remain immutable")
            if item.get("required_body_bridge") in {"app:mti-profile-computation", "app:e-technical"}:
                item["required_body_bridge"] = "app:mti-computation"
                item["recovery"]["no_loss_location"] = "app:mti-computation"
            if item["anchor"] == "rqr2026:prop:supp-convex-intercept-profile":
                item.update({"current_inclusion": "INACTIVE", "disposition": "DEACTIVATE",
                             "replacement_or_no_loss": "The active computation is derived through augmentation and Gibbs/ECM; the old convex-profile proposition remains recoverable in the prior dissertation commit.",
                             "rationale": "Author-approved replacement of the production computation; population identification profile arguments are retained."})
                item["recovery"]["git_commit"] = BASELINE
                item["recovery"]["no_loss_location"] = "app:mti-computation"
            item["status"] = "IMPLEMENTED"
            item["implementation"] = {"commit": BASELINE,
                "final_sha256": file_hash(item["target"]["path"]),
                "validation": f"{RECORD}; source/prose checks, release inspection recorded separately"}
    covered = {key for item in essentiality["records"] for key in item.get("coverage_keys", [])}
    holder = next(item for item in essentiality["records"] if item["id"] == "APPX-ESS-267")
    holder["anchor"] = "app:mti-computation"
    holder["rationale"] = "Retains the authenticated augmented-posterior, Gaussian/GIG conditional, Gibbs and finite-iteration ECM derivations."
    holder["coverage_keys"].extend(sorted(key for key in active_units - covered if key.startswith(APPENDIX + "::")))
    pseudo_displays = {key for item in essentiality["records"]
        if item["unit_type"] == "DISPLAY_FAMILY" and item["current_inclusion"] == "ACTIVE"
        for key in item["coverage_keys"] if key.startswith("display::")}
    essentiality["coverage"]["current_unit_keys"] = sorted(active_units | pseudo_displays)
    for bridge in essentiality.get("body_bridge_inventory", []):
        if bridge.get("source_path") == CHAPTER and bridge.get("target_label") == "app:mti-profile-computation":
            bridge["target_label"] = "app:mti-computation"
            bridge["final_location"] = "app:mti-computation"

    return {RECORD: record, "source-manifest.json": manifest,
        "docs/imports/ch05-mti.json": imports, "docs/claim-evidence.json": claims,
        "docs/revision-ledger.json": revision, "docs/appendix-migration-map.json": migration,
        "docs/display-ledger.json": displays, "docs/accessibility-ledger.json": accessibility,
        "docs/appendix-essentiality-map.json": essentiality}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rqr", required=True, type=Path)
    parser.add_argument("--extensions", required=True, type=Path)
    parser.add_argument("--extensions-commit", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.extensions_commit):
        parser.error("--extensions-commit requires a full Git commit")
    payloads = reconcile(args)
    for relative, payload in payloads.items():
        data = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
        if args.apply:
            (ROOT / relative).write_text(data, encoding="utf-8")
        print(("updated " if args.apply else "would update ") + relative)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
