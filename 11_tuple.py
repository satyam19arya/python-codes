# A tuple is an immmutable data type in python
# Creating a tuple using ()
t=(1,2,3,4)
print(t[0])

t1=()  # Empty tuple
print(t1)

# t2=(1)  #wrong way to declare tuple with one element
t2=(1,)  #Tuple with one element
print(t2)

#cannot update the values of a tuple 
#t[0]=34   ->shows an error

t=(1,2,3,4,5,1,1,5)
print(t.count(1))

print(t.index(3))