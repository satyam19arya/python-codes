# Class Attributes
class Employee:
    company="Google"

satyam=Employee()
aman=Employee()
print(satyam.company)
print(aman.company)

Employee.company="AWS"
print(satyam.company)
print(aman.company)

 
print("\n")
# Instance Attributes
class Employee:
    company="Google"
    salary=90000

satyam=Employee()
aman=Employee()
satyam.salary=190000
print(satyam.salary)
print(aman.salary)  