n1=int(input("enter num 1"))
n2=int(input("enter num 2"))
n3=int(input("enter num 3"))
if n1<=n2 and n1<=n3:
    print(n1,"n1 is smallest",)
elif n2<=n1 and n2<=n3:
    print(n2,"n2 is smallest")
else:
    print(n3,"n3 is smallest")