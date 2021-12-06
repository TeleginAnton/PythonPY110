import string   # todo Написать бесконечный генератор случайных паролей заданной длины n (по умолчанию 8 символов)...
import random
from string import ascii_lowercase, ascii_uppercase, digits


def password(*pas):
    while True:
        password_len = 8
        res = [random.sample(i, password_len) for i in pas]
        print(res)

        # return  # Правильно я понимаю, если закрыть функцию, цикл становиться законченным?
        # По крайне мере PyCharm отрабатывает только одну строку)


if __name__ == "__main__":
    password_generator = string.ascii_lowercase + digits + ascii_uppercase
    print(ascii_lowercase)
    print(ascii_uppercase)
    print(digits)
    password(password_generator)
