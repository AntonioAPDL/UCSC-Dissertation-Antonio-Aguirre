#!/usr/bin/env python3.11
"""Protect the evidence and display decisions of the Chapter 5 polish.

This is a manuscript consistency check, not a new simulation, convergence
assessment, or claim of institutional disclosure approval.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FAMILY_CSV = "tables/ch05-mti/ecm_family_case_summary_20261111.csv"
ASYMMETRIC = {
    "asym_laplace_tau010", "beta18", "exponential", "gamma05",
    "lognormal_hard", "two_piece_normal_1_12",
}
PROPOSITIONS = {
    "rqr2026:prop:population-characterization",
    "rqr2026:thm:quantile-window",
    "rqr2026:thm:profiled-mean-tilt",
}
MOVED_TABLE = "rqr2026:tab:tolerance-validation-primary"
RESULT_FIGURES = {
    "rqr2026:fig:tolerance-validation-primary",
    "rqr2026:fig:tolerance-validation-width-ranges",
    "rqr2026:fig:pharma-application-primary",
}
# Immutable scientific inputs at the pre-polish main a56b66e256245436f5a93af65efa16ca35bba0cd.
PROTECTED_HASHES = {
    "figures/ch05-mti/generated/fig01_three_balance_principles.png": "0ef8fc73eb3ad780475405a971d17da5eb63bacd28f0c461b39d348216d70ed3",
    "figures/ch05-mti/generated/fig03_mean_tilt_cf_anchors.png": "b46586c26575355c7bc4de79dd14d93f33c223871a5248d4060aefea18983c84",
    "figures/ch05-mti/generated/fig04_tolerance_validation_primary.png": "d09897db7feefaae8d701d89989614145ae5d7d2bf05f81e5e81f3f4cc3f254a",
    "figures/ch05-mti/generated/fig05_tolerance_validation_width_ranges.png": "16b9c1c4247da4875000aa7780c1389cd1ae7f2b12c32dc375478cd406c10a91",
    "figures/ch05-mti/generated/fig06_pharma_application_tensile_intervals.png": "c37c50487b3c3af742c37e1c12d327ce867bd9f72a10cedd59070080eee1f6a9",
    "figures/ch05-mti/generated/figS01_cross_distribution_recovery.png": "23287dc0f829f84a94dc73e04a9bc9b8033f3e49865e415fa56ea5d998219e90",
    "figures/ch05-mti/generated/figS02_loss_geometry.png": "8c454dbb06c547a84dc1389c4b39de909f41554c835ae68cba13c034d987928d",
    "figures/ch05-mti/generated/figS03_tolerance_population_shortest_intervals.png": "20c7540acb0be69533c536e6560342853f5423a79767968a5dfd390ce4e7117f",
    "figures/ch05-mti/generated/figS04_pharma_application_rsd_intervals.png": "86e924c25f887c1cb4078bb047b55ec34f22d417974bc9e5ff2e42a053f71447",
    "figures/ch05-mti/generated/figS05_pharma_application_partition_sensitivity.png": "ffa375767cc5d60e24c6ce9026a5f1b6cb22870c7dea56ef7709b414c6e019b0",
    FAMILY_CSV: "c66c9525b954d31bf76560274099213358f082724fdfff2a115864a195b32e47",
    "tables/ch05-mti/ecm_population_width_reference_20261111.csv": "946fc574dae08978c05ee30e69f59b0cac16d1c2b963aca007b18fc5ce7242bf",
    "tables/ch05-mti/pharma_application_numbers.tex": "090bb4ca972a4f41d569217fa0c92aa4b6f0d0707bf51909f533d490e95be77c",
    "tables/ch05-mti/tolerance_validation_article_scenario_ranges.tex": "980aebd8ea08cb4a0d9cae76cbbe51ae0fe41834b068e89e907319601bfa9b94",
}
PHARMA = {
    "MTI-ECM": ((0.553, 0.450, 0.628), (96.6, 87.7, 100.0)),
    "Young-Mathew": ((0.533, 0.445, 0.593), (95.4, 87.7, 100.0)),
    "Wilks": ((0.665, 0.552, 0.708), (98.9, 93.1, 100.0)),
}


def uncomment(text: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", line) for line in text.splitlines())


def normalized(text: str) -> str:
    return " ".join(uncomment(text).replace(r"\%", "%").split())


def summary_errors(rows: list[dict]) -> list[str]:
    """Reproduce the reported counts using matched DGP/sample-size/content keys."""
    errors = []
    cells = defaultdict(dict)
    try:
        for row in rows:
            key = (row["dgp_id"], int(row["n"]), float(row["content"]))
            if row["method"] in cells[key]:
                errors.append("duplicate matched method row in summary CSV")
            cells[key][row["method"]] = row
            if int(row["replications"]) != 1000:
                errors.append("summary replication count is not 1,000")
        methods = {"mti_ecm_adaptive_cell", "young_mathew", "wilks"}
        if len(rows) != 216 or len(cells) != 72:
            errors.append("summary must contain 216 method rows and 72 matched cases")
        if any(set(value) != methods for value in cells.values()):
            return errors + ["summary cases do not contain the three matched methods"]
        wins, asym_wins, asym_total, lognormal_reductions = [], 0, 0, []
        by_family = defaultdict(int)
        for (family, _, _), case in cells.items():
            ecm, ym = case["mti_ecm_adaptive_cell"], case["young_mathew"]
            reduction = 100 * (1 - float(ecm["width_mean"]) / float(ym["width_mean"]))
            if family in ASYMMETRIC:
                asym_total += 1
            if reduction > 0:
                gain = float(ecm["attainment"]) - float(ym["attainment"])
                wins.append(gain)
                by_family[family] += 1
                asym_wins += family in ASYMMETRIC
                if family == "lognormal_hard":
                    lognormal_reductions.append(reduction)
        if len(wins) != 39 or round(100 * len(wins) / 72, 1) != 54.2:
            errors.append("overall width advantage is not 39/72 (54.2%)")
        if (asym_wins, asym_total) != (36, 54):
            errors.append("asymmetric width advantage is not 36/54 (66.7%)")
        if any(by_family[family] != 6 for family in ASYMMETRIC):
            errors.append("each asymmetric family must have six of nine width gains")
        if any(gain <= 0 for gain in wins):
            errors.append("a narrower ECM comparison lacks higher empirical attainment")
        if not lognormal_reductions or round(max(lognormal_reductions), 1) != 30.6:
            errors.append("largest reported lognormal width reduction is not 30.6%")
    except (KeyError, ValueError, TypeError, ZeroDivisionError) as exc:
        errors.append(f"invalid numerical summary: {exc}")
    return errors


def text_errors(chapter: str, appendix: str, synthesis: str, acknowledgments: str) -> list[str]:
    errors = []
    chapter, appendix = uncomment(chapter), uncomment(appendix)
    propositions = "\n".join(re.findall(
        r"\\begin\{proposition\}(.*?)\\end\{proposition\}", chapter, re.DOTALL
    ))
    for label in sorted(PROPOSITIONS):
        if r"\label{" + label + "}" not in propositions:
            errors.append(f"population result is not enclosed in a proposition: {label}")
    if "implicit-function theorem" not in appendix:
        errors.append("standard implicit-function theorem reference was lost")
    table_token = r"\label{" + MOVED_TABLE + "}"
    if table_token in chapter or appendix.count(table_token) != 1:
        errors.append("attainment table must occur exactly once, in Appendix E")
    for label in sorted(RESULT_FIGURES):
        if chapter.count(r"\label{" + label + "}") != 1:
            errors.append(f"required result figure absent or duplicated: {label}")
    for name, text in (("Chapter 5", chapter), ("synthesis", synthesis)):
        prose = normalized(text)
        for value in ("54.2%", "66.7%"):
            if value not in prose:
                errors.append(f"{name} omits audited percentage {value}")
    prose = normalized(chapter + "\n" + appendix)
    if re.search(r"cutoff is (?:selected|fixed).{0,100}simultaneous calibration bounds", prose, re.I):
        errors.append("stale simultaneous cutoff-calibration claim")
    if not re.search(r"simultaneous.{0,80}(?:validation|interval)", prose, re.I):
        errors.append("independent simultaneous validation description was lost")
    if not all(value in prose.casefold() for value in ("0.9460", "0.9382", "pointwise")):
        errors.append("pointwise calibration and its adverse bounds must remain")
    if "30.6%" not in normalized(chapter):
        errors.append("Chapter 5 omits the authenticated lognormal reduction")
    if "qdesn-KoenkerBassett1978" not in chapter:
        errors.append("standard check-loss technique citation is absent")
    ack = normalized(acknowledgments)
    if re.search(r"AI-assisted tools were used only", ack, re.I):
        errors.append("disclosure retains an unsupported exclusive-use claim")
    if "take responsibility" not in ack:
        errors.append("disclosure must retain author responsibility")
    return errors


def table_errors(table: str) -> list[str]:
    errors = []
    table = uncomment(table)
    if len(re.findall(r"\\begin\{tabularx?\}", table)) != 1:
        errors.append("pharmaceutical summary must be one compact table")
    parsed = {}
    for line in table.splitlines():
        if "&" not in line:
            continue
        parts = [value.strip() for value in line.split("&")]
        method = re.sub(r"-+", "-", parts[0])
        if method in PHARMA:
            if len(parts) != 3:
                errors.append(f"{method} pharmaceutical row must have three columns")
                continue
            if method in parsed:
                errors.append(f"duplicate pharmaceutical row: {method}")
            parsed[method] = tuple(
                tuple(float(value) for value in re.findall(r"\d+\.\d+", cell))
                for cell in parts[1:]
            )
    if parsed != PHARMA:
        errors.append("compact pharmaceutical medians/ranges differ from frozen values")
    return errors


def hash_errors(root: Path, expected: dict[str, str] = PROTECTED_HASHES) -> list[str]:
    errors = []
    for relative, digest in expected.items():
        path = root / relative
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            errors.append(f"protected scientific asset changed: {relative}")
    return errors


def validate(root: Path = ROOT) -> list[str]:
    try:
        read = lambda relative: (root / relative).read_text(encoding="utf-8")
        errors = text_errors(
            read("chapters/05-research-d.tex"), read("appendices/e-mti-technical.tex"),
            read("chapters/06-synthesis.tex"), read("frontmatter/acknowledgments.tex"),
        )
        errors.extend(summary_errors(list(csv.DictReader(io.StringIO(read(FAMILY_CSV))))))
        errors.extend(table_errors(read("tables/ch05-mti/pharma_application_primary_summary.tex")))
        errors.extend(hash_errors(root))
        return errors
    except (OSError, UnicodeError) as exc:
        return [f"polish input unavailable: {exc}"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        print("Chapter 5 polish: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Chapter 5 polish: PASS (matched numerical summaries, displays, immutable assets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
