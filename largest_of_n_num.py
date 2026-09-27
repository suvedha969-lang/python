n=int(input("enter number of elements"))
num=int(input("enter num 1:"))
largest=num
for i in range(2,n+1): #note range
    num=int(input("enter a number"+ str(i) + ":")) #use + as , not able to use in input statementfor in num:
    if num>largest:
        largest=num
print(largest)
