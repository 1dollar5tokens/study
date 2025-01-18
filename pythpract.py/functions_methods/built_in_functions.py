print(min(-10, 5, 12, 0, -20))
print(max(-10, 5, 12, 0, -20))

print(min('over', 'the', 'moon'))
print(max('over', 'the', 'moon'))

#print(max(-10, '5', '12', '0', -20)) error  can't do (str) and (int)

my_tuple = ('i', 'tawt', 'i', 'taw', 'a', 'puddy', 'tat')
print(min(my_tuple))
print(max(my_tuple))

#ord and chr
# Given a single character, ord returns an integer that represents the Unicode code point of that character.
# For the standard ASCII character sets, the code points refer to the values of the characters in the standard ASCII character
# set. For example :

print(ord('a'))
print(ord('A'))
print(ord('='))
print(ord('~'))

#chr is the reverse of ord

print(chr(97))
print(chr(65))
print(chr(61))
print(chr(126))

collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(any(collection1))
print(any(collection2))
print(any(collection3))
print(any([]))

print(all(collection1))
print(all(collection2))
print(all(collection3))
print(all([]))

numbers = [2, 5, 8, 10, 13]
print([number % 2 == 0 for number in numbers])  #looking for even numbers
print(any([number % 2 == 0 for number in numbers]))  #looking for even numbers
print(all([number % 2 == 0 for number in numbers]))  #looking for even numbers

numbers =[5, 13]
print(any([number % 2 == 0 for number in numbers]))  #looking for even numbers
print(all([number % 2 == 0 for number in numbers]))  #looking for even numbers

numbers =[2, 8, 10]
print(any([number % 2 == 0 for number in numbers]))  #looking for even numbers
print(all([number % 2 == 0 for number in numbers]))  #looking for even numbers

