print("1.celsius to fahrenhit 2. fahrenhit to celsius")
op=int(input("enter ur option"))
match op:
    case 1:
         v=int(input("enter the temperature in celsius"))
         print("farenhit temperature")
         print((v*1.8)+32)
    case 2:
        c=int(input("enter the temperature in farenhit"))
        print("celsuis temperature")
        print(((int(c)-32)/9)*5)


