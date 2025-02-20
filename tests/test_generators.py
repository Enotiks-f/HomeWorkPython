import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# Тест filter_by_currency


@pytest.fixture()
def list_tran():
    return [
        {"id": 1, "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}}},
        {"id": 2, "operationAmount": {"amount": "500.00", "currency": {"name": "RUB", "code": "RUB"}}},
        {"id": 3, "operationAmount": {"amount": "250.00", "currency": {"name": "USD", "code": "USD"}}},
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


@pytest.fixture()
def list_tran2():
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод с карты на карту"},
        {"id": 3, "description": None},
        {"id": 4, "description": ""},
        {"id": 5, "description": "Перевод со счета на счет"},
        {"id": 3},
    ]


def test_transaction_descriptions(list_tran2):
    """Тест"""
    res = list(transaction_descriptions(list_tran2))
    assert res == ["Перевод организации", "Перевод с карты на карту", "Перевод со счета на счет"]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (1, 1, ["0000 0000 0000 0001"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    res = list(card_number_generator(start, stop))
    assert res == expected
