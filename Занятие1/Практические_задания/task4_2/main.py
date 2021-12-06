from itertools import count


def task():
    iterator_numbers = count(1, 1)
    # filter(lambda i: i % 2 == 0, iterator_numbers)  # сборка кода
    # map(lambda i: i ** 2, iterator_numbers)
    numbers = map(lambda i: i ** 2, filter(lambda i: i % 2 == 0, iterator_numbers))

    # numbers = (i ** 2 for i in iterator_numbers if i % 2 == 0)  # TODO заменить на map и filter

    for _ in range(10):  # TODO напечатать первые 10 чисел
        print(next(numbers))  # TODO с помощью next получать следующий элемент от итератора


if __name__ == "__main__":
    task()
