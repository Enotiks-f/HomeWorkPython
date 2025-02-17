import pytest

from src.generators import filter_by_currency, transaction_descriptions
from tests.test_processing import sample_transactions

# Тест filter_by_currency

@pytest.fixture()
def list_tran():
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "USD", "code": "USD"}
            }
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "500.00",
                "currency": {"name": "RUB", "code": "RUB"}
            }
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "250.00",
                "currency": {"name": "USD", "code": "USD"}
            }
        }
    ]

def test_filter_by_currency_usd(list_tran):
    """Тест USD"""
    result = list(filter_by_currency(list_tran, "USD"))
    assert len(result) == 2
    for tx in result:
        assert tx["operationAmount"]["currency"]["code"] == "USD"

def test_filter_by_currency_rub(list_tran):
    """Тест RUB"""
    result = list(filter_by_currency(list_tran, "RUB"))
    assert len(result) == 1
    for tx in result:
        assert tx["operationAmount"]["currency"]["code"] == "RUB"

def test_filter_by_currency_empty():
    """Тест без списка"""
    result = list(filter_by_currency([], "RUB"))
    assert result == []

# Тест transaction_descriptions

def test_transaction_descriptions():
    """Тест """
    pass