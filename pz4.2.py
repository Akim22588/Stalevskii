def find_k_and_sum(n):
    """
    Находит наименьшее K, для которого сумма 1 + 2 + ... + K >= N, и саму сумму.

    Args:
        n: Целое число больше 1.

    Returns:
        Кортеж (K, сумма), где K - наименьшее целое число, удовлетворяющее условию,
        а сумма -  1 + 2 + ... + K. Возвращает None, если n <= 1.
    """
    if n <= 1:
        return None

    k = 0
    sum_k = 0
    while sum_k < n:
        k += 1
        sum_k = k * (k + 1) // 2  # Используем формулу для суммы арифметической прогрессии

    return k, sum_k


if __name__ == "__main__":
    n = int(input("Введите целое число N > 1: "))
    result = find_k_and_sum(n)
    if result:
        k, sum_k = result
        print(f"Наименьшее K: {k}")
        print(f"Сумма 1 + 2 + ... + {k}: {sum_k}")
    else:
        print("Некорректный ввод.")

