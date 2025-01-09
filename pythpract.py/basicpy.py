print(34 + 7)
print(34.8 + 37.8)
print(34 + 78.8)
print(67 - 45.5)
print(56 * 3)
print(34 / 17)
print(34 // 5)  #it rounds down to the nearist whole number
print(9 // 2)
print(11 // 3)
print(3**3)   #exponets

print(15 % 3)   #15 divided by 3 remainder 0  (the output will be 0 because its only showing the remainder part of the answer)
print(16 % 3)   #16 divided by 3 remainder 1
print(17 % -7)
print(-17 % 7)

from math import remainder
print(int(remainder(14, 7)))
print(int(remainder(17, 7)))
print(int(remainder(17, -7)))
print(int(remainder(-17, 7)))
print(int(remainder(-17, -7)))

print(0.1 + 0.2 == 0.3)

import math
math.isclose(0.1 + 0.2, 0.3)

from decimal import Decimal
Decimal('0.1') + Decimal('0.2') == Decimal('0.3')

