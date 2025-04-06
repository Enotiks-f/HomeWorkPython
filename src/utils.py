import logging
import json
import os

logger = logging.getLogger("transaction")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_handler = logging.FileHandler("logs/utils.log", mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def transactions(json_file):
    if not os.path.isfile(json_file):
        logger.error("Файл не найден: %s")
        return []
    if os.path.getsize(json_file) == 0:
        logger.error("Файл пуст: %s")
        return []

    try:
        logger.debug("Запущенна функция открытия и чтения json.file: %s")
        with open(json_file, encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info("Функция успешно сработала")
                return data
            else:
                logger.warning("Функция успешно сработала, но в файле не найден LIST")
                return []

    except (json.JSONDecodeError, ValueError):
        logger.error("Ошибка чтения файла или неверный формат данных.")
        return []
