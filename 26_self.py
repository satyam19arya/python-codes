# self(self refers to the instance of the class)
class Employee:
    company ="Gooogle"
    def getSalary(self):
        print("Salary is 100k")

aman=Employee()
aman.getSalary()    # Employee.getSalary(aman)


# static method (sometimes we need a function that doesn't use the self parameter)
class Employee:
    company ="Gooogle"
    @staticmethod
    def getSalary():
        print("Salary is 100k")

aman=Employee()
aman.getSalary() 