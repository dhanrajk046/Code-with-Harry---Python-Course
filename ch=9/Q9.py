with open(r"C:\Users\pc\OneDrive\Desktop\CWD python course\ch=9\This.txt", "r") as f:
    content1=f.read()

with open(r"C:\Users\pc\OneDrive\Desktop\CWD python course\ch=9\log.txt", "r") as f:
    content2=f.read()

if (content1==content2):
    print("Yes, the files are identical")
else:
    print("No, the files are not identical")