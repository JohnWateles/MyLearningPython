from decimal import Decimal, getcontext
getcontext().prec = 128


def pi_number(iterations: int):
    result = Decimal()
    for i in range(iterations):
        result += Decimal((1 / (16 ** i)) * ((4 / (8 * i + 1)) - (2 / (8 * i + 4))
                                             - (1 / (8 * i + 5)) - (1 / (8 * i + 6))))
    """
    Максимальная точность - 16 знаков после запятой
    """
    return result


if __name__ == "__main__":
    print(pi_number(15))
