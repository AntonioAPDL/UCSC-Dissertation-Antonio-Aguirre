#!/usr/bin/env python3.11
"""Focused lifecycle-invariant tests for the research-audit validator."""

import copy
import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_research_audit", ROOT / "scripts" / "validate_research_audit.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


VALID = {
    "status": "MANUSCRIPT_CONVERSION_SYNCED_PENDING_SCIENTIFIC_AND_REUSE_REVIEW",
    "lifecycle": {
        "research_audit": "COMPLETE",
        "author_architecture_decision": "COMPLETE",
        "manuscript_conversion": "COMPLETE",
        "scientific_review": "NOT_STARTED",
        "reuse_review": "PENDING",
        "github_sync": "COMPLETE",
        "overleaf_handoff": "AUTHOR_REPORTED_COMPLETE",
    },
}


class LifecycleValidationTests(unittest.TestCase):
    def assert_invalid(self, update):
        record = copy.deepcopy(VALID)
        update(record)
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                MODULE.validate_lifecycle(record)

    def test_synced_conversion_state_is_valid(self):
        MODULE.validate_lifecycle(copy.deepcopy(VALID))

    def test_conversion_requires_completed_audit(self):
        self.assert_invalid(
            lambda record: record["lifecycle"].update(research_audit="IN_PROGRESS")
        )

    def test_overleaf_handoff_requires_github_sync(self):
        self.assert_invalid(
            lambda record: record["lifecycle"].update(github_sync="NOT_SYNCED")
        )

    def test_scientific_review_requires_completed_conversion(self):
        def update(record):
            record["status"] = "SCIENTIFIC_INTEGRATION_IN_PROGRESS_REUSE_REVIEW_PENDING"
            record["lifecycle"].update(
                manuscript_conversion="IN_PROGRESS", scientific_review="IN_PROGRESS"
            )

        self.assert_invalid(update)


if __name__ == "__main__":
    unittest.main()
