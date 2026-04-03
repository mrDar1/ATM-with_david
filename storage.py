import json
import datetime as dt
from models import Bank, Account


def save_data(bank) -> None:
    """take Bank object, convert to dict, write to 'data.json' """
    data = {}
    for account_id, account in bank._accounts.items():
        data[account_id] = {
            "id": account.id,
            "name": account.name,
            "pin": account.pin,
            "balance": account.balance,
            "is_blocked": account.is_blocked,
            "actions_log": account.actions_log_to_dictionary()
        }
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_data() -> Bank:
    """read from 'data.json', convert to Dict, than convert to Bank object, and return it
    if there is no file, return a new Bank object with empty accounts"""
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    bank = Bank()
    for account_id_str, account_data in data.items():
        account_id = int(account_id_str)
        account = Account(name=account_data["name"], balance=account_data["balance"], id=account_id)
        account.pin = account_data["pin"]
        account.is_blocked = account_data["is_blocked"]
        account.actions_log = [
            {
                "time": dt.datetime.fromisoformat(action["time"]),
                "amount": action["amount"],
                "type": action["type"],
                "counterparty": action["counterparty"]
            }
            for action in account_data["actions_log"].values()
        ]
        bank._accounts[account_id] = account

    return bank
