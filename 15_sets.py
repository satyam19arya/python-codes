# Set is a collection of non-repetitive elements 
a={1,2,3,4,5,2}
print(a)


# This syntax will create an empty dictionary and not an empty set
a={}
print(type(a))

# An empty set can be created using the below syntax:
b=set()
print(type(b))

b.add(4)
b.add(5)
b.add(3)
b.add(3)
print(b)
print(len(b))
b.remove(5)
print(b)
b.pop()