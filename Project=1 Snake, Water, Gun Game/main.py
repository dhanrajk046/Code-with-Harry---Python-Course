import random
'''
Docstring for Project=1 Snake, Water, Gun Game.main

1 for snake
-1 for water
0 for gun
'''

computer=random.choice([-1,0,1])
yourstr=input("Enter your choice (snake, water, gun): ")
yourDic={"snake":1,"water":-1,"gun":0}
reserveDict={1:"snake",-1:"water",0:"gun"}
you=yourDic[yourstr]

print(f"You choose:{reserveDict[you]}\nComputer choose:{reserveDict[computer]}")

if (computer==you):
    print("It's a draw!")

#By now we have 2 numbers (variables), you and computer

else:
    if(computer==-1 and you==1):
        print("You win!")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==1 and you==-1):
        print("You Lose!")
    elif(computer==1 and you==-1):
        print("You Win!")
    elif(computer==0 and you==-1):
        print("You Win!")
    elif(computer==0 and you==1):
        print("You Lose!")
        
    else:
        print("Something went wrong!")