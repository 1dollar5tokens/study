print(42 < 41)
print(42 < 42)
print(42 <= 42)
print(42 < 43)

print('abcdf' < 'abcef')
print('abc' < 'abcef')
print('abcdef' < 'abc')
print('abc' < 'abc')
print('abc' <= 'abc')
print('A' < 'a')
print('Z' < 'a')

#ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz  alphabetically A is less than a

print('3' < '24')
print('24' < '3')

#when the numbers are in a string '' it acts like the library system or how 
# decimals works .3 is bigger than .24

print(42 > 41)
print(42 > 42)
print(42 >= 42)
print(42 > 43)

print('abcdf' > 'abcef')
print('abc' > 'abcef')
print('abcdef' > 'abc')
print('abc' > 'abc')
print('abc' >= 'abc')
print('A' > 'a')
print('Z' > 'a')

print('3' > '24')
print('24' > '3')


print({3, 1, 2} < {2, 4, 3, 1})
print({3, 1, 2} > {2, 4, 3, 1})
print({2, 4, 3, 1} >{3, 1, 2})

print([1, 2, 3] < [1, 2, 3, 4])
print([1, 4, 3] < [1, 3, 3])
print([1, 3, 3] < [1, 4, 3])