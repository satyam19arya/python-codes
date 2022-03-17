# f=open('sample.txt)  # By default, the mode is read
f=open('sample.txt','r')
data=f.read()
# data=f.read(5)  # reads first 5 characters from the file
# data=f.readline() # reads first line
print(data)
f.close()


# 'rb' will open for read in binary mode
# 'rt' will open for read in text mode


f=open('sample2.txt','a')
f.write("Hello i am writing anything here")
f.close()

# The best way to open and close the file automatically is the with statement
with open('sample2.txt','r') as f:
    a=f.read()
    print(a)