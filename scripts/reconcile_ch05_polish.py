#!/usr/bin/env python3.11
"""Refresh only current Chapter 5 editorial derivatives, preserving prior releases.

Check-only by default. --apply performs a mechanical JSON ledger refresh, never
manuscript edits, scientific computation, source checkout changes or publication.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import subprocess
from pathlib import Path

from appendix_essentiality import appendix_unit_inventory
from update_display_ledger import refreshed_payload

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "a56b66e256245436f5a93af65efa16ca35bba0cd"
DATE = "2026-11-12"
REVISION = "REV-CH05-POSTMIGRATION-POLISH-20261112"
RECORD = "docs/ch05-postmigration-polish-20261112.json"
HISTORICAL = "docs/ch05-mti-ecm-gibbs-migration-20261111.json"
CHAPTER = "chapters/05-research-d.tex"
APPENDIX = "appendices/e-mti-technical.tex"
TABLE = "tables/ch05-mti/pharma_application_primary_summary.tex"
PATHS = [CHAPTER, APPENDIX, "chapters/06-synthesis.tex",
         "frontmatter/acknowledgments.tex", TABLE]
REQUESTS = [
    "Contextual Chapter 5 and Appendix E prose polish",
    "Concrete mathematical and computational contributions",
    "Concise assistance disclosure consistent with documented use",
    "39/72 (54.2%) and 36/54 (66.7%) in results and synthesis",
    "Named width/attainment comparison under asymmetric sampling",
    "Accurate original RQR loss-minimization description",
    "MPI functional name distinguished from antecedent RQR procedure",
    "Integrated attribution rather than repetitive standalone sentence",
    "Tail-probability and first-moment connection clarified",
    "Author-owned results and proof headings named propositions",
    "Standard check-loss optimality citation, MTI-specific derivation retained",
    "Attainment table moved to Appendix E; main figures retained",
    "Compact pharmaceutical summary with unchanged values",
    "Discussion foregrounds supported contributions and empirical effects",
    "Requested global numerical optimality disclaimer removed from discussion",
    "Selective transitions and contextual prose-semicolon replacements",
    "Pointwise cutoff calibration distinguished from simultaneous validation",
    "Exact review map, tests and guarded Git integration",
]
REVIEW = [
    ("R01", CHAPTER, "rqr2026:sec:introduction", "Introduction and contributions"),
    ("R02", CHAPTER, "rqr2026:prop:population-characterization", "Attribution and tail interpretation"),
    ("R03", CHAPTER, "rqr2026:thm:quantile-window", "Proposition naming and identification"),
    ("R04", CHAPTER, "rqr2026:sec:static-theory-statements", "Training-sample balance and computation bridge"),
    ("R05", CHAPTER, "rqr2026:sec:mti-tolerance", "Calibration and validation distinction"),
    ("R06", CHAPTER, "rqr2026:fig:tolerance-validation-width-ranges", "Results and skewed-family width interpretation"),
    ("R07", TABLE, None, "Compact pharmaceutical summary; caption in Chapter 5"),
    ("R08", CHAPTER, "rqr2026:sec:discussion", "Connected contribution and results discussion"),
    ("R09", APPENDIX, "app:mti-proofs", "Proposition proof headings and empirical-balance citation"),
    ("R10", APPENDIX, "rqr2026:tab:tolerance-validation-primary", "Attainment table retained in appendix"),
    ("R11", "chapters/06-synthesis.tex", "sec:synthesis-findings", "MTI synthesis, formerly printed page 124"),
    ("R12", "frontmatter/acknowledgments.tex", None, "Accurate concise assistance disclosure"),
    ("R13", "frontmatter/abstract.tex", None, "MTI abstract paragraph reviewed and retained"),
    ("R14", "chapters/01-introduction.tex", None, "MTI introductory contribution reviewed and retained"),
    ("R15", CHAPTER, None, "Whole-chapter context and transition review"),
]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def file_hash(path: str) -> str:
    return digest((ROOT / path).read_bytes())


def baseline_bytes(path: str) -> bytes:
    return subprocess.run(["git", "-C", str(ROOT), "show", f"{BASELINE}:{path}"],
                          check=True, stdout=subprocess.PIPE).stdout


def changes(path: str) -> list[dict]:
    before = baseline_bytes(path).decode().splitlines()
    after = (ROOT / path).read_text(encoding="utf-8").splitlines()
    output = []
    for group in difflib.SequenceMatcher(a=before, b=after, autojunk=False).get_grouped_opcodes(2):
        a, b = group[0][1], group[-1][2]
        c, d = group[0][3], group[-1][4]
        output.append({"path": path, "baseline_lines": [a + 1, b],
                       "current_lines": [c + 1, d],
                       "before": "\n".join(before[a:b]),
                       "after": "\n".join(after[c:d])})
    return output


def payloads() -> dict[str, dict]:
    historical = load(HISTORICAL)
    if (ROOT / HISTORICAL).read_bytes() != baseline_bytes(HISTORICAL):
        raise ValueError("historical migration record changed")
    old_artifacts = {item["path"]: item["sha256"] for item in historical["artifacts"]}
    for path in PATHS:
        if digest(baseline_bytes(path)) != old_artifacts[path]:
            raise ValueError(f"baseline differs from historical release: {path}")
    prior = load(RECORD) if (ROOT / RECORD).is_file() else {}
    review = []
    for ident, path, label, description in REVIEW:
        text = (ROOT / path).read_text(encoding="utf-8")
        if label and rf"\label{{{label}}}" not in text:
            raise ValueError(f"review anchor missing: {label}")
        line = text[:text.index(rf"\label{{{label}}}")].count("\n") + 1 if label else 1
        locator = {
            "R11": r"\subsection{Fixed-content interval placement and tolerance inference}",
            "R12": "AI-assisted tools supported",
            "R13": "The fourth project",
            "R14": r"\paragraph{Mean-tilted intervals and tolerance actions.}",
        }.get(ident)
        if locator:
            line = text[:text.index(locator)].count("\n") + 1
        review.append({"id": ident, "path": path, "label": label,
                       "line": line, "description": description,
                       "disposition": "REVIEWED_RETAINED" if ident in {"R13", "R14"} else "EDITED",
                       **({"pdf_page": item["pdf_page"]} if (item := next(
                           (r for r in prior.get("review_map", []) if r["id"] == ident and "pdf_page" in r), None)) else {})})
    record = {
        "schema_version": 1, "date": DATE, "revision_id": REVISION,
        "baseline_commit": BASELINE,
        "status": prior.get("status", "IMPLEMENTED_PENDING_VALIDATION"),
        "scope": "Editorial Chapter 5 polish; scientific results, fits and source authorities unchanged",
        "baseline_migration_record": HISTORICAL,
        "baseline_migration_sha256": digest(baseline_bytes(HISTORICAL)),
        "artifacts": [{"path": p, "baseline_sha256": old_artifacts[p],
                       "current_sha256": file_hash(p)} for p in PATHS],
        "protected_artifacts": [{"path": p, "sha256": sha} for p, sha in old_artifacts.items() if p not in PATHS],
        "request_dispositions": [{"id": f"P{i:02}", "description": text,
                                  "status": "IMPLEMENTED"} for i, text in enumerate(REQUESTS, 1)],
        "review_map": review,
        "paragraph_changes": [h for p in PATHS for h in changes(p)],
        "empirical_summary": {"total_cases": 72, "narrower_than_young_mathew": 39,
            "narrower_percent": 54.2, "asymmetric_cases": 54, "asymmetric_narrower": 36,
            "asymmetric_narrower_percent": 66.7, "lognormal_max_width_reduction_percent": 30.6,
            "narrower_cases_with_higher_attainment": 39},
        "scientific_runs": 0,
        "validation": prior.get("validation", {"status": "PENDING"}),
        "publication": prior.get("publication", {"github": "PENDING", "overleaf": "NOT_PERFORMED"}),
    }
    for item in record["protected_artifacts"]:
        if file_hash(item["path"]) != item["sha256"]:
            raise ValueError(f"protected scientific or contextual artifact changed: {item['path']}")

    revision = load("docs/revision-ledger.json")
    revision["recorded_at"] = DATE
    for artifact in revision["artifacts"]:
        if artifact["path"] in PATHS:
            artifact["current_sha256"] = file_hash(artifact["path"])
            artifact["state"] = "EDITED"
            if REVISION not in artifact["revision_ids"]:
                artifact["revision_ids"].append(REVISION)
    revision["revisions"] = [r for r in revision["revisions"] if r["id"] != REVISION] + [{
        "id": REVISION, "date": DATE, "paths": sorted(PATHS),
        "summary": "Clarifies original RQR and MPI/MTI contributions, population propositions, empirical width gains, calibration language, and concise main/appendix presentation without scientific refitting.",
        "evidence": RECORD, "validation": "Scoped mutation tests, frozen-source gates, clean build and rendered inspection recorded in the polish receipt."}]

    imports = load("docs/imports/ch05-mti.json")
    for item in imports["current_projection"]["projected_items"]:
        if item.get("destination") == TABLE:
            item["destination_sha256"] = file_hash(TABLE)
            item["handling"] = "Compact editorial derivative: preserves three methods' authenticated median width and held-out content with empirical 95% partition ranges; repeated counts and endpoint/tail columns omitted in favor of caption and retained figure."
    imports["editorial_derivative"]["current_polish_record"] = RECORD
    # Existing source release/distribution history remains unchanged.

    manifest = load("source-manifest.json")
    manifest["execution_record"]["ch05_postmigration_polish"] = {
        "record": RECORD, "state": record["status"], "baseline_commit": BASELINE,
        "research_results_changed": False, "scientific_runs": 0}

    claims = load("docs/claim-evidence.json")
    claims["recorded_at"] = DATE
    for item in claims["records"]:
        if item["id"] == "ART-MTI-ECM-001":
            item["claim"] = "MTI-ECM has smaller mean width than Young--Mathew in 39/72 cases (54.2%), including 36/54 asymmetric cases (66.7%); the largest relative reduction is 30.6% in the strongly skewed lognormal case. All 39 narrower cases also have greater empirical content attainment."
            item["qualification"] = "Descriptive comparisons of the frozen finite-iteration ECM procedure over eight distributions and nine settings; not universal superiority, a causal effect of skewness, or a new distribution-free tolerance theorem."
            item["editorial_evidence"] = RECORD

    migration = load("docs/appendix-migration-map.json")
    for item in migration["records"]:
        if item["id"] in {"MIG-CH05-CURRENT-RQR", "MIG-CH05-CURRENT-MTI-EXT"}:
            item["source_file_sha256_after"] = file_hash(CHAPTER)
            item["destination_file_sha256_after"] = file_hash(APPENDIX)
            item["current_editorial_revision"] = RECORD

    displays = refreshed_payload(load("docs/display-ledger.json"))
    for item in displays["records"]:
        if item["id"] == "rqr2026:tab:tolerance-validation-primary":
            item["rationale"] = "Retains exact attainment ranges in Appendix E; the chapter presents the same comparison in the retained primary figure."
        if item["id"] == "rqr2026:tab:pharma-application-primary":
            item["rationale"] = "Compact quantitative anchor for width and held-out content; endpoint and tail placement remain in the retained pharmaceutical figure."

    essentiality = load("docs/appendix-essentiality-map.json")
    paths = [f"appendices/{name}" for name in (
        "a-shared-conventions.tex", "b-exdqlm-technical.tex", "c-hydrology-technical.tex",
        "d-qdesn-technical.tex", "e-mti-technical.tex")]
    active = appendix_unit_inventory(ROOT, paths)
    baseline = set(essentiality["coverage"]["baseline_unit_keys"])
    for item in essentiality["records"]:
        if item.get("appendix") == "E":
            keys = item["coverage_keys"]
            replacements = [key.replace("proof-of-theorem-", "proof-of-proposition-")
                            for key in keys if "proof-of-theorem-" in key]
            item["coverage_keys"] = [key for key in keys if key in baseline or key in active or key.startswith("display::")]
            item["coverage_keys"] += [key for key in replacements if key in active and key not in item["coverage_keys"]]
            item["implementation"]["final_sha256"] = file_hash(APPENDIX)
            item["implementation"]["current_editorial_record"] = RECORD
    holder = next(r for r in essentiality["records"] if r["id"] == "APPX-ESS-257")
    new_table = f"{APPENDIX}::label::rqr2026:tab:tolerance-validation-primary"
    if new_table not in holder["coverage_keys"]:
        holder["coverage_keys"].append(new_table)
    pseudo = {k for r in essentiality["records"]
              if r["unit_type"] == "DISPLAY_FAMILY" and r["current_inclusion"] == "ACTIVE"
              for k in r["coverage_keys"] if k.startswith("display::")}
    essentiality["coverage"]["current_unit_keys"] = sorted(active | pseudo)

    accessibility = load("docs/accessibility-ledger.json")
    for item in accessibility["graphics"]:
        if item.get("figure_label") == "rqr2026:fig:tolerance-validation-width-ranges":
            item["alt_text"] = "Nine sample-size/content panels compare mean widths and empirical 2.5--97.5 percent ranges for MTI-ECM, Young--Mathew and Wilks across eight distributions, on logarithmic width axes with shortest-contiguous population references. MTI-ECM has smaller mean width in 39 of 72 cases (54.2%), including 36 of 54 asymmetric cases (66.7%). Young--Mathew is narrower in all distributions at the three settings closest to the sample-range boundary."

    return {RECORD: record, "docs/revision-ledger.json": revision,
            "docs/imports/ch05-mti.json": imports, "source-manifest.json": manifest,
            "docs/claim-evidence.json": claims, "docs/appendix-migration-map.json": migration,
            "docs/display-ledger.json": displays, "docs/appendix-essentiality-map.json": essentiality,
            "docs/accessibility-ledger.json": accessibility}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    for path, payload in payloads().items():
        data = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
        if args.apply:
            (ROOT / path).write_text(data, encoding="utf-8")
        print(("updated " if args.apply else "would update ") + path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
