#figuring out data types

print(type(1))
print(type(13.14))
print(type(True))
print(type('abc'))
print(type([1, 2, 3]))
print(type(None))

foo = 42
print(type(foo))

#answers

>>> print(type(1))
<class 'int'>
>>> print(type(13.14))
<class 'float'>
>>> print(type(True))
<class 'bool'>
>>> print(type('abc'))
<class 'str'>
>>> print(type([1, 2, 3]))
<class 'list'>
>>> print(type(None))
<class 'NoneType'>
>>>
>>> foo = 42
>>> print(type(foo))
<class 'int'>
>>> 


print(type('abc').__name__)  #2 underscores together__ not _
print(type(False).__name__)
print(type([]).__name__)

>>> print(type('abc').__name__)
str
>>> print(type(False).__name__)
bool
>>> print(type([]).__name__)
list

print(type('abc') is str)       #its like a question.  answer is true
print(type('abc') is int)
print(type(False) is bool)
print(type([]) is list)
print(type([]) is set)

#answer

#>>> print(type('abc') is int)
#False
#>>> print(type(False) is bool)
#True
#>>> print(type([]) is list)
#True
#>>> print(type([]) is set)

print(isinstance('abc', str))
print(isinstance([], set))

#>>> print(isinstance('abc', str))
#True
#>>> print(isinstance([], set))
#False

 