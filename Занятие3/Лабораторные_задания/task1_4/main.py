INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE) as f:  # TODO перезаписать содержимое одного файла в другой
        with open(OUTPUT_FILE, 'w') as fn:
            for i in f:
                fn.write(i.upper())


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
