def fib(index: int) -> int:
    """
    :param index:
    :return: The Fibonacci number under the index
    """
    if isinstance(index, int) and index >= 0:
        return int((((1 + 5 ** 0.5) / 2) ** index - ((1 - 5 ** 0.5) / 2) ** index) / 2)
    elif not (isinstance(index, int)):
        raise TypeError("Index must be an integer value!")
    else:
        raise ValueError("Index must be >= 0!")
