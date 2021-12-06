INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE) as file:  #  открыть указатель на файл
        for print_ in file:  #  файл является итератором, который работает с циклом for в построчном режиме
            print(print_, end='')
# todo Андрей Александрович, почему тут и в других примерах нет return?

if __name__ == "__main__":
    task()


for i in range(0, 11):
    for star in range(i):
        print(f"{'*', end='')
    print()
