"""Mutation tests for factual and structural Chapter 5 polish controls."""

import copy
import csv
import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_ch05_polish", ROOT / "scripts/validate_ch05_polish.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class Ch05PolishTests(unittest.TestCase):
    def rows(self):
        with (ROOT / MODULE.FAMILY_CSV).open(encoding="utf-8") as handle:
            return list(csv.DictReader(handle))

    def texts(self):
        props = "\n".join(
            r"\begin{proposition}\label{" + label + r"} Statement.\end{proposition}"
            for label in sorted(MODULE.PROPOSITIONS)
        )
        figs = "\n".join(r"\label{" + label + "}" for label in MODULE.RESULT_FIGURES)
        chapter = props + figs + r" 54.2\% 66.7\% 30.6\% \citep{qdesn-KoenkerBassett1978}"
        appendix = r"\label{" + MODULE.MOVED_TABLE + "} implicit-function theorem. "
        appendix += "Pointwise bounds 0.9460 and 0.9382. Simultaneous validation intervals."
        return chapter, appendix, r"54.2\% 66.7\%", "We take responsibility for the final text."

    def test_authentic_matched_counts_are_accepted(self):
        self.assertEqual([], MODULE.summary_errors(self.rows()))

    def test_duplicate_matched_key_is_rejected(self):
        rows = self.rows()
        rows.append(copy.deepcopy(rows[0]))
        self.assertTrue(any("duplicate" in error for error in MODULE.summary_errors(rows)))

    def test_unmatched_method_is_rejected(self):
        rows = self.rows()
        rows[0]["method"] = "unmatched"
        self.assertTrue(any("matched methods" in error for error in MODULE.summary_errors(rows)))

    def test_changed_width_ordering_is_rejected(self):
        rows = self.rows()
        for row in rows:
            if row["method"] == "mti_ecm_adaptive_cell":
                row["width_mean"] = "1000000"
        self.assertTrue(any("39/72" in error for error in MODULE.summary_errors(rows)))

    def test_narrower_but_lower_attainment_is_rejected(self):
        rows = self.rows()
        for row in rows:
            if row["method"] == "mti_ecm_adaptive_cell":
                row["attainment"] = "0"
        self.assertTrue(any("higher empirical attainment" in error for error in MODULE.summary_errors(rows)))

    def test_scoped_proposition_and_validation_text_is_accepted(self):
        self.assertEqual([], MODULE.text_errors(*self.texts()))

    def test_theorem_substitution_is_rejected_for_own_result(self):
        texts = list(self.texts())
        texts[0] = texts[0].replace("{proposition}", "{theorem}", 2)
        self.assertTrue(any("not enclosed in a proposition" in error for error in MODULE.text_errors(*texts)))

    def test_standard_theorem_and_parameter_semicolon_are_not_banned(self):
        texts = list(self.texts())
        texts[1] += r" The implicit-function theorem applies to \(f(x;\theta)\)."
        self.assertEqual([], MODULE.text_errors(*texts))

    def test_table_left_in_main_is_rejected(self):
        texts = list(self.texts())
        texts[0] += r"\label{" + MODULE.MOVED_TABLE + "}"
        self.assertTrue(any("exactly once" in error for error in MODULE.text_errors(*texts)))

    def test_missing_figure_is_rejected(self):
        texts = list(self.texts())
        texts[0] = texts[0].replace(r"\label{" + sorted(MODULE.RESULT_FIGURES)[0] + "}", "")
        self.assertTrue(any("result figure" in error for error in MODULE.text_errors(*texts)))

    def test_stale_simultaneous_calibration_claim_is_rejected(self):
        texts = list(self.texts())
        texts[0] += " The cutoff is selected by the simultaneous calibration bounds."
        self.assertTrue(any("stale simultaneous" in error for error in MODULE.text_errors(*texts)))

    def test_wrong_displayed_percentage_is_rejected(self):
        texts = list(self.texts())
        texts[2] = texts[2].replace("54.2", "55.6")
        self.assertTrue(any("percentage" in error for error in MODULE.text_errors(*texts)))

    def test_overrestrictive_disclosure_is_rejected(self):
        texts = list(self.texts())
        texts[3] += " AI-assisted tools were used only for grammar."
        self.assertTrue(any("exclusive-use" in error for error in MODULE.text_errors(*texts)))

    def table(self):
        return "\n".join([
            r"\begin{tabularx}{\textwidth}{lXX}",
            r"MTI--ECM & 0.553 [0.450, 0.628] & 96.6 [87.7, 100.0] \\",
            r"Young--Mathew & 0.533 [0.445, 0.593] & 95.4 [87.7, 100.0] \\",
            r"Wilks & 0.665 [0.552, 0.708] & 98.9 [93.1, 100.0] \\",
            r"\end{tabularx}",
        ])

    def test_compact_authentic_table_is_accepted(self):
        self.assertEqual([], MODULE.table_errors(self.table()))

    def test_changed_pharmaceutical_value_is_rejected(self):
        self.assertTrue(MODULE.table_errors(self.table().replace("0.553", "0.500")))

    def test_duplicate_or_expanded_table_is_rejected(self):
        table = self.table().replace("0.553 [0.450, 0.628]", "1000 & 0.553 [0.450, 0.628]")
        self.assertTrue(any("three columns" in error for error in MODULE.table_errors(table)))
        self.assertTrue(any("one compact table" in error for error in MODULE.table_errors(self.table() * 2)))

    def test_scientific_hash_mutation_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "frozen.csv"
            path.write_bytes(b"original")
            hashes = {"frozen.csv": hashlib.sha256(b"original").hexdigest()}
            self.assertEqual([], MODULE.hash_errors(root, hashes))
            path.write_bytes(b"mutated")
            self.assertTrue(any("protected scientific asset" in error for error in MODULE.hash_errors(root, hashes)))


if __name__ == "__main__":
    unittest.main()
