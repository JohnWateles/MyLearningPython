def divisions(number: int) -> list:
    """
    :param number:
    :return: Sorted list with number divisors
    """
    if isinstance(number, int):
        number = abs(number)
        result = set()
        for divisor in range(1, int(number ** 0.5) + 1):
            if number % divisor == 0:
                result.add(divisor)
                result.add(number // divisor)
        return sorted(result)
    else:
        raise ValueError("Value must be an integer!")
