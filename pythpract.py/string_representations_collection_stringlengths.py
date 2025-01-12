my_str = 'abc'
print(my_str)
print(str(my_str))
print(repr(my_str))

#answers

>>> my_str = 'abc'
>>> print(my_str)
abc
>>> print(str(my_str))
abc
>>> print(repr(my_str))
'abc'

#All built-in collection types (strings, sequences, mappings, and sets) have lengths.  
# The length of a string is the number of characters in the string, while the length 
# of other collections is the number of elements in the collection.  
# You can easily determine the length of a collection using the (len) function:


print(len('Launch School'))
print(len(range(5, 15)))
print(len(range(5, 15, 3)))
print(len(['a', 'b', 'c']))
print(len(('d', 'e', 'f', 'g')))
print(len({'foo': 42, 'bar': 7}))
print(len({'foo', 'bar', 'qux'}))

#answers

>>> print(len('Launch School'))
13
>>> print(len(range(5, 15)))
10
>>> print(len(range(5, 15, 3)))
4
>>> print(len(['a', 'b', 'c']))
3
>>> print(len(('d', 'e', 'f', 'g')))
4
>>> print(len({'foo': 42, 'bar': 7}))
2
>>> print(len({'foo', 'bar', 'qux'}))
3
>>>