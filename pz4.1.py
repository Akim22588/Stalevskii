def sum_harmonic_series(n):
    """
    Вычисляет сумму гармонического ряда 1 + 1/2 + 1/3 + ... + 1/N.

    Args:
        n: Целое положительное число.

    Returns:
        Сумма гармонического ряда.  Возвращает None, если n <= 0.
    """
    if n <= 0:
        return None
    total = 0
    for i in range(1, n + 1):
        total += 1 / i
    return total


if __name__ == "__main__":
    n = int(input("Введите целое положительное число N: "))
    result = sum_harmonic_series(n)
    if result is not None:
        print(f"Сумма гармонического ряда до {n}: {result}")
    else:
        print("Некорректный ввод.")

