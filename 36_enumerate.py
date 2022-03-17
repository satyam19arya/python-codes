# Normal way
list1 =[3,53,2,False,6.2,"Satyam"]
index =0
for item in list1:
    print(item,index)
    index += 1


print("\n")
# enumerate
list1 =[3,53,2,False,6.2,"Rohan"]
for index,item in enumerate(list1):
    print(item,index) 