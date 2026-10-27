"""Shared money rules for the synthetic demo, not production accounting."""
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

CENT = Decimal('0.01')
MAX_AMOUNT = Decimal('1000000000')

def parse_amount(value):
    if not isinstance(value, str):
        raise ValueError('amount must be a decimal string, never a float')
    try:
        amount = Decimal(value)
    except InvalidOperation as exc:
        raise ValueError('invalid decimal amount') from exc
    if not amount.is_finite() or amount < 0 or amount > MAX_AMOUNT:
        raise ValueError('amount must be finite and between 0 and 1000000000')
    if amount.as_tuple().exponent < -6:
        raise ValueError('amount supports at most six decimal places')
    return amount

def round_cents(value):
    return value.quantize(CENT, rounding=ROUND_HALF_UP)
