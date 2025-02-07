import random

def generate_and_check_number():
    """
    Генерирует четырехзначное число и проверяет наличие одинаковых цифр.

    Returns:
        Кортеж: (сгенерированное число, True если есть одинаковые цифры, False иначе).
        Возвращает None, если сгенерировано не четырехзначное число.
    """
    number = random.randint(1000, 9999)
    
    # Преобразование числа в строку для удобства проверки
    number_str = str(number)
    
    # Проверка на одинаковые цифры
    if len(set(number_str)) < 4:  # Если длина множества цифр меньше 4, значит есть повторы
        return number, True
    else:
        return number, False


if __name__ == "__main__":
    number, has_duplicates = generate_and_check_number()
    
    if number is not None:
        print(f"Сгенерированное число: {number}")
        if has_duplicates:
            print("В числе есть одинаковые цифры.")
        else:
            print("В числе нет одинаковых цифр.")
    else:
        print("Ошибка генерации числа.")

