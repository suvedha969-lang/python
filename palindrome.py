num=int(input("enter a number to check it is a palindrome  "))
original=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)
if original==rev:
    print("plalindrom")
else:
    print("not a palindrome")