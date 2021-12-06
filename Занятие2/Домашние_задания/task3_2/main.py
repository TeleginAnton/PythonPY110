def test_int(fn):
    def wrapper(args):
        res = all([isinstance(i, int) for i in args])
        fn(res)
        print(args)
        return res

    return wrapper


@test_int
def chek_int(ar):
    print(ar)
    return


if __name__ == "__main__":
    test = 5, 6, 7
    test_2 = {"A": 5}
    test_3 = 15, 5, 25
    a = 1
    b = 2
    c = 3
    chek_int(test)
    pass
