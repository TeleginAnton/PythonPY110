from itertools import count


def count_(stat=0, step=1) -> int:
    stat = count
    while True:
        yield count
        stat += step ** 2
        print(count)


if __name__ == "__main__":
    # start = 0
    # step = 2
    # test = (start + step ** i for i in count())
    # print(next(test))
    a = count_()
    print(a)

