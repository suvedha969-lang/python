num=input("enter a number ")
sum=0
for i in range(len(num)):
    if i %2==0:
        sum=sum+int(num[i])
print(sum)