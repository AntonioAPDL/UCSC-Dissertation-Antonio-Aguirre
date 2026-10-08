"""Regression tests for the active manuscript and appendix structure."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_structure", ROOT / "scripts" / "validate_structure.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


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
            "tables/ch04-qdesn/glofas_application_current_outputs.tex", relative
        )

    def test_moved_keep_display_remains_active(self):
        files, _ = MODULE.active_tex_files()
        text = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertIn(r"\label{qdesn:fig:supp-pricefm-r98-region-comparison}", text)
        ledger = json.loads((ROOT / "docs" / "display-ledger.json").read_text())
        record = next(
            item
            for item in ledger["records"]
            if item["id"] == "qdesn:fig:supp-pricefm-r98-region-comparison"
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


if __name__ == "__main__":
    unittest.main()
