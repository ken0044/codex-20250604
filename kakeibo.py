import argparse
import json
import os
from datetime import datetime

DATA_FILE = 'kakeibo.json'


def load_records():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_records(records):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def add_record(args):
    records = load_records()
    record = {
        'date': datetime.now().isoformat(timespec='seconds'),
        'type': args.type,
        'category': args.category,
        'description': args.description,
        'amount': args.amount,
    }
    records.append(record)
    save_records(records)
    print('Record added.')


def list_records(args):
    records = load_records()
    if not records:
        print('No records found.')
        return
    for r in records:
        print(f"{r['date']} | {r['type']} | {r['category']} | {r['description']} | {r['amount']}")


def show_balance(args):
    records = load_records()
    income = sum(r['amount'] for r in records if r['type'] == 'income')
    expense = sum(r['amount'] for r in records if r['type'] == 'expense')
    balance = income - expense
    print(f"Income: {income}")
    print(f"Expense: {expense}")
    print(f"Balance: {balance}")


def parse_args():
    parser = argparse.ArgumentParser(description='Simple Kakeibo (household ledger)')
    subparsers = parser.add_subparsers(dest='command')

    add_p = subparsers.add_parser('add', help='Add a record')
    add_p.add_argument('-t', '--type', choices=['income', 'expense'], required=True, help='Record type')
    add_p.add_argument('-a', '--amount', type=float, required=True, help='Amount')
    add_p.add_argument('-c', '--category', default='', help='Category')
    add_p.add_argument('-d', '--description', default='', help='Description')
    add_p.set_defaults(func=add_record)

    list_p = subparsers.add_parser('list', help='List records')
    list_p.set_defaults(func=list_records)

    bal_p = subparsers.add_parser('balance', help='Show balance summary')
    bal_p.set_defaults(func=show_balance)

    return parser.parse_args()


def main():
    args = parse_args()
    if not hasattr(args, 'func'):
        print('No command given. Use -h for help.')
        return
    args.func(args)


if __name__ == '__main__':
    main()
