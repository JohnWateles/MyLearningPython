#include <stdio.h>
#include <math.h>


unsigned long long int c_fib(int number) {
    unsigned long long int result = (pow((1 + sqrt(5)) / 2, number) - pow((1 - sqrt(5)) / 2, number)) / 2;
    return result;
}
