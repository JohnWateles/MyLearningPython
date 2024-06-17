from decimal import Decimal, getcontext
from sys import getsizeof

getcontext().prec = 1000

big_float = Decimal('1.2345678901234567890123456789012345678901234567890')

result = big_float / Decimal('1.1000000000000000000000000000000000000000000000001')

print(big_float)
print(result)
