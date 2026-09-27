num=input("enter a number")
for i in range(len(num)):  #here len used ,if we for i in num then number is string so cant divide ,so we use length to find index
    if i%2!=0:
        print(num[i])

        #len start with 1 not 0
        #commputer start index from 0,1,2,3