Lists

>>> my_list = [1, 'xyz', True, [2, 3, 4]]
>>> my_list 
[1, 'xyz', True, [2, 3, 4]]

Tuple

>>> tup = ('xyz', [2, 3, 4], 1, True)
>>> tup
('xyz', [2, 3, 4], 1, True)

# Begin multi-line list literal
["Monty Python's Flying Circus",#begin multi-lined tuple literal ('Eric Idle', 'John Cleese', 'Terry Gilliam', 
 'Graham Chapman', 'Michael Palin', 'Terry Jones',),#end tuple ] #end list

>>> ["Monty Python's Flying Circus", ('Eric Idle', 'John Cleese', 'Terry Gilliam', 
...  'Graham Chapman', 'Michael Palin', 'Terry Jones',),]
["Monty Python's Flying Circus", ('Eric Idle', 'John Cleese', 'Terry Gilliam', 'Graham Chapman', 'Michael Palin', 'Terry Jones')]

>>> my_list = [1, 'xyz', True, [2, 3, 4]]
>>> my_list[0]
1

>>> my_list[1]
'xyz'

>>> my_list[2]
True

>>> my_list[3]
[2, 3, 4]

>>> my_list[4]
error

#"lists" are mutable "tuple" are not mutable

#If you want to use a literal to create a tuple with one element, you can't simply write:
>>> my_tuple = (1)
>>> print(type(my_tuple))
<class 'int'>

#the () treat the expression as a parenthesized expression, not a tuple literal. To define a 
# one-element tuple you must add a comma after the element value:
>>> my_tuple = (1,)
>>> print(type(my_tuple))
<class 'tuple'>

>>> tuple(range(5))
(0, 1, 2, 3, 4)

>>> tuple(range(5, 10))
(5, 6, 7, 8, 9)

list(range(1, 10, 2))
[1, 3, 5, 7, 9]

list(range(0, -5, -1))
[0, -1, -2, -3, -4]


>>> list(range(0, -5, -1))
[0, -1, -2, -3, -4]
>>> list(range(0, 10, 2))  
[0, 2, 4, 6, 8]
>>> list(range(0, 20, 2)) 
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> list(range(3, 21, 3)) 
[3, 6, 9, 12, 15, 18]
>>> my_range = range(0, 20, 5)
>>> my_range[2]
10
>>> list(range(3, 21, 7))      
[3, 10, 17]
>>> list(range(0, 21, 7)) 
[0, 7, 14]
>>>