'''
list=["Camera","Laptop","Phone","Mobile","Kite","Hard Disk"]

sentence=" @@ ".join(list)
print(sentence) 


print("\n")
# map (Map applies a function to all items in the input list)
def square(num):
    return num*num

l=[1,2,3,4,5]
print(list(map(square,l)))


print("\n")
# filter
def greater_than_5(num):
    if num>5:
        return True
    else:
        return False

l=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(greater_than_5,l)))

'''
print("\n")
# A list contains the multiplication table of 7. Write a program to convert it to a vertical string of same number
l=[str(i*7) for i in range(1,11)]
print(l)

verticalTable="\n".join(l)
print(verticalTable)