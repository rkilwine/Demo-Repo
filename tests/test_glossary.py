import json
import tempfile
import unittest
from pathlib import Path
from src.fee_breakdown import FEE_TYPES, build_breakdown, load_glossary

class GlossaryTests(unittest.TestCase):
    def test_all_supported_types_have_short_explanations(self):
        glossary = load_glossary()
        self.assertTrue(glossary['synthetic'])
        for kind in FEE_TYPES:
            entry = glossary['entries'][kind]
            self.assertGreater(len(entry['explanation'].split()), 0)
            self.assertLessEqual(len(entry['explanation'].split()), 25)
            self.assertIn(entry['status'], {'demo_reviewed', 'in_review'})

    def test_unapproved_wording_is_visible_as_in_review(self):
        result = build_breakdown([{'type': 'fund_expense_ratio', 'amount': '1'}])
        self.assertEqual(result['lines'][0]['wording_status'], 'in_review')

    def test_external_configuration_changes_without_code_change(self):
        glossary = load_glossary()
        glossary['entries']['advisory_fee']['explanation'] = 'Revised synthetic explanation.'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'glossary.json'
            path.write_text(json.dumps(glossary), encoding='utf-8')
            result = build_breakdown([{'type': 'advisory_fee', 'amount': '1'}], load_glossary(path))
        self.assertEqual(result['lines'][0]['explanation'], 'Revised synthetic explanation.')

    def test_missing_glossary_entry_is_rejected(self):
        with self.assertRaises(ValueError):
            build_breakdown([{'type': 'advisory_fee', 'amount': '1'}], {'entries': {}})

if __name__ == '__main__':
    unittest.main()
