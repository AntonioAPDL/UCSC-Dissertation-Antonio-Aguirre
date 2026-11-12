"""Keep private absolute paths distinct from repository-relative data paths."""

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_manuscript_imports", ROOT / "scripts/validate_manuscript_imports.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ManuscriptPathGuardTests(unittest.TestCase):
    def test_absolute_data_path_is_rejected(self):
        self.assertRegex('"/data/user/project/results.csv"', MODULE.ABSOLUTE_SERVER_PATH)

    def test_absolute_home_path_is_rejected(self):
        self.assertRegex("/home/user/secret.txt", MODULE.ABSOLUTE_SERVER_PATH)

    def test_absolute_tmp_path_is_rejected(self):
        self.assertRegex("source: /tmp/audit/main.tex", MODULE.ABSOLUTE_SERVER_PATH)

    def test_repository_relative_frozen_data_path_is_accepted(self):
        path = "figures/data/mti_ecm_validation_20261111/family_case_summary.csv"
        self.assertNotRegex(path, MODULE.ABSOLUTE_SERVER_PATH)

    def test_repository_relative_home_named_directory_is_accepted(self):
        self.assertNotRegex("examples/home/illustration.tex", MODULE.ABSOLUTE_SERVER_PATH)


if __name__ == "__main__":
    unittest.main()
