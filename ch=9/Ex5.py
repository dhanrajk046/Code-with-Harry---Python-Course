st="Hey Harry you are amazing"
f=open("myfile.txt","a")
f.write("\n"+st)
f.close()

'''
MODES OF OPENING FILE:

r=reading
w=writing
a=appending
u=updating
rb=reading in binary mode
wb=writing in text mode

WITH STATEMENT:

f=open("file.txt")
print(f.read())
f.close()

The same can be written using with statement:
with open("file.txt") as f:
    print(f.read())
'''


with open("myfile.txt") as f:
    print(f.read())