name = 'Jane'
print(f'good morning, {name}!')

print(
    
    {'a': 1,
     'b': 42,
     'c': 'string',
     'd': [5, 6],
     'e': {8, 9, 10}
    }
)

import time
print(time.asctime())

print(1, 2, 3, 'a', 'b', 'c')
print(
    [1, 2, 3],
    4,
    False,
    {5, 6, 7, 8},
)

print(1, 2, 3, 'a', 'b', sep=',')
print('a', 'b', 'c', 'd', 'e', sep='')

print(1, 2, 'a', 'b', sep=',', end=',-\n')
print('a', 'b', end='', sep=','); print('c', 'd', sep=',')
print(1, 2, sep='', end=','); print(4, 5, sep='', end='ehr')
print()