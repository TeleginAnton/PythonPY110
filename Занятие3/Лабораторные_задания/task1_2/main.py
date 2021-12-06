OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, 'w') as f:  # записать лесенку в файл
        for star in range(1, 11):
            f.write(f"{star * '*':>10}\n")  # TODO эту строку списал :(


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
