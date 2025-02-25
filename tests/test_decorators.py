import pytest
from src.decorators import log


@log()
def add(a, b):
    return a + b


def test_not_function():
    """Проверка, что декоратор не изменяет поведение функции."""
    assert add(5, 6) == 11


def test_log_console(capsys):
    """Проверка декоратора на вывод в консоль"""
    res = add(1, 1)

    captured = capsys.readouterr()
    assert "Функция add вызвана с args=(1, 1), kwargs={}" in captured.out
    assert res == 2


def test_log_file(tmp_path):
    """Проверка декоратора на запись в файл"""

    log_file = tmp_path / "log.txt"

    @log(filename=log_file)
    def multi(a, b):
        return a * b

    res = multi(2, 3)

    content = log_file.read_text(encoding="utf-8")  # Это должно читать файл
    assert "Функция multi вызвана с args=(2, 3), kwargs={}" in content
    assert res == 6


def test_log_error(capsys):
    "Проверка декоратора на логирование ошибок"

    @log()
    def devide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        devide(4, 0)

    captured = capsys.readouterr()
    assert "Ошибка в devide: ZeroDivisionError" in captured.out
