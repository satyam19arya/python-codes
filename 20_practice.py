#1 Program to print multiplication table of a given number
number=int(input("Enter the number \n"))

for i in range(1,11):
    print(str(number) + "X" + str(i) + "=" + str(i*number))


print("\n")
#2 Program to greet all the persons names stored in a list and which starts with S
list=["Harry","Satyam","Sachin","Sohan","Rahul"]

for name in list:
    if(name.startswith("S")):
        print(str(name) + ",Hello")


print("\n")
#3 Program to find whether a given number is prime or not
num=int(input("Enter the number:\n"))
prime=True

for i in range(2,num):
    if(num%i==0):
        prime=False
        break
if prime:
    print("This number is prime")
else:
    print("This number is not prime")
  

print("\n")
#4 Program to calculate the factorial of a given number using for loop
num=int(input("Enter the number:\n"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f"The factorial of {num} is {factorial}")
 

print("\n")
#5 Program to print star pattern
n=4
for i in range(4):
    print("*"*(i+1))

'''
*
**
***
****
'''