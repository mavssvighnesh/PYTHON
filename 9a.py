import math
a=input("Enter the first string:")
b=input("Enter the second string:")
c=len(a)
d=len(b)

if c==d:
    i=0
    count=0
    for i in range(c):
        if a[i]==b[i]:
            count=0
        else :
            count=count+1
            break

    if count==0:
        print("All characters are same")
    else: 
        print("Values are not same")
else:
    print("Enter the characters of same lenght")
    print("Run again")