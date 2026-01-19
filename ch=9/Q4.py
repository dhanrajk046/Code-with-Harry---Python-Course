word="Donkey"
with open(r"C:\Users\pc\OneDrive\Desktop\CWD python course\ch=9\file1.txt", "r") as f:
    content=f.read()

contentNew=content.replace(word,"######")

with open(r"C:\Users\pc\OneDrive\Desktop\CWD python course\ch=9\file1.txt","w") as f:
    f.write(contentNew)