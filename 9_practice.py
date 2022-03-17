#1
a=input("Enter your name:\n")
print("Good Afternoon "+a)

#2
letter='''Dear, realname
You are selected!
Date: currentdate'''

name=input("Enter your name\n")
date=input("Enter the date\n")

letter=letter.replace("realname",name)
letter=letter.replace("currentdate",date)
print(letter)

#3
letter="Dear Satyam, This Python course is nice! Thanks!"
print(letter)

formatted_letter="Dear Satyam,\n\tThis Python course is nice!\nThanks!"
print(formatted_letter)