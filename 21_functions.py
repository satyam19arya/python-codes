def percent(marks):
     p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
     return p

marks1=[45,78,65,34]
percentage1=percent(marks1)

marks2=[75,98,88,78]
percentage2=percent(marks2)

print(percentage1,percentage2)


# Default Parameter values
def greet(name="Stranger"):
    print("Good Day, "+name)

greet("Satyam")
greet() 


# Recursion
def factorial_recursion(n):
    if n==1 or n==0: 
        return 1
    return n* factorial_recursion(n-1)


# Function to remove a given word from a string and strip it at the same time
def remove_and_split(string,word):
    newStr=string.replace(word,"madam")      #change the word
    return newStr.strip()               #remove the space

this="    Hello sir, How are you   "
n=remove_and_split(this,"sir")
print(n)