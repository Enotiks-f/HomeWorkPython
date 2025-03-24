import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.getenv('API_KEY')


def convert(to, to_from, amount):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={to_from}&amount={amount}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    result = response.json()
    return result.get("result")


def total_amount(dict_transaction):
    count = 0
    for i in dict_transaction:
        try:
            if not isinstance(i, dict) or not i:
                continue

            if i["operationAmount"]["currency"]["code"] == "RUB":
                count += float(i["operationAmount"]["amount"])
            else:
                to_from = i["operationAmount"]["currency"]["code"]
                amount = float(i["operationAmount"]["amount"])

                converted = convert("RUB", to_from, amount)
                if converted is not None:
                    count += converted

        except (KeyError, TypeError, ValueError):
            continue
    return count
