def find_min_even_indexed(a):
    """
    Находит минимальный элемент в списке с четными индексами.

    Args:
        a: Список чисел.

    Returns:
        Минимальный элемент среди элементов с четными индексами.
        Возвращает None, если список пуст или содержит только один элемент.
    """
    if len(a) < 2:
        return None

    min_even = a[1]  # Начинаем с элемента с индексом 1 (второго элемента)
    for i in range(3, len(a), 2):  # Перебираем элементы с четными индексами, начиная с 3
        if a[i] < min_even:
            min_even = a[i]
    return min_even


if __name__ == "__main__":
    n = int(input("Введите размер списка: "))
    a = []
    for i in range(n):
        while True:
            try:
                num = int(input(f"Введите элемент {i+1}: "))
                a.append(num)
                break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите целое число.")

    min_element = find_min_even_indexed(a)

    if min_element is not None:
        print(f"Минимальный элемент с четным индексом: {min_element}")
    else:
        print("Список слишком короткий для поиска минимального элемента с четным индексом.")

