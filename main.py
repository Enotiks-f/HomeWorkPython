# print(add(2, 5))
# print(multi(3, 7))

# from src.external_api import total_amount
# from src.utils import transactions
#
# transaction = transactions('data/operations.json')
# print(total_amount(transaction))
#
# # test masks
# from src.masks import get_mask_account, get_mask_card_number
#
# print(get_mask_account("7000792289606361"))
# print(get_mask_card_number("7000792289606361"))

from src.read_transaction import reading_csv, reading_xlsx
print(reading_csv("data/transactions.csv"), "\n")
print(reading_xlsx("data/transactions_excel.xlsx"))