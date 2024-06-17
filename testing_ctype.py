from time import perf_counter
from fib import fib
import ctypes


def main():
    lib1 = ctypes.CDLL("test_ctypes/c_fib.so")

    timer = perf_counter()
    a = lib1.c_fib(19)
    print((perf_counter() - timer) * 100)

    timer = perf_counter()
    b = fib(19)
    print((perf_counter() - timer) * 100)

    print(a)
    print(b)


if __name__ == "__main__":
    main()
