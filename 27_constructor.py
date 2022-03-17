#
class Employee:
    company ="Google"
    def __init__(self):
        print("Employee is created")

aman=Employee()


#
class Employee:
    company ="Google"
    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = 50000
        self.subunit = subunit
    def getDetails(self):
        print(f"The name of the employee is: {self.name}")
        print(f"The salary of the employee is: {self.salary}")
        print(f"The subunit of the employee is: {self.subunit}")

rohan=Employee("Rohan",80000,"AWS")
rohan.getDetails()