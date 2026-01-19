try:
    a=int(input("Hey, enter a number: "))
    print(a)
except Exception as e:
    print(e)
else:
    print("I am inside else")