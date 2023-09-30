a=int (input("enter the number value"))
b=int (input("enter the number value"))
l=[10,20,30,40,50]
try:
    d="python"+str(20)
    c=a/b
    print(l[3])
except(ZeroDivisionError,IndexError,TypeError):
    print('exception raised')
else:
    print(c)
    print(d)
finally:
    print("code sucessful")