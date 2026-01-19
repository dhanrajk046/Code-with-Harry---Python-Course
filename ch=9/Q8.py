with open(r"C:\Users\pc\OneDrive\Desktop\CWD python course\ch=9\This.txt", "r") as f:
    content=f.read()

with open(r"C:\Users\pc\OneDrive\Desktop\CWD python course\ch=9\This_copy.txt", "w") as f:
    f.write(content)