def pow_gen(base: int):
    x = 0  # TODO записать функцию-генератор
    while True:
        res = x * 2
        yield base ** res
        x += 1


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
