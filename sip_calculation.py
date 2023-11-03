import math as m
from datetime import datetime as dt

global p, a, r, t, n

def calculate_tenure():
    
    start = input("Enter the start date (YYYY-MM-DD): ")
    end = input("Enter the end date (YYYY-MM-DD): ")

    start = dt.strptime(start, '%Y-%m-%d')
    end = dt.strptime(end, '%Y-%m-%d')

    # Calculate the time difference
    time_period=end-start

    # Calculate the number of years and remaining days
    years = time_period.days // 365
    remain = time_period.days % 365

    # Calculate the number of months and remaining days
    months = remain // 30
    remain = remain % 30

    print(years,months,remain)


def take_input():

    print("enter the following values if no value available please enter 0")
    global p, a, r, t, n
    p = float(input("enter the principal value"))
    a = float(input("enter the maturity value"))
    r = float(input("enter the rate of interest"))
    vv=int(input("enter 1 if u have dates with u 0 if no "))
    if vv==1:
        t=calculate_tenure()
    if vv==0:
        pass

    n = float(input("enter the compounding factor for a year"))


def calculate():
    while (1):
        print("------------MENU-------------- \n 1.calculate principal \n 2.calculate maturity value \n 3.calculate rate of interest ")
        print("\n 4.calculate period of time \n 5. calculate compounding span \n 6.change the values \n 7.exit")
        op = input("enter a choice")
        if op.isdigit():
            pass
        else:
            op = input("enter a valid choice")
            match op:
                case 1:
                    x = a/(1+r/n)**(n*t)
                    print("PRINCIPAL AMOUNT IS  : "+x)
                case 2:
                    x = p(1+r/n) ^ (n*t)
                    print("THE MATURITY VALUE IS : "+x)
                case 3:
                    x = n*((a/p) ^ (1/(n*t))-1)
                    print("THE RATE OF INTERST IS : "+x)
                case 4:
                    x = (m.log(a/p))/n(m.log(1+(r/n)))
                    print("THE TENURE IS : "+x)
                case 5:
                    x = (m.log(a/p))/(m.log(1+r))
                    print("THE COMPOUNDING FREQUENCY IS : "+x)
                case 6:
                    take_input()
                case 7:
                    exit()
calculate_tenure()