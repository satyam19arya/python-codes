#
while(True):
    a=input("Enter the number: ")
    if a =='quit':
        break

    try:
        a=int(a)
        if a>5:
            print("You have entered a number grater than 5")
        else:
            print("You have entered a number smaller than 5")

    except Exception as e:
        print(f"Your input is an error: {e}")

print("Thanks for playing this game")


print("\n")
#
while(True):
   try:
    a=int(input("Enter the number: "))
    c=1/a
    print(c)

   except ValueError as e:
      print("Please enter a valid value")

   except ZeroDivisionError as e:
      print("Make sure you are not using zero")



print("\n")
# Raising exception 
def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is false")

a=increment('ddd')
print(a)


print("\n")
# try with else
try:
    i=int(input("Enter the number: "))
    c=1/i
except Exception as e:
    print(e)
else:
    print("We are successfull")
 


print("\n")
# try with finally
try:
    i=int(input("Enter the number: "))
    c=1/i
except Exception as e:
    print(e)
    exit()              #finally statement will print even we have exit the code
finally:
    print("We are done")