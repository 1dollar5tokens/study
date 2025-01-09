>>> d1 = {}                     # empty dict
>>> print(type(d1))
<class 'dict'>
>>> s1 = set()                  # empty set
>>> print(s1)
set()


#create a set from a literal
>>> s2 = {2, 3, 5, 7, 11, 13} 
>>> print(s2)
{2, 3, 5, 7, 11, 13}
>>> s3 = set("hello there!")
>>> 


#create a set from a string
>>> s3
{'e', ' ', '!', 'h', 'l', 't', 'r', 'o'}


>>> monty_python_cast = {'Eric Idle', 'John Cleese', 'Terry Gilliam', 'Graham Chapman', 'Michael Palin', 'Terry Jones'}
>>> monty_python_cast
{'Michael Palin', 'Eric Idle', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Graham Chapman'}
>>>

>>> s5 = frozenset([1, 2, 3])
>>> print(s5)
frozenset({1, 2, 3})
>>> s6 = frozenset((1, 2, 3))
>>> print(s6)
frozenset({1, 2, 3})
>>> s7 = ({1, 2, 3})
>>> s7
{1, 2, 3}
>>> s8 = frozenset(range(1, 4))
>>> s8
frozenset({1, 2, 3})
>>>