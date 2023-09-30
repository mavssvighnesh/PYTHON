a=int (input("enter the number value"))
b=int (input("enter the number value"))
l=[10,20,30,40,50]
try :
    c=a/b
    print(c)
    print(l[5])
except ZeroDivisionError:
    print("divide by zero error")
except IndexError:
    print("index is out of range")
except:
    print("exception raised")
finally:
    print("code runned sucessfully ")

    
