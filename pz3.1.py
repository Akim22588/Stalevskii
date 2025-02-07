def is_in_second_or_third_quadrant(x: float, y: float) -> bool:
    """
    Checks if a point (x, y) lies in the second or third quadrant.

    Args:
        x: The x-coordinate of the point.
        y: The y-coordinate of the point.

    Returns:
        True if the point is in the second or third quadrant, False otherwise.
    """
    if x < 0:
        if y > 0:
            return True  # Second quadrant
        elif y < 0:
            return True  # Third quadrant
        else:
            return False # x<0, y=0 - on the x-axis, not in a quadrant
    else:
        return False  # Point is not in second or third quadrant

# Примеры использования
print(is_in_second_or_third_quadrant(-1, 1))  # True (Second quadrant)
print(is_in_second_or_third_quadrant(-1, -1)) # True (Third quadrant)
print(is_in_second_or_third_quadrant(1, 1))   # False (First quadrant)
print(is_in_second_or_third_quadrant(1, -1))  # False (Fourth quadrant)
print(is_in_second_or_third_quadrant(-1, 0))  # False (On the x-axis)
print(is_in_second_or_third_quadrant(0, 1))   # False (On the y-axis)
print(is_in_second_or_third_quadrant(0,0))    # False (Origin)

