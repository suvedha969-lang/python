s=input()
count=0
for i in s:
    if i in "aeiouAEIOU": #if i in "aeiou" or i in "AEIOU" is allowed again write "i"
        count=count+1

print(count)