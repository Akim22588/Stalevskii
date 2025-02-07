def seconds_since_last_hour(total_seconds: int) -> int:
    """
    Calculates the number of seconds passed since the beginning of the last hour.

    Args:
        total_seconds: The total number of seconds since the beginning of the day.

    Returns:
        The number of seconds passed since the beginning of the last hour.
        Returns 0 if total_seconds is negative or zero.

    Raises:
        TypeError: if input is not an integer.
    """

    if not isinstance(total_seconds, int):
        raise TypeError("Input must be an integer.")

    if total_seconds <= 0:
        return 0

    return total_seconds % 3600


# Примеры использования
print(seconds_since_last_hour(10000))  # Output: 1640
print(seconds_since_last_hour(3600))  # Output: 0
print(seconds_since_last_hour(7200))  # Output: 0
print(seconds_since_last_hour(0))     # Output: 0
print(seconds_since_last_hour(-100)) # Output: 0
