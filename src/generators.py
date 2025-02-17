from email.generator import Generator
from typing import Dict, List, Any, Generator

def filter_by_currency(transact: List[Dict[str, Any]], currency: str = "USD") -> Generator:
    for i in transact:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i

def transaction_descriptions(transact: List[Dict[str, Any]]) -> Generator:
    for i in transact:
        yield i["description"]


def card_number_generator(first: int, last: int) -> Generator:
    for num in range(first, last + 1):
        formatted = f"{num:016d}"
        formatted = ' '.join([formatted[i:i+4] for i in range(0, 16, 4)])
        yield formatted

