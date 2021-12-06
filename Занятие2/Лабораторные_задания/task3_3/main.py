def header_footer(a):  # TODO написать декоратор
    def wrapper():
        print('=' * 8)
        a()
        print('=' * 8)
    return wrapper


@header_footer
def my_func():
    print("Hello World")
    return my_func  # TODO тут?


if __name__ == "__main__":
    my_func()


# print(len('========'))
