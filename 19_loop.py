fruits=['Banana','Apple','Mango','Grapes']
i=0
while (i<len(fruits)):
    print(fruits[i])
    i=i+1


for items in fruits:
    print(items)


# Range function is used to generate a sequence of numbers
for i in range(1,8):
    print(i)

print("\n")

for i in range(1,10,2): #it will skip every 2 numbers
    print(i)

print("\n")

for i in range(10):
    if i==5:
     continue
    print(i) 


# pass is a null statement in python. It instructs to "Do nothing"
i=4
if i>0:
    pass
print("Satyam is a good boy")