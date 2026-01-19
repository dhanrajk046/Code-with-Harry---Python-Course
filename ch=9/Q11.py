#renaming a file

#you can use OS module to rename a file

with open (r"C:\Users\pc\OneDrive\Desktop\CWD python course\ch=9\This.txt") as f:
    content=f.read()
with open (r"C:\Users\pc\OneDrive\Desktop\CWD python course\ch=9\This2.txt", "w") as f:
    f.write(content)