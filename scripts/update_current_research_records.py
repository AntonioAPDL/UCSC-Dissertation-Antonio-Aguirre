#!/usr/bin/env python3.11
"""Reconcile the public source manifest and claim ledger after the 2026-10-26 refresh."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-10-26"
Q = "483e6edbec72ec76e48f2259e943e674b76e5041"
RQR = "4223c6a3a44f376255bacdca91db71cdf4f3afde"
EXD = "98cec593d11bf32715a690ae168086f16160e7f0"
OLD_Q = "757522db0f85815244370ec92a194de132268883"
OLD_RQR = "73887b9c86ef767aa1567c660718667945630aef"
OLD_EXD = "d5534e97db8414fd875022261d4c530eae4676e4"


def write(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def claim(
    ident: str,
    classification: str,
    text: str,
    source_id: str,
    commit: str,
    source_path: str,
    locator: str,
    level: str,
    status: str,
    qualification: str,
    disposition: str,
) -> dict:
    return {
        "id": ident,
        "classification": classification,
        "claim": text,
        "source_id": source_id,
        "commit": commit,
        "source_path": source_path,
        "locator": locator,
        "evidence_level": level,
        "verification_status": status,
        "qualification": qualification,
        "dissertation_disposition": disposition,
    }


def update_manifest() -> None:
    path = ROOT / "source-manifest.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["recorded_at"] = DATE
    data["lifecycle"]["state_note"] = (
        "The 2026-10-26 current-source refresh supersedes the September working "
        "snapshots for Q--DESN, the RQR/MTI tolerance article, and the exdqlm "
        "software article. The refresh passed full local release validation and "
        "rendered review and is awaiting merge, GitHub push, and a deliberate "
        "Overleaf pull. "
        "Material-specific reuse permission remains unverified."
    )
    data["execution_record"]["current_source_refresh"] = {
        "record": "docs/source-refresh-20261026.json",
        "audit": "docs/current-source-refresh-audit.md",
        "script": "scripts/refresh_current_research.py",
        "state": "RELEASE_AND_RENDERED_REVIEW_PASSED",
        "distinct_projected_destinations": 94,
        "release": {
            "path": "build/release-20261027T005737Z/main.pdf",
            "sha256": "92e4c36c451ecfceca2e0674e7d904f40f9b63e863f5799ba4b310dc262391d1",
            "pages": 439,
            "pdf_version": "1.7",
            "tracked": False,
        },
    }
    by_id = {item["id"]: item for item in data["sources"]}

    q = by_id["SRC-QDESN"]
    q["discovery_commit"] = Q
    q["audit_commit"] = Q
    q["audit_scope"] = (
        "Isolated partial Git clone at current origin/main; history comparison, "
        "manuscript/supplement inspection, and dependency-scoped asset projection"
    )
    q["inventory"]["tracked_files"] = 3393
    q["related_snapshots"] = [
        {
            "id": "SNAP-QDESN-THESIS-20260915",
            "ref": "prior dissertation working source",
            "commit": OLD_Q,
            "role": "immutable baseline for the first manuscript conversion",
        }
    ]
    q["imports"][0].update({
        "status": "CURRENT_REFRESH_RELEASE_VALIDATED",
        "scope": (
            "current main article in Chapter 4; current main and Gaussian "
            "technical material in Appendix D; only final active and "
            "claim-relevant display dependencies"
        ),
        "refresh": "docs/source-refresh-20261026.json",
    })

    rqr = by_id["SRC-RQR"]
    rqr["discovery_commit"] = RQR
    rqr["audit_commit"] = RQR
    rqr["audit_scope"] = (
        "Isolated partial Git clone at current origin/main; full main/supplement "
        "inspection and comparison with the prior TCSP-centered thesis snapshot"
    )
    rqr["inventory"]["tracked_files"] = 1406
    rqr["related_snapshots"] = [
        {
            "id": "SNAP-RQR-THESIS-20260915",
            "ref": "prior dissertation working source",
            "commit": OLD_RQR,
            "role": "immutable TCSP-era baseline for the first manuscript conversion",
        }
    ]
    rqr["imports"][0].update({
        "status": "CURRENT_REFRESH_RELEASE_VALIDATED",
        "scope": (
            "current profiled-MTI main article in Chapter 5 and current proofs, "
            "calibration protocol, and application diagnostics in Appendix E"
        ),
        "refresh": "docs/source-refresh-20261026.json",
    })

    exd = by_id["SRC-EXDQLM-ARTICLE"]
    exd["discovery_commit"] = EXD
    exd["audit_commit"] = EXD
    exd["audit_scope"] = (
        "Isolated partial Git clone at current origin/main; article/README diff "
        "audit and manuscript-only projection of the version 1.1.2 rerun"
    )
    exd["related_snapshots"] = [
        {
            "id": "SNAP-EXDQLM-ARTICLE-THESIS-20260915",
            "ref": "prior dissertation working source",
            "commit": OLD_EXD,
            "role": "immutable version 1.1.1 article baseline for the first conversion",
        }
    ]
    exd["imports"][0].update({
        "status": "CURRENT_REFRESH_RELEASE_VALIDATED",
        "scope": "version 1.1.2 article corrections and nine current displayed figures",
        "refresh": "docs/source-refresh-20261026.json",
    })

    unchanged_run_ids = {
        "RUN-ENV-LINEAGE", "RUN-SAN-VALIDATE", "RUN-MTI-TEX", "RUN-EXDQLM-PKG"
    }
    data["validation_runs"] = [
        item for item in data["validation_runs"] if item["id"] in unchanged_run_ids
    ] + [
        {
            "id": "RUN-QDESN-20261026-SOURCE-REFRESH",
            "source_id": "SRC-QDESN",
            "result": "PASS",
            "evidence_level": "E2",
            "summary": (
                "Current main, supplement, Gaussian supplement, override chain, "
                "and article-facing result tables were inspected; source Git-blob "
                "hashes and the pruned thesis projection are recorded"
            ),
        },
        {
            "id": "RUN-RQR-20261026-SOURCE-REFRESH",
            "source_id": "SRC-RQR",
            "result": "PASS",
            "evidence_level": "E2",
            "summary": (
                "Current profiled-MTI manuscript and supplement were compared with "
                "the prior TCSP-era source and projected with exact source hashes"
            ),
        },
        {
            "id": "RUN-EXDQLM-20261026-SOURCE-REFRESH",
            "source_id": "SRC-EXDQLM-ARTICLE",
            "result": "PASS",
            "evidence_level": "E2",
            "summary": (
                "Current 1.1.2 article, replication contract, numerical changes, "
                "and nine rerun figures were inspected and hash-recorded"
            ),
        },
    ]
    write(path, data)


def update_claims() -> None:
    path = ROOT / "docs/claim-evidence.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    preserved = [
        item for item in data["records"]
        if item["source_id"] not in {"SRC-QDESN", "SRC-RQR", "SRC-EXDQLM-ARTICLE"}
        and item["id"] != "CON-EXDQLM-003"
    ]
    current = [
        claim(
            "CLM-QDESN-001", "definition_or_setup",
            "Q--DESN models conditional quantiles using fixed deep echo-state features, AL or exAL working likelihoods, and shrinkage on the readout.",
            "SRC-QDESN", Q, "main.tex", "abstract and Fixed-Feature Bayesian Quantile Models",
            "E1", "located in the current main article",
            "The reservoir realization is fixed before regression fitting; likelihood language must retain its model-specific working interpretation.",
            "central Chapter 4 method claim",
        ),
        claim(
            "CLM-QDESN-002", "numerical_implementation_claim",
            "The current single-quantile evaluation treats 300 forecast targets as primary and 500 targets as a sensitivity analysis.",
            "SRC-QDESN", Q, "main.tex", "Single-quantile simulation design and results",
            "E2", "main text, display aliases, and supplement sensitivity sections agree",
            "The older 1000-target framing is not part of the current article result line.",
            "current Chapter 4 simulation contract",
        ),
        claim(
            "CLM-QDESN-003", "definition_or_setup",
            "MQ--DESN estimates quantile-specific coefficients jointly through adjacent-level shrinkage under a composite likelihood that reuses the observed response across levels.",
            "SRC-QDESN", Q, "main.tex", "Multiquantile regression (MQ--DESN)",
            "E1", "definition and composite-likelihood qualification are explicit",
            "The composite construction is not a normalized scalar-response joint likelihood.",
            "central Chapter 4 multiquantile method claim",
        ),
        claim(
            "ART-QDESN-004", "empirical_result",
            "In the current one-origin GloFAS experiment, Q--DESN AL is the descriptive score leader relative to the raw ensemble, but its nominal 90% interval covers 21 of 28 issued horizons.",
            "SRC-QDESN", Q, "main.tex", "Streamflow Quantile Forecast Correction results",
            "E2", "main prose and current Search III score/calibration displays agree",
            "The design conditions on realized future PRISM/ERA5 weather and does not establish operational or multi-origin dominance.",
            "central application result with calibration qualification",
        ),
        claim(
            "ART-QDESN-005", "empirical_result",
            "Across 114 matched PriceFM region--fold comparisons, Q--DESN has lower average quantile loss in 54 cases and PriceFM in 60, with a small aggregate difference favoring PriceFM.",
            "SRC-QDESN", Q, "main.tex", "Electricity-Price Quantile Forecasting results",
            "E2", "main prose, current alias values, and regional display agree",
            "Performance is heterogeneous across regions and folds; neither method uniformly dominates.",
            "central application comparison",
        ),
        claim(
            "ART-QDESN-008", "empirical_result",
            "MQ--DESN reduces quantile crossing without a uniform score gain; independent fits have the lowest mean oracle score in six of eight mechanisms and winner--runner-up intervals overlap in every mechanism.",
            "SRC-QDESN", Q, "main.tex", "Multiquantile simulation results",
            "E2", "current main and supporting multiquantile displays agree",
            "Crossing reduction and forecast-score improvement are different empirical criteria.",
            "retain mixed evidence and avoid dominance language",
        ),
        claim(
            "CON-QDESN-009", "publication_or_reuse_status_claim",
            "The current Q--DESN abstract retains an unresolved PriceFM placeholder although the results section contains the matched 114-comparison result.",
            "SRC-QDESN", Q, "main.tex", "abstract compared with PriceFM Results",
            "E2", "internal manuscript conflict confirmed",
            "The thesis resolves the placeholder only by restating the supported result; the upstream abstract still requires repair.",
            "documented thesis adaptation and upstream maintenance item",
        ),
        claim(
            "CLM-RQR-001", "proved_theorem_or_proposition",
            "Under the stated regularity conditions, the residual-product score characterizes the mean-preserving fixed-content interval.",
            "SRC-RQR", RQR, "main.tex", "Mean-Preserving Interval Target",
            "E1", "statement, conditions, and supplement proof located",
            "Do not extend the result beyond the stated iid continuous regular-interior setting without proof.",
            "central Chapter 5 theory claim",
        ),
        claim(
            "CLM-RQR-002", "definition_or_setup",
            "Mean-tilted intervals index admissible fixed-content windows by retained-mean balance; content, placement, and repeated-sampling confidence remain distinct inferential components.",
            "SRC-RQR", RQR, "main.tex", "Mean-Tilted Intervals",
            "E1", "target definition and interpretation located",
            "A tilt selected for a calibrated tolerance action is not automatically a response-likelihood parameter.",
            "mandatory target distinction",
        ),
        claim(
            "CLM-RQR-003", "numerical_implementation_claim",
            "The current tolerance method profiles fitted content and tilt over a prespecified grid, computes endpoints by a convex midpoint profile, screens candidates with a direct DP content probability, and reports the shortest eligible interval.",
            "SRC-RQR", RQR, "main.tex", "Calibrated MTI Tolerance Intervals",
            "E2", "main method, supplement proposition, and profile-policy table agree",
            "The grid and calibration policy are part of the reported method and must not be selected on validation outcomes.",
            "primary current Chapter 5 tolerance procedure",
        ),
        claim(
            "CON-RQR-004", "definition_or_setup",
            "Calibration settings are fixed on separate development and assessment samples before evaluation on independent validation samples.",
            "SRC-RQR", RQR, "main.tex", "Calibrated MTI Tolerance Intervals and Validation Design",
            "E2", "sample split and cutoff-selection protocol agree across main and supplement",
            "This design supports an empirical panel-specific assessment, not a distribution-free theorem.",
            "critical validation boundary",
        ),
        claim(
            "ART-RQR-003", "empirical_result",
            "Across 72 distribution-level validation cells, profiled MTI attainment ranges from 95.1% to 99.3%; no simultaneous validation interval has an upper endpoint below 0.95.",
            "SRC-RQR", RQR, "main.tex", "Validation Design results",
            "E2", "main summary and current validation tables agree",
            "The result pertains to the fixed eight-distribution panel and independent validation design; it is not a distribution-free guarantee.",
            "central empirical validation evidence",
        ),
        claim(
            "ART-RQR-005", "empirical_result",
            "Profiled MTI has smaller mean width than Young--Mathew in 40 of 72 validation cells and in six of nine designs for each asymmetric distribution.",
            "SRC-RQR", RQR, "main.tex", "Validation Design width comparison",
            "E2", "main summary and width-range displays agree",
            "Boundary cases often coincide with Wilks intervals, and width comparisons do not replace attainment checks.",
            "mixed efficiency evidence",
        ),
        claim(
            "ART-RQR-007", "empirical_result",
            "The pharmaceutical illustration uses 187 product-23 batches and 1000 paired 100-training/87-holdout splits, with recorded-order, month/API grouping, and numerical sensitivity checks.",
            "SRC-RQR", RQR, "main.tex", "Pharmaceutical Batch Application",
            "E2", "main, supplement, source-number macros, and current displays agree",
            "Held-out content is descriptive; overlapping splits, possible batch dependence, ties, and unresolved measurement units limit interpretation.",
            "application illustration with explicit data limitations",
        ),
        claim(
            "CON-MTI-004", "novelty_or_relationship_claim",
            "The unchanged MTI-EXTENSIONS manuscript shares the interval geometry with the current RQR article but predates its final profiled tolerance procedure.",
            "SRC-RQR", RQR, "main.tex", "current tolerance method compared with MTI-EXTENSIONS introduction",
            "E2", "cross-manuscript scope and terminology compared",
            "Use RQR as authority for tolerance inference and MTI-EXTENSIONS only for conditional fixed-target regression and dynamic proposals.",
            "one combined research chapter",
        ),
        claim(
            "CLM-EXDQLM-001", "novelty_or_relationship_claim",
            "The exdqlm article is software-centered and explicitly inherits the exAL family, exDQLM formulation, MCMC, ISVB, and transfer-function foundations.",
            "SRC-EXDQLM-ARTICLE", EXD, "exdqlm-jss.tex", "Introduction and contribution list",
            "E2", "current article wording checked against its cited methodological antecedents",
            "Do not attribute inherited methods or algorithms to the candidate without a separate contribution record.",
            "Chapter 2 software/infrastructure boundary",
        ),
        claim(
            "CON-EXDQLM-004", "numerical_implementation_claim",
            "The current article fixes its final rerun to public CRAN exdqlm 1.1.2 and records a flat replication interface with platform-stable fast dynamic MCMC state simulation.",
            "SRC-EXDQLM-ARTICLE", EXD, "README.md", "package source and replication-script sections",
            "E2", "README and current article implementation prose agree",
            "The full approximately 40-minute batch was not rerun in this thesis refresh; runtime values remain platform dependent.",
            "current Chapter 2 computation contract",
        ),
        claim(
            "ART-EXDQLM-005", "empirical_result",
            "The 1.1.2 rerun changes benchmark timings and selected stochastic summaries while preserving the examples' mixed substantive conclusions.",
            "SRC-EXDQLM-ARTICLE", EXD, "exdqlm-jss.tex", "Examples 1--4",
            "E2", "old-to-current article diff and nine changed displayed figures inspected",
            "Examples illustrate workflow and tradeoffs rather than uniform predictive or inferential superiority.",
            "retain current numerical values and negative evidence",
        ),
        claim(
            "CON-EXDQLM-003", "numerical_implementation_claim",
            "The Environmetrics application remains attached to its 1.1.0 snapshot, whereas the current exdqlm software article and package support snapshot are 1.1.2.",
            "SRC-EXDQLM-PKG", "e51045a4324901cced27ca2aaa22569afbc8e0e6", "DESCRIPTION",
            "Version field compared with the current article and application provenance",
            "E2", "version boundary checked across the three authorities",
            "A later software version must not silently replace the frozen application dependency.",
            "pin software provenance by chapter",
        ),
    ]
    data["recorded_at"] = DATE
    data["records"] = preserved + current
    write(path, data)


def main() -> int:
    update_manifest()
    update_claims()
    print("Current research manifest and claim ledger updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
