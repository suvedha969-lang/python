n=int(input("enter a number"))
num=int(input("enter num 1:"))

smallest=num
for i in range(2,n+1):
    num=int(input("enter num"+str(i)+":"))
    if num<smallest:
        smallest=num
print(smallest)