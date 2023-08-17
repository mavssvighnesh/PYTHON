feet=float(input("enter the length in feet"))
choice=9
while(choice!=8):

    print("""--------------------MENU---------------------
            1.CONVERT FEET INTO INCHES 
            2.CONVERT FEET INTO YARDS 
            3.CONVERT FEET INTO MILES
             4.CONVERT FEET INTO MILLINMETERS
            5.CONVERT FEET INTO CENTIMETERS
             6.CONVERT FEET INTO METERS
            7.CONVERT FEET INTO KILOMETERS
             8.EXIT""")
    choice=int(input("enter ur choice"))
    inches=feet*12
    yards=feet*0.3333
    miles=feet*0.0001893
    millimeters=feet*304.8
    centimeters=feet*30.48
    meters=feet*0.3048
    kilometers=feet*0.0003048
    ext="code execution sucessful"
    convert=[feet,inches,yards,miles,millimeters,centimeters,meters,kilometers,ext]

    print(convert[choice])
