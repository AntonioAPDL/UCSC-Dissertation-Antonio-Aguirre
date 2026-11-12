"""Regression tests for the source-aware Chapter 5 manuscript migration."""

import importlib.util
import hashlib
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_mti_migration", ROOT / "scripts/validate_mti_migration.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class MtiMigrationTests(unittest.TestCase):
    def fixture(self):
        labels = "\n".join(r"\label{" + label + "}" for label in MODULE.REQUIRED_LABELS)
        chapter = labels + r"\[L=-q\delta(a+b-2y_i),\quad H=H_0+\omega_{\mathrm R}nq\delta.\]"
        return chapter, "ECM estimates a mode. Gibbs samples raw roots.", "", {
            "gibbs_empirical_status": "NOT_REPORTED"
        }

    def test_complete_method_without_invented_results_is_accepted(self):
        self.assertEqual([], MODULE.text_errors(*self.fixture()))

    def test_missing_gibbs_algorithm_is_rejected(self):
        chapter, appendix, context, record = self.fixture()
        chapter = chapter.replace(r"\label{alg:ch05-mti-gibbs}", "")
        self.assertTrue(any("alg:ch05-mti-gibbs" in item for item in MODULE.text_errors(chapter, appendix, context, record)))

    def test_old_production_computation_is_rejected(self):
        chapter, appendix, context, record = self.fixture()
        context = "We compute endpoints by a convex profile calculation."
        self.assertTrue(any("superseded" in item for item in MODULE.text_errors(chapter, appendix, context, record)))

    def test_population_profile_argument_is_not_prohibited(self):
        chapter, appendix, context, record = self.fixture()
        appendix += " The population identification proof uses a profiled risk."
        self.assertEqual([], MODULE.text_errors(chapter, appendix, context, record))

    def test_wrong_computational_tilt_sign_is_rejected(self):
        chapter, appendix, context, record = self.fixture()
        chapter = chapter.replace(r"-q\delta", r"+q\delta")
        self.assertTrue(any("computational loss" in item for item in MODULE.text_errors(chapter, appendix, context, record)))

    def test_missing_content_factor_in_tilt_is_rejected(self):
        chapter, appendix, context, record = self.fixture()
        chapter = chapter.replace(r"-q\delta", r"-\delta")
        self.assertTrue(any("computational loss" in item for item in MODULE.text_errors(chapter, appendix, context, record)))

    def test_wrong_root_canonical_tilt_sign_is_rejected(self):
        chapter, appendix, context, record = self.fixture()
        chapter = chapter.replace(r"+\omega_{\mathrm R}", r"-\omega_{\mathrm R}")
        self.assertTrue(any("canonical parameter" in item for item in MODULE.text_errors(chapter, appendix, context, record)))

    def test_anticipated_gibbs_agreement_is_not_reported_as_observed(self):
        chapter, appendix, context, record = self.fixture()
        context = "Gibbs means are comparable to ECM estimates."
        self.assertTrue(any("unverified Gibbs" in item for item in MODULE.text_errors(chapter, appendix, context, record)))

    def test_fabricated_speed_ratio_is_rejected(self):
        chapter, appendix, context, record = self.fixture()
        context = "ECM is 100 times faster than Gibbs."
        self.assertTrue(any("unverified Gibbs" in item for item in MODULE.text_errors(chapter, appendix, context, record)))

    def test_comment_does_not_create_a_result(self):
        chapter, appendix, context, record = self.fixture()
        context = "% Gibbs means are comparable to ECM estimates.\n"
        self.assertEqual([], MODULE.text_errors(chapter, appendix, context, record))

    def disk_fixture(self, directory):
        root = Path(directory)
        chapter, appendix, _, record = self.fixture()
        files = {
            "chapters/05-research-d.tex": chapter,
            "appendices/e-mti-technical.tex": appendix,
            "frontmatter/abstract.tex": "",
            "frontmatter/acknowledgments.tex": "",
            "chapters/01-introduction.tex": "",
            "chapters/06-synthesis.tex": "",
            "docs/historical-fixture.json": "unchanged historical fixture\n",
        }
        for relative, content in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        record.update({
            "schema_version": 1,
            "artifacts": [{"path": "chapters/05-research-d.tex",
                           "sha256": hashlib.sha256(chapter.encode()).hexdigest()}],
            "protected_history": [{"path": "docs/historical-fixture.json",
                                   "sha256": hashlib.sha256(files["docs/historical-fixture.json"].encode()).hexdigest()}],
            "source_artifacts": [{"source_id": "SRC-UNIT-FIXTURE", "clone": "fixture",
                                  "commit": "a" * 40, "path": "main.tex",
                                  "sha256": "b" * 64}],
        })
        (root / MODULE.RECORD).write_text(json.dumps(record), encoding="utf-8")
        return root

    def test_complete_hash_record_is_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.disk_fixture(directory)
            self.assertEqual([], MODULE.validate(root))

    def test_changed_manuscript_hash_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.disk_fixture(directory)
            with (root / "chapters/05-research-d.tex").open("a", encoding="utf-8") as handle:
                handle.write("\nAdditional prose.\n")
            self.assertTrue(any("artifact hash mismatch" in item for item in MODULE.validate(root)))

    def test_historical_receipt_mutation_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.disk_fixture(directory)
            (root / "docs/historical-fixture.json").write_text("rewritten", encoding="utf-8")
            self.assertTrue(any("immutable historical control changed" in item for item in MODULE.validate(root)))

    def test_nonimmutable_source_pin_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.disk_fixture(directory)
            path = root / MODULE.RECORD
            record = json.loads(path.read_text(encoding="utf-8"))
            record["source_artifacts"][0]["commit"] = "main"
            path.write_text(json.dumps(record), encoding="utf-8")
            self.assertTrue(any("full Git commit" in item for item in MODULE.validate(root)))

    def polish_fixture(self, root):
        record = json.loads((root / MODULE.RECORD).read_text(encoding="utf-8"))
        artifact = record["artifacts"][0]
        path = root / artifact["path"]
        path.write_text(path.read_text(encoding="utf-8") + "\nEditorial derivative.\n", encoding="utf-8")
        polish = {
            "baseline_migration_sha256": hashlib.sha256((root / MODULE.RECORD).read_bytes()).hexdigest(),
            "artifacts": [{"path": artifact["path"], "baseline_sha256": artifact["sha256"],
                           "current_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}],
        }
        return polish

    def test_source_locked_polish_override_is_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.disk_fixture(directory)
            polish = self.polish_fixture(root)
            (root / MODULE.POLISH_RECORD).write_text(json.dumps(polish), encoding="utf-8")
            self.assertEqual([], MODULE.validate(root))

    def test_polish_cannot_rewrite_migration_record_baseline(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.disk_fixture(directory)
            polish = self.polish_fixture(root)
            polish["baseline_migration_sha256"] = "0" * 64
            (root / MODULE.POLISH_RECORD).write_text(json.dumps(polish), encoding="utf-8")
            self.assertTrue(any("baseline migration record" in item for item in MODULE.validate(root)))

    def test_polish_cannot_rewrite_original_artifact_identity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.disk_fixture(directory)
            polish = self.polish_fixture(root)
            polish["artifacts"][0]["baseline_sha256"] = "0" * 64
            (root / MODULE.POLISH_RECORD).write_text(json.dumps(polish), encoding="utf-8")
            self.assertTrue(any("baseline artifact hash" in item for item in MODULE.validate(root)))

    def test_polish_unknown_override_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.disk_fixture(directory)
            polish = self.polish_fixture(root)
            polish["artifacts"][0]["path"] = "unrelated.tex"
            (root / MODULE.POLISH_RECORD).write_text(json.dumps(polish), encoding="utf-8")
            self.assertTrue(any("unknown polish artifact" in item for item in MODULE.validate(root)))

    def test_polish_duplicate_override_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.disk_fixture(directory)
            polish = self.polish_fixture(root)
            polish["artifacts"].append(dict(polish["artifacts"][0]))
            (root / MODULE.POLISH_RECORD).write_text(json.dumps(polish), encoding="utf-8")
            self.assertTrue(any("duplicate polish artifact" in item for item in MODULE.validate(root)))

    def test_polish_stale_current_hash_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.disk_fixture(directory)
            polish = self.polish_fixture(root)
            polish["artifacts"][0]["current_sha256"] = "0" * 64
            (root / MODULE.POLISH_RECORD).write_text(json.dumps(polish), encoding="utf-8")
            self.assertTrue(any("artifact hash mismatch" in item for item in MODULE.validate(root)))


if __name__ == "__main__":
    unittest.main()
