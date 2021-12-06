# TODO Домашка: Реализовать функцию enumerate с помощью zip

def list_zip(list_enter, key_):
    list_enter = list_enter.replace(' ', '')
    key_ = list(key_)
    for key_, list_enter in zip(key_, list_enter):  # можно ли привести к set?
        print(f'{key_}-{list_enter}', end=' ')
    return  # Не пойму, как избавится от None


def enumerate_(list_3):
    res = [print(i, end=' ') for i in enumerate(list_3, 1)]  # Как можно избавиться от (6, ' ')
    #  ругается на local variable 'res_' value is not used


if __name__ == "__main__":
    list_ = 'Hello world'
    list_1 = range(1, 100)
    print(list_zip(list_, list_1))

    print('*' * 10)

    list_2 = 'Hello world'
    print(enumerate_(list_2))

# 1-H 2-e 3-l 4-l 5-o 6-  7-w 8-o 9-r 10-l 11-d None
# **********
# (1, 'H') (2, 'e') (3, 'l') (4, 'l') (5, 'o') (6, ' ') (7, 'w') (8, 'o') (9, 'r') (10, 'l') (11, 'd') None
