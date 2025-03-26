import csv
import pandas as pd

def reading_csv(csv_file):
    transactions_list = []
    with open(csv_file, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions_list.append(row)
    return transactions_list


def reading_xlsx(xlsx_file):
    exel_data = pd.read_excel(xlsx_file)
    transactions_list = exel_data.to_dict(orient="records")

    return transactions_list