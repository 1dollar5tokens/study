answer = 41
print(answer)
41

answer = 42
print(answer)
42


#illegal name but will work with python because it doesnt recognize it as an error
first,last = ['mary', 'wonder']

>>> first,last = ['mary', 'wonder']
>>> first
'mary'
>>> last
'wonder'
>>>first_last = ('mary', 'wonder')

#varible done right
>>> first_last = ('mary', 'wonder')
>>> first_last
('mary', 'wonder')

forename = 'clare'
forename
'clare'

forename = 'victor'
forename
'victor'

left_side = 5
right_side = 32
total = left_side + right_side
print(total)
37

def square(number):
    return number * number

forty_two_squared = square(42)
print(forty_two_squared)
1764

foo = 42
foo = foo - 2

>>> foo = 42
>>> foo = foo - 2
>>> foo
40
>>> foo = foo * 2
>>> foo = foo + 8
>>> foo = foo + 12
>>> foo = foo // 5
>>> foo
20
>>> foo = foo / 5
>>> foo
4.0
>>> foo = foo**3
>>> print(foo)
64.0
>>>


foo = 42
foo -= 2
foo *= 2
foo += 8
foo += 12
foo //= 5
foo /= 5
foo **= 3
print(foo)
64

bar = 'xyz'
bar += 'abc'
bar *= 2
print(bar)

>>> bar = 'xyz'
>>> bar += 'abc'
'xyzabc'
>>> bar *= 2
'xyzabcxyzabc'
>>> print(bar)
xyzabcxyzabc
>>>

bar = [1, 2, 3]
bar += [4, 5]
print(bar)
[1, 2, 3, 4, 5]

bar = {1, 2, 3}
bar |= {2, 3, 4, 5}
bar -= {2, 4}
print(bar)


#this will be an error
def foo(bar):
    print(bar)
    
a = 3
foo(a *= 2)

#this wont work either
def foo():
    a = 3
    return a *= 2
num = 3
my_list = [1, 2, 3]
my_dict = {
    'a': 1,
    'b': 2,
}
