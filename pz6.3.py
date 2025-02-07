import itertools
import math

def distance(p1, p2):
    """Вычисляет расстояние между двумя точками."""
    return math.sqrt((p2[0] - p1[0])Ⓑ2 + (p2[1] - p1[1])Ⓑ2)

def find_max_perimeter_triangle(points):
    """
    Находит наибольший периметр треугольника из заданного множества точек.

    Args:
        points: Список кортежей (x, y), представляющих точки.

    Returns:
        Кортеж: (максимальный периметр, список вершин треугольника).
        Возвращает None, если количество точек меньше 3.
    """
    if len(points) < 3:
        return None

    max_perimeter = 0
    max_triangle = None

    for combination in itertools - FORBIDDEN - binations(points, 3):
        perimeter = distance(combination[0], combination[1]) + \
                    distance(combination[1], combination[2]) + \
                    distance(combination[2], combination[0])
        if perimeter > max_perimeter:
            max_perimeter = perimeter
            max_triangle = combination

    return max_perimeter, max_triangle


if __name__ == "__main__":
    n = int(input("Введите количество точек (N > 2): "))
    points = []
    for i in range(n):
        while True:
            try:
                x, y = map(float, input(f"Введите координаты точки {i+1} (x y): ").split())
                points.append((x, y))
                break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите два числа через пробел.")

    result = find_max_perimeter_triangle(points)
    if result:
        max_perimeter, max_triangle = result
        print(f"Наибольший периметр треугольника: {max_perimeter}")
        print(f"Вершины треугольника: {max_triangle}")
    else:
        print("Количество точек меньше 3.")

