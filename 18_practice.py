#1 Write a program to find out whether a student is pass or fail, if it requires told 40% and
# atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user

sub1=int(input("Enter first subject marks:\n"))
sub2=int(input("Enter second subject marks:\n"))
sub3=int(input("Enter third subject marks:\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subjects")

if((sub1+sub2+sub3)/3<40):
    print("You are fail due to total percentage less than 40%")
else:
    print("You passed the exam")


#2 A spam comment is defined as a text containing following keywords:
# "make a lot of money","buy now","subscribe this","click this".Write a program to detect these spams

spam=False
text=input("Enter the text:\n")

if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("click this" in text):
    spam=True
elif("subscribe this" in text):
    spam=True

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")  


#4 Program which finds out whether a given name is present in a list or not
names=["satyam","rohan","aman","rahul","aditi","shipra"]
name=input("Enter the name to check:\n")

if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")