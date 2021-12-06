def positive_check(fn):
    def wrapper(arg):
        if arg < 0:  # TODO написать проверку положительности аргумента arg
            raise ValueError("Аргумент функции не является положительным числом")
        result = fn(arg)
        return result

    return wrapper


@positive_check
def some_func(num: int):
    return num


if __name__ == "__main__":
    # print(some_func(5))  # всё хорошо

    print(some_func(-5))  # должна быть вызвана ошибка ValueError
