print(int('6'))   #making number strings into integers  '6' to 6 
print(float(3.141592))   #or floats '3.141592' to 3.141592

print(str(5))
print(str(3.141592))

#unnexessary explicit coercion
print(str(3))
print(str(False))
print(str([1, 2, 3]))
print(str({4, 5, 6}))

#implicit coercion
print(3)
print(False)
print([1, 2, 3])
print({4, 5, 6})

print(True + True + True)      #True = 1
print(True + 1 + 1.0)
print(False * 5000)            #False = 0

