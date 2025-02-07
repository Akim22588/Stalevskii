def get_season(month):
    """
    Определяет время года по номеру месяца.

    Args:
        month: Целое число от 1 до 12, представляющее номер месяца.

    Returns:
        Строка, представляющая время года ("зима", "весна", "лето" или "осень").
        Возвращает None, если month не находится в диапазоне 1-12.
    """

    if not 1 <= month <= 12:
        return None

    if month in (12, 1, 2):
        return "зима"
    elif month in (3, 4, 5):
        return "весна"
    elif month in (6, 7, 8):
        return "лето"
    elif month in (9, 10, 11):
        return "осень"


if __name__ == "__main__":
    month_number = int(input("Введите номер месяца (1-12): "))
    season = get_season(month_number)

    if season:
        print(f"Время года для месяца {month_number}: {season}")
    else:
        print("Некорректный номер месяца.")

