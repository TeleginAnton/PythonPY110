def min_len_check(fn):
    def wrapper(arg):  # TODO записать обертку для исходной функции
        len_min = 10
        if len(arg) < len_min:
            raise ValueError("Строка слишком короткая")
        res = fn(arg)
        return res
    return wrapper


@min_len_check  # TODO задекорировать функцию
def some_func(str_arg: str):
    return str_arg


if __name__ == "__main__":
    # print(some_func("Hello, World!!!"))  # всё хорошо

    print(some_func("Short str"))  # ValueError("Строка слишком короткая")
