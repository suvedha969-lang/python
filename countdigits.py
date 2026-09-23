num=int(input("enter a number to count"))
count=0
while num>0:
    
    count=count+1
    num=num//10
print(count)