#1 Program to read the text from a given file 'poems.txt' and find out whether it contains the word twinkle
f=open('poems.txt','r')
t=f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()


#2 The game function in a program lets a user plays a game and returns the score as an integer. 
#  You need to read a file 'score.txt' which is either blank or contains the previous high score. 
#  You need to write a program to update the high score whenever game() breaks the high score

def game():
    return 25

score = game()
with open('score.txt','r') as f:
    high_score = f.read()

if high_score=='':
    with open('score.txt','w') as f:
        f.write(str(score))
elif int(high_score)<score :
    with open('score.txt','w') as f:
        f.write(str(score))


#3 Program to generate multiplication tables from 2 to 20 and write it to the defined files. 
# Place these files in the folder for a 13 year old child

for i in range(2,21):
  with open(f"tables/Multiplication_table_of_{i}.txt",'w') as f:
    for j in range(1,11):
        f.write(f"{i}X{j}={i*j}")
        if j!=10:
          f.write('\n')


#4 A file contains a word "Donkey" multiple times. You need to write a program which replaces this word with ##### by updating the same file
with open("sample3.txt",'r') as f:
    content = f.read()

content = content.replace("donkey","#$%^&*")

with open("sample3.txt",'w') as f:
    f.write(content)


#5 Program to read a log file and find out whether it contains python
content=True
i=1

with open("log_file.txt",'r') as f:
    while content:
        content=f.readline()
        if 'python' in content:
            print(f"Yes, python is present on line number {i}")
        i+=1


#6 Program to find out whether a file is identical or not
with open("log_file.txt",'r') as f:
    f1=f.read()

with open("log_file.txt",'r') as f:
    f2=f.read()

if (f1==f2):
    print("Files are identical")
else:
    print("Files are not identical")