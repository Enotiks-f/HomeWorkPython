import unittest
from src.analytics import filter_transaction, filter_description

class TestTransactionFilters(unittest.TestCase):
    def setUp(self):
        self.transactions = [
            {"description": "Оплата услуг связи"},
            {"description": "Покупка продуктов"},
            {"description": "Открытие вклада"},
            {"description": "Перевод организации"},
            {"note": "без описания"},  # случай, где description нет
        ]

    def test_filter_transaction_found(self):
        result = filter_transaction(self.transactions, "перевод")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["description"], "Перевод организации")

    def test_filter_transaction_not_found(self):
        result = filter_transaction(self.transactions, "машина")
        self.assertEqual(result, [])

    def test_filter_transaction_ignore_case(self):
        result = filter_transaction(self.transactions, "ПОКУПКА")
        self.assertEqual(len(result), 1)
        self.assertIn("Покупка продуктов", result[0]["description"])

    def test_filter_description_single_category(self):
        result = filter_description(self.transactions, ["вклада"])
        self.assertEqual(result, {"вклада": 1})

    def test_filter_description_multiple_categories(self):
        result = filter_description(self.transactions, ["услуг", "продуктов"])
        self.assertEqual(result, {"услуг": 1, "продуктов": 1})

    def test_filter_description_empty(self):
        result = filter_description([], ["что-нибудь"])
        self.assertEqual(result, {})

    def test_filter_description_missing_description(self):
        # one transaction without description, should be skipped
        result = filter_description(self.transactions, ["услуг", "вклада"])
        self.assertEqual(result, {"услуг": 1, "вклада": 1})

if __name__ == "__main__":
    unittest.main()
