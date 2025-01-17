#my answer

# a = 1.05
# balence = (1000 * a)
# print(balence)
# balence2 = (balence * a)
# print(balence2)
# balence3 = (balence2 * a)
# print(balence3)
# balence4 = (balence3 * a)
# print(balence4)
# balence5 = (balence4 * a)
# print(balence5)

#book answer  again i made it to complicated

balence = 1000
balence *= 1.05
balence *= 1.05
balence *= 1.05
balence *= 1.05
balence *= 1.05
print(balence)

#reassignment, mutation, or neither

obj = 'ABcd'            #reassignment
obj.upper()             #neither
obj = obj.lower()       #reassignment
print(len(obj))         #neither
obj = list(obj)         #reassignment
obj.pop()               #mutation           I thought it was neither
obj[2] = 'X'            #mutation
obj.sort()              #mutation           This one too
set(obj)                #neither
obj = tuple(obj)        #reassignment
