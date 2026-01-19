with open(r"C:\Users\pc\OneDrive\Desktop\CWD python course\ch=9\log.txt", "r") as f:
    lines=f.readlines()
    
    Lineno=1
    for line in lines:
        if "python" in line.lower():
            print(f"The word python is present in line no {Lineno}")
            break
        Lineno +=1
    else:
            print(f"The word python is not present in line no {Lineno}")