'Hello!'
"He's pining for the fjord!"
'1969-07-20'

greeting = 'hello'
for letter in greeting:
    print(letter)
# h
# e
# l
# l
# o

'Hi, there'                     # single quotes
"Monty Python's Flying Circus"  # Double quotes

# Triple quotes
'''King Arthur: "what is your name?"
Black Knight: "None shall pass!"
King Authur: "What is your quest?"
Black Knight: "I have no quarrel with you, but I must cross this bridge."
'''

# Triple double quotes
"""Man: "Is this the right room for an argurment?"
Other Man: "I've told you once."
Man: No you haven't!"
"""
print("""My nickname is "wolfy". What's yours?""")
print('My nickname is "wolfy". What\'s yours?')
print("My mickname is \"Wolfy\". What's yours?")

print("C:\\Users\\Xyzzy")   # Each \\ produces a literal \
    
>>> my_str = 'abc'
>>> my_str[0]
a

>>> my_str[1]
b

>>> my-str[2]
c

>>> my_str[4]
indexError: string index out of range


>>> my_str = 'abc'
>>> my_str[-1]
c

>>> my_str[-2]
b

>>> my-str[-3]
a

>>> my_str[-4]
indexError: string index out of range

# Both of these print C:\Users\Xyzzy
print("C:\\Users\\Xyzzy")   #Each \\ produces a literal \
print(r"C:\Users\Xyzzy")    # raw string literal

>>> f'5 + 5 equals {5 + 5}.'
'5 + 5 equals 10.'

>>> my_name = 'willardth'
>>> f'My name is {my_name}.'
'My name is willardth.'

>>> my_name = 'Willardth'
>>> greeting = 'ey up?'
>>> f'{greeting} My name is {my_name}.'
'ey up? My name is Willardth.'
>>> f'{greeting} My name is {my_name}'  
'ey up? My name is Willardth

f'Blah {expression} blah.'

>>> foo = 'hello'
>>> print(f'Use {{foo}} to embed a string: {foo}.')
Use {foo} to embed a string: hello.

>>> print(f'{123456789:_}')
123_456_789
>>> print(f'{123456789:,}') 
123,456,789

>>> print(f'{123456789:_}')
123_456_789
>>> print(f'{123456789:,}') 
123,456,789
>>> print(f'{123456.7890123:_}')
123_456.7890123
>>> print(f'{123456.78901234:,}')
123,456.78901234

