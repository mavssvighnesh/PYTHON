import random #importing the random module 



MAX_LINES = 3 #defining the maximum lines of bet we have 
MAX_BET =1000  # MAXIMUM amount we can bet 
MIN_BET = 1    #the minimum bet 


ROWS = 3    #no of rows 
COLS = 3    #no of columns 
#defining a dictoinary to no of symbols present in the row 
symbol_count={  
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
#defining a dictionary to make the value multiply 
symbol_value={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#fucntion to check the winning amount 
def check_winnnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]

    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
            else:
                winnings += values[symbol]*bet
                winning_lines.append(line+1)
    return winnings,winning_lines

#function to spin the slot machine 
def get_slot_machine_spin(rows, cols, symbol):
    all_symbols = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

#function to print the output of the slot machine 
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate (columns):
            if i!=len(columns)-1:
                print(column[row],"|",end=" | ")
            else:
                print(column[row],end="")
        print()

#fucntion to get the deposite amount
def intial_deposite():
    while True:
        depo = input("enter the intial deposite u want to add $")
        if depo.isdigit():
            depo = int(depo)
            if (depo > 0):
                break
            else:
                print("amount must be greater than zero 0")

        else:
            print("please enter a number")
    return depo

#function to get the no of lines u want to bet 

def get_no_of_lines():
    while True:
        lines = input(
            "enter the no of lines u want to bet (1 -"+str(MAX_LINES)+"?)")
        if lines.isdigit():
            lines = int(lines)
            if (1 <= lines <= MAX_LINES):
                break
            else:
                print("enter the no of lines in given range")

        else:
            print("please enter a number")
    return lines

#function to get the bet amount u want to bet on the no of lines 
def get_bet():
    while True:
        depo = input("what would u like to bet on each line ")
        if depo.isdigit():
            depo = int(depo)
            if (MIN_BET <= depo <= MAX_BET):
                break
            else:
                print(
                    f"enter the number of bet between ${MIN_BET}-${MAX_BET} ? ")

        else:
            print("please enter a number")
    return depo

#the main game function which preforms everything 
def game(balance):
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print("you have not enough balance to bet balance:", balance)
        else:
            print(
                f"you are bet is ${bet} on {lines} lines the total bet is equal to ${total_bet}")
            break
    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines=check_winnnings(slots,lines,bet,symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on lines ",*winning_lines)
    return winnings-total_bet

#main function of the program 
def main():
    balance = intial_deposite()
    while True:
        print(f"current balance is: ${balance}")
        spin=input("press enter to play(q to quit)")
        if spin=="q":
            break
        balance+=game(balance)
    print(f"you left with ${balance}")

main() #calling the main function 
