def add_right_digit(d, k):
    """
    Добавляет цифру D справа к целому числу K.

    Args:
        d: Целое число от 0 до 9.
        k: Целое число (входное и выходное).

    Returns:
        Целое число K с добавленной справа цифрой D.
        Возвращает None, если d не находится в диапазоне 0-9.
    """
    if not 0 <= d <= 9:
        return None
    return k * 10 + d


if __name__ == "__main__":
    k = int(input("Введите целое число K: "))
    d1 = int(input("Введите цифру D1 (0-9): "))
    d2 = int(input("Введите цифру D2 (0-9): "))

    if 0 <= d1 <= 9 and 0 <= d2 <= 9:
        k = add_right_digit(d1, k)
        if k is not None:
            print(f"Результат после добавления {d1}: {k}")
            k = add_right_digit(d2, k)
            if k is not None:
                print(f"Результат после добавления {d2}: {k}")
            else:
                print("Ошибка: Некорректная цифра D2.")
        else:
            print("Ошибка: Некорректная цифра D1.")
    else:
        print("Ошибка: Некорректные цифры D1 или D2.")

