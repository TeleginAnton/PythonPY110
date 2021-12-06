def task() -> str:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return min(list_words, key=min)  # Андрей Александрович, так(min) корректно?


if __name__ == "__main__":
    print(task())
