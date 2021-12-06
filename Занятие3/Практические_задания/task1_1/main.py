def task():
    filename = "input.txt"
    with open(filename) as f:  # менеджер контекста открывает файл в режиме чтения в текстовом формате "rt"
        for line in f:  # файл является итератором, который построчно возвращает свое содержимое
            line = line.strip()  # TODO c помощью метода строки strip очистить строку от непечатыемых символов
            print(line)  # или так print(line.strip())


if __name__ == "__main__":
    # try:
    #     file = open('input.txt')
    #     print(file.read())
    # except Exception:
    #     pass
    # finally:
    #     file.close()
    task()
