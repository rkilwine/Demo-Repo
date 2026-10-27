import json
import unittest
from decimal import Decimal
from src.fee_breakdown import ROOT, build_breakdown

class FeeBreakdownTests(unittest.TestCase):
    def test_normal_total(self):
        result = build_breakdown([{'type': 'advisory_fee', 'amount': '12.34'}, {'type': 'transaction_fee', 'amount': '1.00'}])
        self.assertEqual(result['total'], '13.34')
        self.assertTrue(result['synthetic'])

    def test_zero_total(self):
        self.assertEqual(build_breakdown([{'type': 'advisory_fee', 'amount': '0'}])['total'], '0.00')

    def test_half_cent_boundary_total_matches_lines(self):
        result = build_breakdown([{'type': 'advisory_fee', 'amount': '12.345'}, {'type': 'fund_expense_ratio', 'amount': '3.335'}])
        self.assertEqual([item['amount'] for item in result['lines']], ['12.35', '3.34'])
        self.assertEqual(result['total'], '15.69')
        self.assertEqual(Decimal(result['total']), sum(Decimal(item['amount']) for item in result['lines']))

    def test_all_synthetic_fixtures(self):
        data = json.loads((ROOT / 'data/accounts.json').read_text())
        for case in data['cases']:
            with self.subTest(case=case['id']):
                self.assertEqual(build_breakdown(case['fees'])['total'], case['expected_total'])

    def test_feature_flag_hides_explanations(self):
        result = build_breakdown([{'type': 'advisory_fee', 'amount': '1'}], glossary={}, show_explanations=False)
        self.assertIsNone(result['lines'][0]['explanation'])
        self.assertEqual(result['lines'][0]['wording_status'], 'hidden')

if __name__ == '__main__':
    unittest.main()
