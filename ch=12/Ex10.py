try:
    a=int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("Hey I am inside of finally.")