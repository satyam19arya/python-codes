greeting = "Good Morning, "
name = "Harry"
print(type(name))

# Concatenating two strings
c = greeting + name
print(c)
name = "Harry"
print(name[4])
# name[3] = "d" --> Does not work

print(name[1:4])
print(name[:4]) # is same as name[0:4]
print(name[1:]) # is same as name[1:5]
c = name[-4:-1] # is same is name[1:4]
print(c)

name = "HarryIsGood"
d = name[0::3]  #skip every 2 char
print(d)


#The upper() method returns the string in upper case
a="Hello, world!"
print(a[2:4].upper())