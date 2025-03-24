import json
import os


def transactions(json_file):

    if not os.path.isfile(json_file):
        return []
    if os.path.getsize(json_file) == 0:
        return []

    try:
        with open(json_file, encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []

    except (json.JSONDecodeError, ValueError):
        print("Ошибка чтения файла или неверный формат данных.")
        return []
