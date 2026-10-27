import unittest
from decimal import Decimal
from src.fee_breakdown import build_breakdown
from src.money import parse_amount, round_cents

class ValidationTests(unittest.TestCase):
    def test_invalid_amounts_rejected(self):
        for value in [1.2, 1, True, None, '', 'abc', '-0.01', 'NaN', 'Infinity', '1000000001', '0.0000001']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                build_breakdown([{'type': 'advisory_fee', 'amount': value}])

    def test_bad_fee_containers_rejected(self):
        for value in [None, {}, [], ['bad'], [{'type': 'unknown', 'amount': '1'}], [{'type': 'advisory_fee'}]]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                build_breakdown(value)

    def test_excessive_line_count_rejected(self):
        with self.assertRaises(ValueError):
            build_breakdown([{'type': 'advisory_fee', 'amount': '1'}] * 101)

    def test_shared_rounding_helper_uses_half_up(self):
        self.assertEqual(round_cents(parse_amount('0.005')), Decimal('0.01'))
        self.assertEqual(round_cents(parse_amount('12.345')), Decimal('12.35'))

    def test_maximum_amount_supported(self):
        self.assertEqual(build_breakdown([{'type': 'advisory_fee', 'amount': '1000000000'}])['total'], '1000000000.00')

if __name__ == '__main__':
    unittest.main()
