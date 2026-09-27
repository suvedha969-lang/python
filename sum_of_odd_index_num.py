num=input("enter a number")
sum=0
for i in range(len(num)):
    if i%2!=0:
       # num[i]=int(num[i]) cant do because string are immputable
        sum=sum+int(num[i]) #here temporaily change
print(sum)