#1 English translation dictionary
'''
myDict={
    "Pankha":"Fan",
    "Dabba":"Box",
    "Vastu":"Item",
    "Ghar":"Home"
}
a=input("Enter the Hindi Word\n")
# print("The meaning of your word is:",myDict[a])

print("The meaning of your word is:",myDict.get(a))  # This will not throw an error if key is not present in the dictionary


#2 Take input from users & display all unique numbers
a1=int(input("Enter the number 1:\n"))
a2=int(input("Enter the number 2:\n"))
a3=int(input("Enter the number 3:\n"))
a4=int(input("Enter the number 4:\n"))
a5=int(input("Enter the number 5:\n"))
a6=int(input("Enter the number 6:\n"))
a7=int(input("Enter the number 7:\n"))
a8=int(input("Enter the number 8:\n"))

s={a1,a2,a3,a4,a5,a6,a7,a8}
print(s)

'''
#3
s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))


#4 Create an empty dictionary and allow 4 friends to enter their favorite language as values and use keys as their names
favLang={

}

a=input("Enter your favorite language Shubham:\n")
b=input("Enter your favorite language Ankit:\n")
c=input("Enter your favorite language Sonali:\n")
d=input("Enter your favorite language Harshit:\n")

favLang["Subham"]=a
favLang["Ankit"]=b
favLang["Sonali"]=c
favLang["Harshit"]=d

print(favLang)