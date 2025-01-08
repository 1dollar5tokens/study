#examples of integer literals

1
2
-3
234891234
131_587_465_014_410_491

#Examples of float literals

1.0
1.4142
-3.14159
42348.912346
131_587_465.014_410_491

import sys

# The maximum number of digits that can be accurately
# presented
print(sys.float_info.dig)       # Typically 15

# The largest possible positive float value
print(sys.float_info.max)       # About 1.8 * (10**308)

# The smallest non-zero positive float value
print(sys.float_info.min)       # About 2.2 * (10**-308)

print(3.14 * (10**20))          # 3.14e+20
print(3.14 * (10**-20))         # 3.14e-20

print(3.14e+20 / 2.72e-15)      # 1.1544117647058823e+35

print(3 * (10**20))             # 300000000000000000000

print(int(3e+20))               # 300000000000000000000
