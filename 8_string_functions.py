story="once upon a time there was a youtuber named Harry who uploaded python course with notes"

#string functions
print(len(story))
print(story.endswith("klfdj"))
print(story.endswith("notes"))
print(story.count("a"))
print(story.capitalize())
print(story.find("who"))
print(story.replace("time","ontime"))


#To check if a certain phrase or character is present in a string, we can use the keyword in
txt="The best things in life are free!"
if "free" in txt:
    print("yes, it is present")
else:
    print("False")


#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 


#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))