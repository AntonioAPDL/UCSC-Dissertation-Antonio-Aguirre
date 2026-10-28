#!/usr/bin/env python3.11
"""Initialize the approved appendix-unit essentiality and recovery map once."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

from appendix_essentiality import appendix_unit_inventory, normalized_sha256


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "appendix-essentiality-map.json"
BASELINE_COMMIT = "37b9da0fdb16168dff07efdc9454886f8467f6cd"
APPENDICES = {
    "A": ("1", "appendices/a-shared-conventions.tex", "175--178"),
    "B": ("2", "appendices/b-exdqlm-technical.tex", "179--192"),
    "C": ("3", "appendices/c-hydrology-technical.tex", "193--201"),
    "D": ("4", "appendices/d-qdesn-technical.tex", "202--312"),
    "E": ("5", "appendices/e-mti-technical.tex", "313--378"),
}

RETAINED_DISPLAYS = {
    "qdesn2026:tab:supp-reservoir-selection",
    "qdesn2026:tab:simulation-dgp",
    "qdesn2026:fig:independent-eval500-forecast_check",
    "qdesn2026:fig:supp-independent-quantile-calibration",
    "qdesn2026:tab:joint-qdesn-pure-desn-v2-recursive-policy",
    "qdesn2026:fig:supp-pricefm-r98-region-comparison",
    "qdesn2026:tab:supp-glofas-search3-specifications",
    "qdesn2026:fig:supp-glofas-part4-calibration",
    "rqr2026:tab:supp-mti-profile-policy",
    "rqr2026:tab:supp-scan-reference",
    "rqr2026:tab:supp-full-range-thresholds",
    "rqr2026:fig:supp-pharma-rsd",
    "rqr2026:fig:supp-pharma-partition-sensitivity",
}

APPENDIX_DISPLAYS = {
    "C": [
        "env:fig:synthsupport_20210123",
        "env:fig:synthsupport_20211221",
    ],
    "D": [
        "qdesn2026:tab:supp-reservoir-selection",
        "qdesn2026:fig:supp-quantile-sequential-initialization",
        "qdesn2026:tab:simulation-dgp",
        "qdesn2026:tab:independent-eval300-mcmc-normal",
        "qdesn2026:tab:independent-eval300-mcmc-laplace",
        "qdesn2026:tab:independent-eval300-mcmc-gausmix",
        "qdesn2026:tab:independent-vb-fit-preserved",
        "qdesn2026:fig:simulation-500obs-mcmc-forecast-mae-intervals",
        "qdesn2026:fig:simulation-500obs-mcmc-fit-rmse-intervals",
        "qdesn2026:fig:simulation-500obs-vb-fit-rmse-intervals",
        "qdesn2026:fig:independent-eval500-forecast_check",
        "qdesn2026:fig:independent-eval500-forecast_mae",
        "qdesn2026:tab:independent-eval500-mcmc-normal",
        "qdesn2026:tab:independent-eval500-mcmc-laplace",
        "qdesn2026:tab:independent-eval500-mcmc-gausmix",
        "qdesn2026:fig:supp-independent-quantile-calibration",
        "qdesn2026:tab:supp-independent-quantile-calibration",
        "qdesn2026:tab:joint-qdesn-pure-desn-v2-protocol",
        "qdesn2026:tab:joint-qdesn-pure-desn-v2-score",
        "qdesn2026:tab:joint-qdesn-pure-desn-v2-secondary",
        "qdesn2026:tab:joint-qdesn-pure-desn-v2-recursive-policy",
        "qdesn2026:tab:joint-qdesn-pure-desn-v2-vb-score",
        "qdesn2026:tab:joint-qdesn-pure-desn-v2-contrasts",
        "qdesn2026:tab:joint-qdesn-pure-desn-v2-crossings",
        "qdesn2026:fig:joint-qdesn-pure-desn-v2-fit-rmse",
        "qdesn2026:tab:joint-qdesn-pure-desn-v2-oracle",
        "qdesn2026:tab:supp-pricefm-fold-design",
        "qdesn2026:tab:supp-pricefm-r98-global-comparison",
        "qdesn2026:fig:supp-pricefm-r98-region-comparison",
        "qdesn2026:tab:supp-glofas-search3-specifications",
        "qdesn2026:tab:supp-glofas-part123-priors",
        "qdesn2026:tab:supp-glofas-part4-priors",
        "qdesn2026:fig:supp-glofas-part4-all-families",
        "qdesn2026:tab:supp-glofas-part123-scores",
        "qdesn2026:tab:supp-glofas-part4-convergence",
        "qdesn2026:tab:supp-glofas-part4-calibration",
        "qdesn2026:fig:supp-glofas-part1",
        "qdesn2026:fig:supp-glofas-part2",
        "qdesn2026:fig:supp-glofas-part3",
        "qdesn2026:fig:supp-glofas-part4-convergence",
        "qdesn2026:fig:supp-glofas-part4-calibration",
    ],
    "E": [
        "rqr2026:fig:supp-loss-geometry",
        "rqr2026:tab:supp-primary-dgp-delivery",
        "rqr2026:tab:supp-primary-dgp-width-ranges",
        "rqr2026:fig:supp-tolerance-population-shortest",
        "rqr2026:tab:supp-mti-profile-policy",
        "rqr2026:tab:supp-scan-reference",
        "rqr2026:tab:supp-full-range-thresholds",
        "rqr2026:tab:supp-pharma-response-diagnostics",
        "rqr2026:tab:supp-pharma-rsd",
        "rqr2026:tab:supp-pharma-primary-paired",
        "rqr2026:tab:supp-pharma-rsd-paired",
        "rqr2026:fig:supp-pharma-rsd",
        "rqr2026:tab:supp-pharma-primary-sensitivity",
        "rqr2026:tab:supp-pharma-rsd-sensitivity",
        "rqr2026:fig:supp-pharma-partition-sensitivity",
        "rqr2026:tab:supp-pharma-campaign",
        "rqr2026:tab:supp-pharma-numerical",
    ],
}

PROTECTED = [
    ("APPX-CONC-001", "Hydrologic results cover five origins, and the 28-day and common 8-day comparisons answer different questions.", ["Chapter 3 evaluation protocol and origin-specific score tables"]),
    ("APPX-CONC-002", "LDVB is approximate; MCMC remains the reference when posterior tails or interval accuracy are central.", ["Chapter 2 computation discussion", "Appendix B LDVB section"]),
    ("APPX-CONC-003", "The Q--DESN 500-target sensitivity is development-linked evidence rather than an untouched confirmation experiment.", ["Chapter 4 simulation interpretation", "Appendix D retained sensitivity figure"]),
    ("APPX-CONC-004", "MQ--DESN reduces crossings more consistently than it improves predictive score.", ["Chapter 4 multiquantile results"]),
    ("APPX-CONC-005", "All reported multiquantile winner and runner-up marginal intervals overlap.", ["Chapter 4 multiquantile results"]),
    ("APPX-CONC-006", "The descriptive GloFAS score leader remains undercovered, with particularly poor upper-quantile frequency for MQ--DESN exAL.", ["Chapter 4 GloFAS results", "Appendix D calibration figure"]),
    ("APPX-CONC-007", "Q--DESN does not dominate PriceFM in aggregate and its comparison varies by region and fold.", ["Chapter 4 PriceFM results", "Appendix D regional figure"]),
    ("APPX-CONC-008", "Calibrated MTI evidence is restricted to a fixed eight-distribution panel and is not a distribution-free theorem.", ["Chapter 5 validation design", "Appendix E calibration section"]),
    ("APPX-CONC-009", "MTI width is not uniformly smaller than Young--Mathew, especially near the sample-range boundary.", ["Chapter 5 validation results"]),
    ("APPX-CONC-010", "The pharmaceutical splits overlap, partition choice matters, and physical units for the derived response remain unresolved.", ["Chapter 5 application", "Appendix E application section"]),
    ("APPX-CONC-011", "The proposed endpoint regression and dynamic models have no matched implementation, simulation study, or application.", ["Chapter 5 proposed extensions", "Appendix E extension section"]),
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def headings(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    found: list[dict] = []
    pattern = re.compile(r"\\(section|subsection|subsubsection)\{(.+)\}\s*$")
    for index, line in enumerate(lines, 1):
        match = pattern.match(line.strip())
        if match:
            found.append({"level": match.group(1), "title": match.group(2), "start": index})
    for index, item in enumerate(found):
        item["end"] = (found[index + 1]["start"] - 1) if index + 1 < len(found) else len(lines)
        item["span"] = "\n".join(lines[item["start"] - 1 : item["end"]]) + "\n"
    return found


def decision(appendix: str, title: str) -> tuple[str, str]:
    lower = title.lower()
    if appendix == "A":
        if "complete details" in lower:
            return "DEACTIVATE", "Navigation belongs in the introduction and topical chapter bridges."
        if "latent-variable scales" in lower:
            return "CONDENSE", "Only the cross-chapter scale conversion is needed."
        return "RETAIN", "The distinction prevents incompatible statistical targets or uncertainty statements from being conflated."
    if appendix == "B":
        if "ldvb" in lower:
            return "RETAIN", "The structured scale--skewness approximation and its limits are nonstandard and claim-bearing."
        if "transfer-function" in lower or "synthesis" in lower:
            return "RETAIN", "This unit connects a chapter-level scientific or predictive construction to posterior computation."
        return "CONDENSE", "The inferential role is retained once; package-maintainer and repeated standard details are unnecessary."
    if appendix == "C":
        if "cutoff-specific" in lower:
            return "DEACTIVATE", "The body reports all five origins and already retains a representative synthesis display."
        if "parameter summaries" in lower:
            return "SUMMARIZE", "A short interpretation prevents likelihood parameters from being mistaken for synthesis weights."
        return "CONDENSE", "One integrated algorithm is sufficient; standard filtering and smoothing recursions can be cited."
    if appendix == "D":
        deactivate = ("metric summaries", "log marginal", "omitted variants", "implementation notes", "validation and consistency")
        summarize = ("evaluation period sensitivity", "forecast-path recovery", "computation and diagnostics", "pricefm design", "selection and initialization", "laplace", "crossing diagnostics")
        retain = ("augmented posterior", "likelihoods, priors", "mcmc full", "variational bayes", "mq--desn", "stacked exal", "quantile-indexed", "complete-data posterior", "structured exal", "glofas reference", "weighted augmented", "latent-path", "exact posterior", "posterior predictive", "direct posterior sampler", "use as initialization")
        if any(value in lower for value in deactivate):
            return "DEACTIVATE", "This development or duplicate calculation is recoverable from the baseline but does not support a distinct dissertation claim."
        if any(value in lower for value in summarize):
            return "SUMMARIZE", "The conclusion is retained without the full repeated computational or diagnostic path."
        if any(value in lower for value in retain):
            return "RETAIN", "This unit defines a nonstandard posterior, approximation, prior, or application target needed to audit Chapter 4."
        return "CONDENSE", "The statistical object remains necessary, but the chapter or a neighboring unit already supplies part of the derivation."
    deactivate = ("alternative ecm", "reproducibility and validation limits")
    retain = ("quantile-window", "mean-preserving contraction", "mean-tilted", "profile radius", "global profiled", "fractional empirical", "convex midpoint", "tolerance-validation", "pharmaceutical", "root labels", "pseudo-al", "gaussian root")
    if any(value in lower for value in deactivate):
        return "DEACTIVATE", "The reported calculation uses the retained profiled route or the material is internal validation inventory."
    if any(value in lower for value in retain):
        return "RETAIN", "This proof, calibration rule, application qualification, or nonstandard update is required to audit Chapter 5."
    return "CONDENSE", "The scientific distinction remains, but repeated exposition or standard calculation can be shortened."


def target_label(appendix: str, title: str) -> str:
    lower = title.lower()
    choices = {
        "A": [("", "app:shared-conventions")],
        "B": [("ldvb", "app:exdqlm-ldvb"), ("forecast", "app:exdqlm-synthesis"), ("posterior", "app:exdqlm-posterior")],
        "C": [("markov", "app:hydrology-mcmc"), ("variational", "app:hydrology-vb"), ("parameter", "app:hydrology-parameters")],
        "D": [("glofas", "app:qdesn-glofas-support"), ("pricefm", "app:qdesn-pricefm-support"), ("gaussian", "app:qdesn-gaussian-baseline"), ("reservoir", "app:qdesn-simulation-support"), ("simulation", "app:qdesn-simulation-support"), ("independent", "app:qdesn-simulation-support"), ("recursive-policy", "app:qdesn-simulation-support"), ("forecast", "app:qdesn-simulation-support"), ("calibration", "app:qdesn-simulation-support"), ("mcmc", "app:qdesn-computation"), ("variational", "app:qdesn-computation"), ("posterior", "app:qdesn-posterior"), ("likelihood", "app:qdesn-posterior")],
        "E": [("regression", "app:mti-extensions"), ("dynamic", "app:mti-extensions"), ("pharma", "app:mti-application-sensitivity"), ("mti-profile-policy", "app:mti-calibration"), ("scan-reference", "app:mti-calibration"), ("full-range-thresholds", "app:mti-calibration"), ("tolerance", "app:mti-calibration"), ("validation", "app:mti-calibration"), ("computation", "app:mti-profile-computation"), ("ecm", "app:mti-profile-computation"), ("interval", "app:mti-proofs"), ("mean", "app:mti-proofs"), ("empirical", "app:mti-proofs")],
    }
    for needle, label in choices[appendix]:
        if needle in lower:
            return label
    return f"app:{appendix.lower()}-technical"


def body_references(labels: list[str]) -> list[str]:
    result: list[str] = []
    for path in sorted((ROOT / "chapters").glob("*.tex")):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if any(re.search(rf"\\(?:ref|eqref|pageref|autoref)\{{{re.escape(label)}\}}", line) for label in labels):
                result.append(f"{path.relative_to(ROOT)}:{line_number}")
    return result


def locate_display(ident: str, default_path: str) -> tuple[str, int, str]:
    needle = rf"\label{{{ident}}}"
    for directory in (ROOT / "appendices", ROOT / "tables", ROOT / "figures", ROOT / "chapters"):
        for path in sorted(directory.rglob("*.tex")):
            text = path.read_text(encoding="utf-8", errors="replace")
            if needle in text:
                line = text[: text.index(needle)].count("\n") + 1
                return str(path.relative_to(ROOT)), line, normalized_sha256(text)
    return default_path, 1, sha256(ROOT / default_path)


def planned_bridge(path: str, line: int) -> tuple[str, str]:
    if path.endswith("01-introduction.tex"):
        return (
            "RETAIN_CHAPTER_BRIDGE",
            "app:exdqlm-technical" if line == 393 else "app:mti-technical",
        )
    if path.endswith("02-research-a.tex"):
        if line in {83, 174}:
            return "RETAIN_CHAPTER_BRIDGE", "app:exdqlm-technical"
        if line == 493:
            return "RETARGET", "app:exdqlm-posterior"
        if line == 475:
            return "RETARGET", "app:exdqlm-ldvb"
        return "RETARGET", "app:exdqlm-synthesis"
    if path.endswith("03-research-b.tex"):
        if line == 5:
            return "RETAIN_CHAPTER_BRIDGE", "app:hydrology-technical"
        if line == 200:
            return "RETARGET", "app:hydrology-mcmc"
        if line == 258:
            return "RETARGET", "app:hydrology-vb"
        return "REPLACE_WITH_BODY_EVIDENCE", ""
    if path.endswith("04-research-c.tex"):
        if line in {5, 152}:
            return "RETAIN_CHAPTER_BRIDGE", "app:qdesn-technical"
        if line <= 354:
            return "RETARGET", "app:qdesn-posterior"
        if line in {380, 412, 474, 528, 630}:
            return "RETARGET", "app:qdesn-computation"
        if line <= 655:
            return "RETARGET", "app:qdesn-simulation-support"
        if line <= 756:
            return "RETARGET", "app:qdesn-glofas-support"
        return "RETARGET", "app:qdesn-pricefm-support"
    if line in {5, 88}:
        return "RETAIN_CHAPTER_BRIDGE", "app:mti-technical"
    if line <= 409:
        return "RETARGET", "app:mti-proofs"
    if line <= 629:
        return "RETARGET", "app:mti-profile-computation"
    if line <= 904:
        return "RETARGET", "app:mti-calibration"
    if line <= 1013:
        return "RETARGET", "app:mti-application-sensitivity"
    return "RETARGET", "app:mti-extensions"


def bridge_inventory() -> list[dict]:
    chapter_labels = {
        "app:exdqlm-technical",
        "app:hydrology-technical",
        "app:qdesn-technical",
        "app:mti-technical",
    }
    records: list[dict] = []
    for path in sorted((ROOT / "chapters").glob("*.tex")):
        relative = str(path.relative_to(ROOT))
        lines = path.read_text(encoding="utf-8").splitlines()
        for line_number, line in enumerate(lines, 1):
            labels = [
                label
                for label in chapter_labels
                if re.search(rf"\\ref\{{{re.escape(label)}\}}", line)
            ]
            if not labels:
                continue
            action, target = planned_bridge(relative, line_number)
            records.append(
                {
                    "id": f"APPX-BRIDGE-{len(records) + 1:03d}",
                    "source_path": relative,
                    "baseline_line": line_number,
                    "baseline_label": labels[0],
                    "question_context": " ".join(line.strip().split()),
                    "action": action,
                    "target_label": target,
                    "status": "APPROVED",
                }
            )
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--refresh-approved-map",
        action="store_true",
        help="replace only the still-APPROVED, pre-TeX initialization map",
    )
    args = parser.parse_args()
    if OUTPUT.exists() and not args.refresh_approved_map:
        raise SystemExit(f"refusing to overwrite {OUTPUT.relative_to(ROOT)}")
    if OUTPUT.exists():
        current = json.loads(OUTPUT.read_text(encoding="utf-8"))
        if any(record.get("status") != "APPROVED" for record in current.get("records", [])):
            raise SystemExit("refusing to refresh a map with implemented or verified records")
    appendix_paths = [value[1] for value in APPENDICES.values()]
    inventory = appendix_unit_inventory(ROOT, appendix_paths)
    records: list[dict] = []
    assigned_keys: set[str] = set()
    next_id = 1

    for appendix, (chapter, relative, pages) in APPENDICES.items():
        path = ROOT / relative
        items = headings(path)
        source_lines = path.read_text(encoding="utf-8").splitlines()
        for item in items:
            prefix = f"{relative}::heading::{item['level']}::"
            heading_key = next(key for key in inventory if key.startswith(prefix) and key not in assigned_keys)
            unit_keys = {heading_key}
            assigned_keys.update(unit_keys)
            disposition, rationale = decision(appendix, item["title"])
            protected_ids: list[str] = []
            title_lower = item["title"].lower()
            if appendix == "B" and "ldvb" in title_lower:
                protected_ids.append("APPX-CONC-002")
            if appendix == "E" and ("tolerance" in title_lower or "validation" in title_lower):
                protected_ids.extend(["APPX-CONC-008", "APPX-CONC-009"])
            if appendix == "E" and "pharmaceutical" in title_lower:
                protected_ids.append("APPX-CONC-010")
            if appendix == "E" and ("regression" in title_lower or "dynamic" in title_lower):
                protected_ids.append("APPX-CONC-011")
            target = target_label(appendix, item["title"])
            records.append(
                {
                    "id": f"APPX-ESS-{next_id:03d}",
                    "appendix": appendix,
                    "chapter": chapter,
                    "unit_type": "SECTION",
                    "source_path": relative,
                    "anchor": item["title"],
                    "baseline": {
                        "line_start": item["start"],
                        "line_end": item["end"],
                        "pdf_pages": pages,
                        "source_span_sha256": normalized_sha256(item["span"]),
                    },
                    "migration_ids": [],
                    "display_ids": [],
                    "claim_ids": [],
                    "labels": [],
                    "citations": [],
                    "active_dependencies": [relative],
                    "body_references": [],
                    "question": "What technical support from this unit is necessary for the corresponding chapter claim?",
                    "disposition": disposition,
                    "current_inclusion": "ACTIVE",
                    "rationale": rationale,
                    "target": {"path": relative, "heading": item["title"], "label": ""},
                    "required_body_bridge": target,
                    "replacement_or_no_loss": "Retain the claim-bearing result in the target section or corresponding body statement.",
                    "protected_conclusion_ids": sorted(set(protected_ids)),
                    "recovery": {
                        "baseline_pdf_pages": pages,
                        "source_snapshot": f"thesis commit {BASELINE_COMMIT}",
                        "source_path": relative,
                        "git_commit": BASELINE_COMMIT,
                        "no_loss_location": target,
                    },
                    "coverage_keys": sorted(unit_keys),
                    "risk": "HIGH" if appendix in {"D", "E"} else "MODERATE",
                    "reviewer": "Antonio de Leon and dissertation advisors",
                    "status": "APPROVED",
                    "implementation": {},
                }
            )
            next_id += 1

        for key in sorted(inventory):
            if not key.startswith(f"{relative}::label::") or key in assigned_keys:
                continue
            ident = key.rsplit("::", 1)[-1]
            marker = rf"\label{{{ident}}}"
            line_number = next(
                (index for index, line in enumerate(source_lines, 1) if marker in line),
                1,
            )
            parent = max(
                (item for item in items if item["start"] <= line_number),
                key=lambda item: item["start"],
            )
            disposition, rationale = decision(appendix, parent["title"])
            if re.search(r":(?:thm|prop|lem|cor):", ident):
                unit_type = "THEOREM_PROOF"
                disposition = "CONDENSE" if ident.endswith("supp-dp-content-law") else "RETAIN"
                rationale = "The formal result and its proof obligation require an explicit authoritative location."
            elif re.search(r":alg(?::|$)", ident):
                unit_type = "ALGORITHM"
            else:
                unit_type = "EQUATION_GROUP"
            span_start = max(1, line_number - 8)
            span_end = min(len(source_lines), line_number + 8)
            span = "\n".join(source_lines[span_start - 1 : span_end]) + "\n"
            target = target_label(appendix, parent["title"])
            formal = {}
            body_statement = {
                "rqr2026:thm:supp-quantile-window": "rqr2026:thm:quantile-window",
                "rqr2026:prop:supp-mean-tilt": "rqr2026:prop:mean-tilt",
                "rqr2026:thm:supp-profiled-risk": "rqr2026:thm:profiled-mean-tilt",
            }.get(ident)
            if unit_type == "THEOREM_PROOF":
                formal = {
                    "statement_authority": body_statement or ident,
                    "appendix_role": "PROOF_ONLY" if body_statement else "STATEMENT_AND_PROOF",
                    "proof_location": target,
                }
            records.append(
                {
                    "id": f"APPX-ESS-{next_id:03d}",
                    "appendix": appendix,
                    "chapter": chapter,
                    "unit_type": unit_type,
                    "source_path": relative,
                    "anchor": ident,
                    "baseline": {
                        "line_start": span_start,
                        "line_end": span_end,
                        "pdf_pages": pages,
                        "source_span_sha256": normalized_sha256(span),
                    },
                    "migration_ids": [],
                    "display_ids": [],
                    "claim_ids": [],
                    "labels": [ident],
                    "citations": [],
                    "active_dependencies": [relative],
                    "body_references": body_references([ident]),
                    "question": "What equation, formal result, or algorithmic step must remain recoverable for the chapter claim?",
                    "disposition": disposition,
                    "current_inclusion": "ACTIVE",
                    "rationale": rationale,
                    "target": {"path": relative, "heading": parent["title"], "label": ""},
                    "required_body_bridge": target,
                    "replacement_or_no_loss": "Preserve the result, proof obligation, or nonstandard computational role in the target section.",
                    "protected_conclusion_ids": [],
                    "recovery": {
                        "baseline_pdf_pages": pages,
                        "source_snapshot": f"thesis commit {BASELINE_COMMIT}",
                        "source_path": relative,
                        "git_commit": BASELINE_COMMIT,
                        "no_loss_location": target,
                    },
                    "coverage_keys": [key],
                    "risk": "HIGH" if unit_type == "THEOREM_PROOF" or appendix in {"D", "E"} else "MODERATE",
                    "reviewer": "Antonio de Leon and dissertation advisors",
                    "status": "APPROVED",
                    "implementation": {},
                    **({"formal_result": formal} if formal else {}),
                }
            )
            assigned_keys.add(key)
            next_id += 1

    for appendix, display_ids in APPENDIX_DISPLAYS.items():
        chapter, default_path, pages = APPENDICES[appendix]
        for ident in display_ids:
            source_path, line, span_hash = locate_display(ident, default_path)
            coverage_key = f"{default_path}::label::{ident}"
            if coverage_key not in inventory:
                coverage_key = f"display::{ident}"
                inventory.add(coverage_key)
            for record in records:
                if coverage_key in record["coverage_keys"]:
                    record["coverage_keys"].remove(coverage_key)
            assigned_keys.add(coverage_key)
            retained = ident in RETAINED_DISPLAYS
            conclusions = {
                "qdesn2026:fig:independent-eval500-forecast_check": ["APPX-CONC-003"],
                "qdesn2026:tab:joint-qdesn-pure-desn-v2-recursive-policy": ["APPX-CONC-004", "APPX-CONC-005"],
                "qdesn2026:fig:supp-glofas-part4-calibration": ["APPX-CONC-006"],
                "qdesn2026:fig:supp-pricefm-r98-region-comparison": ["APPX-CONC-007"],
                "rqr2026:tab:supp-mti-profile-policy": ["APPX-CONC-008"],
                "rqr2026:tab:supp-full-range-thresholds": ["APPX-CONC-009"],
                "rqr2026:fig:supp-pharma-partition-sensitivity": ["APPX-CONC-010"],
                "env:fig:synthsupport_20210123": ["APPX-CONC-001"],
            }.get(ident, [])
            target = target_label(appendix, ident)
            records.append(
                {
                    "id": f"APPX-ESS-{next_id:03d}",
                    "appendix": appendix,
                    "chapter": chapter,
                    "unit_type": "DISPLAY_FAMILY",
                    "source_path": source_path,
                    "anchor": ident,
                    "baseline": {"line_start": line, "line_end": line, "pdf_pages": pages, "source_span_sha256": span_hash},
                    "migration_ids": [],
                    "display_ids": [ident],
                    "claim_ids": [],
                    "labels": [ident],
                    "citations": [],
                    "active_dependencies": [source_path],
                    "body_references": body_references([ident]),
                    "question": "Does this display provide evidence that changes or qualifies a dissertation claim?",
                    "disposition": "RETAIN" if retained else "DEACTIVATE",
                    "current_inclusion": "ACTIVE",
                    "rationale": "This is one of the exact claim-bearing displays approved in the controlling plan." if retained else "The claim is visible in the body or a retained display; the full display remains recoverable from the baseline.",
                    "target": {"path": default_path, "heading": "Selective empirical support", "label": ""},
                    "required_body_bridge": target,
                    "replacement_or_no_loss": "Retained display and interpretation." if retained else "Body conclusion or retained display identified by the protected-conclusion and bridge records.",
                    "protected_conclusion_ids": conclusions,
                    "recovery": {
                        "baseline_pdf_pages": pages,
                        "source_snapshot": f"thesis commit {BASELINE_COMMIT}",
                        "source_path": source_path,
                        "git_commit": BASELINE_COMMIT,
                        "no_loss_location": target,
                    },
                    "coverage_keys": [coverage_key],
                    "risk": "HIGH" if conclusions else "MODERATE",
                    "reviewer": "Antonio de Leon and dissertation advisors",
                    "status": "APPROVED",
                    "implementation": {},
                }
            )
            next_id += 1

    records = [record for record in records if record["coverage_keys"]]
    covered = {key for record in records for key in record["coverage_keys"]}
    if covered != inventory:
        raise SystemExit(f"coverage mismatch: missing={sorted(inventory-covered)!r}, extra={sorted(covered-inventory)!r}")

    pdf = ROOT / "build/release-20261028T044714Z/main.pdf"
    payload = {
        "schema_version": 1,
        "plan_id": "essential-appendix-revision-v2.1",
        "approval": {
            "status": "APPROVED",
            "date": "2026-10-28",
            "record": "docs/research-decisions.md#G5B",
            "scope": "Sixteen defaults and Phases 0--8; push, merge, and Overleaf synchronization excluded.",
        },
        "baseline": {
            "thesis_commit": BASELINE_COMMIT,
            "branch": "main",
            "appendix_source_sha256": {relative: sha256(ROOT / relative) for _, relative, _ in APPENDICES.values()},
            "pdf_path": str(pdf.relative_to(ROOT)),
            "pdf_sha256": sha256(pdf),
            "pdf_pages": 414,
            "appendix_pages": 204,
            "validation_counts": {"tests": 17, "research_sources": 8, "claim_records": 30, "display_records": 102, "active_tex_files": 83, "active_labels": 482, "migration_records": 6, "active_visual_records": 47},
        },
        "links": {
            "migration_map": "docs/appendix-migration-map.json",
            "display_ledger": "docs/display-ledger.json",
            "accessibility_ledger": "docs/accessibility-ledger.json",
            "claim_ledger": "docs/claim-evidence.json",
            "revision_ledger": "docs/revision-ledger.json",
            "source_refresh": "docs/source-refresh-20261026.json",
        },
        "coverage": {"baseline_unit_keys": sorted(inventory), "current_unit_keys": sorted(inventory)},
        "body_bridge_inventory": bridge_inventory(),
        "protected_conclusions": [
            {"id": ident, "statement": statement, "final_locations": locations, "status": "MAPPED"}
            for ident, statement, locations in PROTECTED
        ],
        "records": records,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    subprocess.run(["python3.11", "scripts/validate_structure.py"], cwd=ROOT, check=True)
    print(f"essentiality map written: {len(records)} records, {len(inventory)} covered units")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
