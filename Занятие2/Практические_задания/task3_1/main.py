def print_args(*args):
    print(type(args), args)


def print_kwargs(**kwargs):
    print(type(kwargs), kwargs)


def print_args_kwargs(*args, **kwargs):
    for index, arg in enumerate(args):
        print(f"Позиционный аргумент {index}: {arg}")

    for key, kwarg in kwargs.items():
        print(f"Именованный аргумент {key}: {kwarg}")


if __name__ == "__main__":
    # a = 100500
    # print_args(1, 2, 3, a)
    # print_kwargs(a=1, b=2, c=3)

    print_args_kwargs(1, 2, 3, a=1, b=2, c=3)
