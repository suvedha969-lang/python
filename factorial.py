num=int(input("enter a number to find its factorial"))
fact=1
for i in range(num,0,-1):
    fact=fact*i
print(fact)