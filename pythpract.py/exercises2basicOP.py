>>> number = 4936
>>> ones = number % 10
>>> ones
6
>>> number = number // 10
>>> tens = number % 10
>>> tens
3
>>> number = number // 10
>>> hundreds = number % 10
>>> hundreds
9
>>> thousands = number // 10
>>> thousands
4
>>>


print('5' + '10') #this is two strings  it could be 'toilet' + 'bowl' and it will be toiletbowl
510

print('toilet' + 'bowl')
toiletbowl

print(5 + 10)
15

#using coercion to add '5' + '10' 
print(int('5') + int('10')) 
15

foo = ['a', 'b', 'c']
print(foo[3]) #this will result in a error. There is not a 3's place  0=a 1=b 2=c

'foo' == 'Foo'   #False

int('3.1415') # error  this is a float not an int

'12' < '9' # True.  this would be look at like .12 < .90

12 < 9 #False.  this would be the number 12 is less than the number 9