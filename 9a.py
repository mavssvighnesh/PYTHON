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
        if a[i]!=b[i]:
            count=count+1
    value=math.ceil(c/2)
    if count==0:
        print("All characters are same")

    elif count<value:
        print("Values are nearly same")
    else: 
        print("Values are not same")
else:
    print("Enter the characters of same lenght")
    print("Run again")