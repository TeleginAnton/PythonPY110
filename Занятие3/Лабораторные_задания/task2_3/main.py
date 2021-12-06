import json


def task():
    filename = "input.json"
    with open(filename, 'r') as f:  # TODO считать содержимое JSON файла
        json_res = json.load(f)
    return max(json_res, key=lambda i: i["score"])  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
