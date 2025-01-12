#not sure why it didnt work.  I also didnt expect it to work


print(isinstance('abc', str))
print(isinstance([], set))

class A:
    pass

class B(A):
    pass

b  = B()

print(type(b).__name__)
print(type(b) is B)
print(type(A) is A)
print(isinstance(b, B))
print(isinstance(b, A))