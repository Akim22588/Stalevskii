def copy_even_numbers(a):
    """
    Копирует четные числа из списка A в новый список B.

    Args:
        a: Исходный целочисленный список.

    Returns:
        Кортеж: (размер списка B, список B).
    """
    b = [num for num in a if num % 2 == 0]
    return len(b), b


if __name__ == "__main__":
    n = int(input("Введите размер списка A: "))
    a = []
    for i in range(n):
        while True:
            try:
                num = int(input(f"Введите элемент {i + 1}: "))
                a.append(num)
                break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите целое число.")

    size_b, b = copy_even_numbers(a)
    print(f"Размер списка B: {size_b}")
    print(f"Список B: {b}")

