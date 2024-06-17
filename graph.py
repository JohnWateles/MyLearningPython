# Оптимизация вычисления делителей числа

def divisions(number: int) -> list:
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


def main():
    print(divisions(1002451453241))


if __name__ == "__main__":
    main()
