import csv
import pandas as pd

def reading_csv(csv_file):
    """Функция чтения csv файлов"""
    with open(csv_file, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        return reader


def reading_xlsx(xlsx_file):
    """Функция чтения xlsx файлов"""
    exel_data = pd.read_excel(xlsx_file)
    transactions_list = exel_data.to_dict(orient="records")

    return transactions_list