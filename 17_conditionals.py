#1
a=8
if(a<3):
    print("The value of a is greater than 3") 
elif(a>7):
    print("The value of a is greater than 7")
elif(a>17):
    print("The value of a is greater than 17")
else:
    print("The value of a is not greater than 3 or 7")


#2
age=int(input("Enter you age:\n"))
if(age>34 and age<56):
    print("You can work with us")
else:
    print("No,You cannot work with us") 


#3
age=int(input("Enter your age:\n"))
if(age>34 or age<56):
    print("You can work with us")
else:
    print("No,You cannot work with us")


#4
a=None
if(a is None):
    print("Yes")
else:
    print("No")