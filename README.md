# Обработка транзакций

## Описание
"Обработка транзакций" - это Python-приложение для фильтрации и сортировки финансовых транзакций.

## Установка
1. Клонируйте репозиторий:
git clone https: https://github.com/Enotiks-f/HomeWorkPython
2. Установите зависимости:
pip install -r requirements.txt
## Использование:

1. Импортируйте функции в ваш Python-код.

2. Используйте filter_by_state() для фильтрации транзакций по статусу.

3. Используйте sort_by_date() для сортировки транзакций по дате.

4. Функция card_number_generator(start, stop) создаёт номера карт в формате XXXX XXXX XXXX XXXX.

5. Функция filter_by_currency(transactions, currency) возвращает только транзакции с указанной валютой.

6. Функция transaction_descriptions(transactions) извлекает description из всех транзакций.

## Тестирование

Проект включает тесты для проверки корректности работы функций. Тесты находятся в каталоге tests/ и используют pytest.

# Запуск тестов:

Убедитесь, что pytest установлен:

    pip install pytest

Запустите тесты командой:

    pytest -v