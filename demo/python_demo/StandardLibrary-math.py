import math
from decimal import Decimal

print(math.ceil(2.5))
print(math.ceil(2))
print(math.floor(2.5))
print(math.floor(2))
print(math.fabs(2))
print(math.fabs(-20))

print(math.pi)
print(math.e)

print(math.sqrt(5))
print(math.sqrt(4))

print(0.1 + 0.2)
print(round(0.1 + 0.2, 2))
print(Decimal(0.1))
print(Decimal(0.2))
print(Decimal(0.1) + Decimal(0.2))
print((Decimal(0.1) + Decimal(0.2)) == Decimal(0.3))  # 要注意与下面表达式的区别
print((Decimal('0.1') + Decimal('0.2')) == Decimal('0.3'))
