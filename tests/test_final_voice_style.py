"""Tests for the final voice and targeted prose validator."""

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
SPEC = importlib.util.spec_from_file_location(
    "validate_final_voice_style", ROOT / "scripts" / "validate_final_voice_style.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class FinalVoiceStyleTests(unittest.TestCase):
    def test_math_i_is_not_first_person(self):
        text = r"The identity is \(\mat I_K\). We use the resulting matrix."
        self.assertNotRegex(MODULE.prose_only(text), MODULE.SINGULAR)

    def test_singular_authorial_pronoun_is_detected(self):
        text = "My contribution is the revised algorithm."
        self.assertRegex(MODULE.prose_only(text), MODULE.SINGULAR)

    def test_display_math_is_removed(self):
        text = "Before.\\[ I_c(u)=[Q(u),Q(u+c)] \\]After."
        self.assertEqual("Before. After.", MODULE.prose_only(text))

    def test_citation_key_is_not_authorial_pronoun(self):
        text = r"The original procedure is due to \citet{exd-me}."
        self.assertNotRegex(MODULE.prose_only(text), MODULE.SINGULAR)

    def test_panel_range_is_not_authorial_pronoun(self):
        text = "Panels A--I report the nine settings."
        self.assertNotRegex(MODULE.prose_only(text), MODULE.SINGULAR)

    def test_file_hit_reports_location(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.tex"
            path.write_text("We define the target.\nI estimate it.\n", encoding="utf-8")
            hits = MODULE.singular_pronoun_hits({path})
            self.assertEqual(1, len(hits))
            self.assertIn("fixture.tex:2", hits[0])


if __name__ == "__main__":
    unittest.main()
