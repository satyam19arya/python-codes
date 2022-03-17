#
class Employee:
    company ="Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    languages ="python"

    def getLanguages(self):
        print(f"The language is {self.language}")

e=Employee()
p=Programmer()
e.showDetails()
p.showDetails()


print("\n")
#
class Employee:
    company ="Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    languages ="python"

    def getLanguages(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is an programmme")

e=Employee()
p=Programmer()
e.showDetails()
p.showDetails()


print("\n")
# Multiple inheritance
class  Employee:
    company ="Google"
    eCode=120

class FreeLance:
    company="Microsoft"
    level=2

class Programmer(Employee,FreeLance):
    name="Rohit"


p=Programmer()
print(p.level)
print(p.eCode)


print("\n")
# Multilevel inheritance
class Person:
    country="India"

    def takeBreak(self):
        print("I am breathing...")

class Employee(Person):
    company="Google"

    def getSalary(self):
        print(f"Salary is {self.Salary}")

    def takeBreak(self):
        print("I am an Employee so I am luckily breathing...")

class Programmer(Employee):
    company ="Fiverr" 

    def getSalary(self):
        print(f"No salary to programmers")

p=Person()
p.takeBreak()
e=Employee()
e.takeBreak()
pr=Programmer()
pr.takeBreak()
print(pr.country)


print("\n")
# super (The super() function is used to give access to methods and properties of a parent or sibling class.)
# (The super() function returns an object that represents the parent class)
class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am a Progarmmer so I am breathing++..")

p = Person()
# p.takeBreath() 
e = Employee()
# e.takeBreath() 
pr = Programmer()
pr.takeBreath() 


print("\n")
#
class Employee:
    company ="Google"
    salary=5000
    location="Delhi"

    def changeSalary(self,sal):
      #  self.__class__.salary=sal    #change class attribute
        self.salary=sal               #change instance attribute

e=Employee()
print(e.salary)
e.changeSalary(6000)
print(e.salary)
print(Employee.salary)


print("\n")
# @property decorators
class Employee:
    company ="Google"
    salary=5000
    salaryBonus=1000
    #totalSalary=6000

    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus

e=Employee()
print(e.totalSalary)


print("\n")
# Operator overloading
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)