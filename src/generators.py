from typing import Any, Dict, Generator, List


def filter_by_currency(transaction: List[Dict[str, Any]], currency: str = "USD") -> Generator[Dict[str, str]]:
    for i in transaction:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i


def transaction_descriptions(transaction: List[Dict[str, Any]]) -> Generator[str]:
    for i in transaction:
        description = i.get("description")
        if description:
            yield i["description"]


def card_number_generator(start: int, stop: int) -> Generator[str]:
    for num in range(start, stop + 1):
        formatted = f"{num:016d}"
        formatted = " ".join([formatted[i:i + 4] for i in range(0, 16, 4)])
        yield formatted
