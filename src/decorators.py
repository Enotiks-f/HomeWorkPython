import functools


def log(filename=None):
    def decorators(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # логирование вызова функции
            log_entry = f"Функция {func.__name__} вызвана с args={args}, kwargs={kwargs}"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_entry + "\n" )
            else:
                print(log_entry)

            try:
                res = func(*args)
                log_entry = f"Функция {func.__name__} успешно выполнена, результат: {res}"
            except Exception as error:
                log_entry = f"Ошибка в {func.__name__}: {type(error).__name__}, args={args}, kwargs={kwargs}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_entry + "\n")
                else:
                    print(log_entry)

                raise

            log_entry = f"Функция {func.__name__} вызвана с args={args}, kwargs={kwargs}"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_entry + "\n" )

            return res

        return wrapper

    return decorators
