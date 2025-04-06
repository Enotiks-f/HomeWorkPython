import csv
import pandas as pd
from unittest.mock import mock_open, patch
import pytest

def reading_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def reading_xlsx(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')

@pytest.fixture
def mock_csv_data():
    return "name,age\nJohn,30\nDoe,25"

@pytest.fixture
def mock_xlsx_data():
    return pd.DataFrame([{"name": "John", "age": 30}, {"name": "Doe", "age": 25}])

def test_reading_csv(mock_csv_data):
    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        with patch("csv.DictReader", return_value=[{"name": "John", "age": "30"}, {"name": "Doe", "age": "25"}]):
            result = reading_csv("dummy.csv")
            expected = [{"name": "John", "age": "30"}, {"name": "Doe", "age": "25"}]
            assert result == expected

def test_reading_xlsx(mock_xlsx_data):
    with patch("pandas.read_excel", return_value=mock_xlsx_data):
        result = reading_xlsx("dummy.xlsx")
        expected = [{"name": "John", "age": 30}, {"name": "Doe", "age": 25}]
        assert result == expected
