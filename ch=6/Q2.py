marks1=int(input("Enter marks for subject 1: "))
marks2=int(input("Enter marks for subject 2: "))
marks3=int(input("Enter marks for subject 3: "))

total_percentage=((marks1+marks2+marks3)/300)*100
if(total_percentage>=4 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You have passed the exam")
else:
    print("You have failed the exam,try next year.")