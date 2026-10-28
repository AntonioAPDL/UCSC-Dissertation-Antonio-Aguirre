"""Regression tests for the active manuscript and appendix structure."""

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
SPEC = importlib.util.spec_from_file_location(
    "validate_structure", ROOT / "scripts" / "validate_structure.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)

ESS_SPEC = importlib.util.spec_from_file_location(
    "appendix_essentiality", ROOT / "scripts" / "appendix_essentiality.py"
)
ESSENTIALITY = importlib.util.module_from_spec(ESS_SPEC)
assert ESS_SPEC.loader is not None
ESS_SPEC.loader.exec_module(ESSENTIALITY)

EDITORIAL_SPEC = importlib.util.spec_from_file_location(
    "validate_editorial_audit", ROOT / "scripts" / "validate_editorial_audit.py"
)
EDITORIAL = importlib.util.module_from_spec(EDITORIAL_SPEC)
assert EDITORIAL_SPEC.loader is not None
EDITORIAL_SPEC.loader.exec_module(EDITORIAL)


class StructureValidationTests(unittest.TestCase):
    def test_active_graph_contains_scientific_appendices_not_demo(self):
        files, _ = MODULE.active_tex_files()
        relative = {str(path.relative_to(ROOT)) for path in files}
        self.assertIn("appendices/a-shared-conventions.tex", relative)
        self.assertIn("appendices/e-mti-technical.tex", relative)
        self.assertNotIn("appendices/a-format-demonstration.tex", relative)

    def test_compiler_graph_resolves_macro_input(self):
        files, dynamic = MODULE.active_tex_files()
        relative = {str(path.relative_to(ROOT)) for path in files}
        self.assertTrue(dynamic)
        self.assertIn(
            "tables/ch04-qdesn/current_source_aliases_20261026.tex", relative
        )

    def test_moved_keep_display_remains_active(self):
        files, _ = MODULE.active_tex_files()
        text = "\n".join(path.read_text(encoding="utf-8") for path in files)
        current_label = "qdesn2026:fig:supp-pricefm-r98-region-comparison"
        self.assertIn(rf"\label{{{current_label}}}", text)
        ledger = json.loads((ROOT / "docs" / "display-ledger.json").read_text())
        record = next(
            item
            for item in ledger["records"]
            if item["id"] == current_label
        )
        self.assertEqual("KEEP", record["disposition"])

    def test_appendices_have_no_machine_paths(self):
        for path in ROOT.glob("appendices/[a-e]-*.tex"):
            text = path.read_text(encoding="utf-8")
            self.assertNotRegex(text, r"/(?:data|home)/")

    def test_static_graph_reports_a_missing_input(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            main = root / "main.tex"
            main.write_text(r"\input{fixture-that-does-not-exist}" + "\n")
            _, _, missing = MODULE.active_tex_graph(root, main)
            self.assertEqual({"fixture-that-does-not-exist"}, missing)

    def test_duplicate_label_helper_reports_active_duplicates(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "first.tex"
            second = root / "second.tex"
            first.write_text(r"\label{fixture:duplicate}" + "\n")
            second.write_text(r"\label{fixture:duplicate}" + "\n")
            self.assertEqual(
                {"fixture:duplicate": 2}, MODULE.duplicate_labels({first, second})
            )

    def essentiality_fixture(self, root):
        source = root / "appendix.tex"
        source.write_text("fixture\n", encoding="utf-8")
        return {
            "schema_version": 1,
            "plan_id": "essential-appendix-revision-v2",
            "approval": {"status": "APPROVED", "date": "2026-10-28"},
            "baseline": {},
            "links": {},
            "protected_conclusions": [
                {
                    "id": "APPX-CONC-001",
                    "statement": "A protected finding.",
                    "final_locations": ["chapter fixture"],
                }
            ],
            "records": [
                {
                    "id": "APPX-ESS-001",
                    "appendix": "C",
                    "chapter": "3",
                    "unit_type": "DISPLAY_FAMILY",
                    "source_path": "appendix.tex",
                    "anchor": "fixture",
                    "display_ids": ["fixture:fig:inactive"],
                    "labels": ["fixture:fig:inactive"],
                    "disposition": "DEACTIVATE",
                    "current_inclusion": "INACTIVE",
                    "rationale": "The finding remains in prose.",
                    "replacement_or_no_loss": "Retained body statement.",
                    "target": {"path": "appendix.tex", "label": "fixture:section"},
                    "protected_conclusion_ids": ["APPX-CONC-001"],
                    "recovery": {
                        "baseline_pdf_pages": "1",
                        "source_path": "appendix.tex",
                        "git_commit": "a" * 40,
                        "no_loss_location": "chapter fixture",
                    },
                    "coverage_keys": ["fixture-unit"],
                    "risk": "LOW",
                    "reviewer": "author",
                    "status": "IMPLEMENTED",
                    "implementation": {
                        "commit": "b" * 40,
                        "final_sha256": __import__("hashlib").sha256(source.read_bytes()).hexdigest(),
                        "validation": "fixture",
                    },
                }
            ],
        }

    def test_approved_inactive_keep_display_is_allowed(self):
        with tempfile.TemporaryDirectory() as directory:
            payload = self.essentiality_fixture(Path(directory))
            self.assertEqual(
                {"fixture:fig:inactive"},
                ESSENTIALITY.approved_inactive_display_ids(payload),
            )

    def test_unapproved_missing_keep_display_is_not_allowed(self):
        errors = EDITORIAL.display_presence_errors(
            [
                {
                    "id": "fixture:fig:missing",
                    "disposition": "KEEP",
                    "implementation_status": "IMPLEMENTED",
                }
            ],
            set(),
            {},
        )
        self.assertEqual(["KEEP display is absent: fixture:fig:missing"], errors)

    def test_stale_active_accessibility_record_fails(self):
        accessibility = {
            "graphics": [
                {
                    "source_path": "appendix.tex",
                    "graphic": "fixture.pdf",
                    "figure_label": "fixture:fig:inactive",
                    "alt_text": "fixture",
                    "status": "REVIEWED",
                    "current_inclusion": "ACTIVE",
                }
            ]
        }
        errors, _ = MODULE.accessibility_errors(accessibility, set(), {})
        self.assertTrue(any("marked active" in error for error in errors))

    def test_body_reference_to_inactive_label_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = self.essentiality_fixture(root)
            errors = ESSENTIALITY.validate_payload(
                payload, root, body_references={"fixture:fig:inactive"}
            )
            self.assertTrue(any("body references inactive" in error for error in errors))

    def test_inactive_record_requires_recovery_pointer(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = self.essentiality_fixture(root)
            payload["records"][0]["recovery"].pop("no_loss_location")
            errors = ESSENTIALITY.validate_payload(payload, root)
            self.assertTrue(any("missing recovery" in error for error in errors))

    def test_protected_conclusion_requires_responsible_record(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = self.essentiality_fixture(root)
            payload["records"][0]["protected_conclusion_ids"] = []
            errors = ESSENTIALITY.validate_payload(payload, root)
            self.assertTrue(any("lack a responsible record" in error for error in errors))

    def test_historical_migration_marker_is_preserved(self):
        migration = json.loads((ROOT / "docs" / "appendix-migration-map.json").read_text())
        for record in migration["records"]:
            destination = ROOT / record["destination_path"]
            self.assertIn(
                f"% migration-id: {record['id']}",
                destination.read_text(encoding="utf-8"),
            )


if __name__ == "__main__":
    unittest.main()
