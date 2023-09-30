str=input("Enter a String:")
dict = {}
for n in str:
    keys= dict.keys()
    print(keys)#added
    if n in keys:
        dict[n] = 1
    else:
        dict[n] = 2
print (dict) 
print(type(dict))#added