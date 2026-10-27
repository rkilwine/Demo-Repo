'''Synthetic demo only. No client data, network calls, or money movement.'''
import argparse
import json
from decimal import Decimal
from pathlib import Path
from src.money import parse_amount, round_cents

ROOT = Path(__file__).resolve().parents[1]
FEE_TYPES = {'advisory_fee', 'fund_expense_ratio', 'transaction_fee'}

def load_glossary(path=None):
    with open(path or ROOT / 'config/fee_glossary.json', encoding='utf-8') as handle:
        return json.load(handle)

def build_breakdown(fees, glossary=None, show_explanations=True):
    if not isinstance(fees, list) or not fees or len(fees) > 100:
        raise ValueError('fees must be a list of 1 to 100 items')
    glossary = load_glossary() if glossary is None else glossary
    lines = []
    for fee in fees:
        if not isinstance(fee, dict) or fee.get('type') not in FEE_TYPES:
            raise ValueError('unsupported fee type')
        amount = parse_amount(fee.get('amount'))
        entry = glossary.get('entries', {}).get(fee['type'])
        if show_explanations and not entry:
            raise ValueError('missing glossary entry')
        lines.append({
            'type': fee['type'],
            'amount': format(round_cents(amount), '.2f'),
            'explanation': entry['explanation'] if show_explanations else None,
            'wording_status': entry['status'] if show_explanations else 'hidden',
        })
    # CU-868mnhw8a: total equals the rounded lines actually displayed.
    total = sum((Decimal(line['amount']) for line in lines), Decimal('0.00'))
    return {'synthetic': True, 'currency': 'USD', 'lines': lines, 'total': format(total, '.2f')}

def main():
    parser = argparse.ArgumentParser(description='Synthetic fee-breakdown demo')
    parser.add_argument('--data', type=Path, default=ROOT / 'data/accounts.json')
    parser.add_argument('--glossary', type=Path, default=ROOT / 'config/fee_glossary.json')
    parser.add_argument('--case', default='normal')
    parser.add_argument('--hide-explanations', action='store_true')
    args = parser.parse_args()
    try:
        accounts = json.loads(args.data.read_text(encoding='utf-8'))
        case = next(item for item in accounts['cases'] if item['id'] == args.case)
        result = build_breakdown(case['fees'], load_glossary(args.glossary), not args.hide_explanations)
    except (OSError, ValueError, KeyError, StopIteration) as exc:
        parser.exit(2, f'Invalid demo input: {exc}')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
