# Write a program to open three files 1.txt,2.txt,3.txt.
# If any of the files are not present,a message without exiting the program must be printed prompting the same
def read_file(filename):
  try:
    with open(filename, 'r') as f:
        print(f.read())
  except FileNotFoundError:
        print(f"File {filename} is not found")

read_file("1.txt")
read_file("2.txt")
read_file("3.txt")

 
print("\n")
# Write a program to print third, fifth and seventh element from a list using enumerate function
l=[1,2,3,4,5,6,7,8,9,10]

for index,item in enumerate(l):
    if index==2 or index==4 or index==6:
        print(index,item)


print("\n")
# Write a list comprehension to print a list which contains the multiplication table of a user entered number
num=int(input("Enter your number: "))

table=[num*i for i in range(1,11)]
print(table)


print("\n")
# Store the multiplication table generated above in a file named table.txt
num=int(input("Enter your number: "))

table=[num*i for i in range(1,11)]
print(table)
with open("table.txt", 'w') as f:
    f.write(str(table))
    f.write('\n')