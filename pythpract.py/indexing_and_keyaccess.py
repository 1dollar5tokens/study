my_str = "abc"
print(my_str[0])
print(my_str[1])
print(my_str[2])
print(my_str[3])

my_range = range(5, 8)
print(my_range[0])
print(my_range[1])
print(my_range[2])
print(my_range[3])

my_list = [4, 5, 6]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

tup = (8, 9, 10)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

#answers

>>> my_str = "abc"
>>> print(my_str[0])
a
>>> print(my_str[1])
b
>>> print(my_str[2])
c
>>> print(my_str[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>>
>>> my_range = range(5, 8)
>>> print(my_range[0])
5
>>> print(my_range[1])
6
>>> print(my_range[2])
7
>>> print(my_range[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: range object index out of range
>>>
>>> my_list = [4, 5, 6]
>>> print(my_list[0])
4
>>> print(my_list[1])
5
>>> print(my_list[2])
6
>>> print(my_list[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
>>> tup = (8, 9, 10)
>>> print(tup[0])
8
>>> print(tup[1])
9
>>> print(tup[2])
10
>>> print(tup[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>>



my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['a'])
print(my_dict['b'])
print(my_dict['c'])
print(my_dict['d'])

#answers

>>> my_dict = {'a': 1, 'b': 2, 'c': 3}
>>> print(my_dict['a'])
1
>>> print(my_dict['b'])
2
>>> print(my_dict['c'])
3
>>> print(my_dict['d'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'd'
>>>

my_list = [1, 2, 3, 4]
my_list[2] = 6
print(my_list)
my_list[4] = 10

#answer

>>> my_list = [1, 2, 3, 4]
>>> my_list[2] = 6
>>> print(my_list)
[1, 2, 6, 4]
>>> my_list[4] = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>>

my_dict = {
    'dog': 'barks',
    'cat': 'meows',
    'pig': 'oinks',
}

my_dict['pig'] = 'snorts'
print(my_dict)

my_dict['fish'] = 'glub glub'
print(my_dict)

#answer

>>> my_dict = {
...     'dog': 'barks',
...     'cat': 'meows',
...     'pig': 'oinks',
... }
>>>
>>> my_dict['pig'] = 'snorts'
>>> print(my_dict)
{'dog': 'barks', 'cat': 'meows', 'pig': 'snorts'}
>>>
>>> my_dict['fish'] = 'glub glub'
>>> print(my_dict)
{'dog': 'barks', 'cat': 'meows', 'pig': 'snorts', 'fish': 'glub glub'}