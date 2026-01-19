with open(r"C:\Users\pc\OneDrive\Desktop\CWD python course\ch=9\log.txt", "r") as f:

    content=f.read()

    if("python" in content):
        print("Yes,the word python is present in the content")
    else:
        print("No,the word python is not present in the content")