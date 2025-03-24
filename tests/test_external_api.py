from unittest.mock import patch

from src.external_api import convert, total_amount


@patch("requests.get")
def test_convert(mock_get):
    mock_get.return_value.json.return_value = {"result": 100.0}

    result = convert("RUB", "USD", 1.0)

    mock_get.assert_called_once()

    assert result == 100.0


@patch("src.external_api.convert")
def test_total_amount(mock_convert):
    mock_convert.return_value = 100.0

    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}, "amount": "50.0"}},
        {"operationAmount": {"currency": {"code": "RUB"}, "amount": "30.0"}},
        {},
        {"operationAmount": {"currency": {"code": "EUR"}, "amount": "20.0"}}
    ]

    result = total_amount(transactions)

    assert mock_convert.call_count == 2

    assert result == 230.0


test_convert()
test_total_amount()
