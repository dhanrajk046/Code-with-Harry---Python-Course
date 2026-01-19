def divisibles5(n):
    if (n%5==0):
        return True
    return False

a=[1,2,3454,54,143,545,1254,140]
f=list(filter(divisibles5,a))
print(f)