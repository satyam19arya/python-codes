# Create a class C 2d vector and use it to create another class representing a 3d vector
class C2dVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def __str__(self):
        return f"{self.i}i + {self.j}k"

class C3dVector(C2dVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"


v2=C2dVector(1,3)
v3=C3dVector(1,9,7)
print(v2.__str__())
print(v3.__str__())


print("\n")
# Create a class pets from a class Animals and further create class og from pets. Add a method bark to class Dog      
class Animal:
    pass

class Pets:
    pass

class Dog:
    def bark(self):
        print("Bow Bow")

d=Dog()
d.bark()


print("\n")
# Create a class Employee and add salary increment properties to it. Write a method salary after increment method with a @property decorator
# with a setter which changes the value of increment based on the salary
class Employee:

    salary=55000
    salaryIncrement=2000
    # newSalary=57000

    @property
    def newSalary(self):
        return self.salary+self.salaryIncrement

e=Employee()
print(e.newSalary)


print("\n")
# Complex numbers
class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imag=i

    def __add__(self,c):
        return Complex(self.real+c.real, self.imag+c.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1=Complex(1,4)
c2=Complex(8,5)
print(c1+c2)


print("\n")
# Write a class vector representing a vector of n dimension.
# Overload the + and * operator which calculates the sum and the dot product of them
class vector:
     def __init__(self,vec):
         self.vec=vec
