import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS =3

symbol_count = {
    "A":2,
    "B":5,
    "C":6,
    "D":8
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winings(columns, lines, bet, value):
    winings = 0
    winings_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winings += value[symbol] * bet
            winings_lines.append(line+1)

    return winings, winings_lines





def get_slot_machine_spin(rows,cols,symbol):
    All_symbol = []

    for symbol,symbol_count in symbol.items():
        for _ in range(symbol_count):
            All_symbol.append(symbol)

    columns = []    
    for _ in range(cols):
        column = []
        current_symbol = All_symbol[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i ,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()



def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Amount must be greater then 0 ")
        else:
            print("Please Enter a number ")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter a number of line to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Enter a valid number of lines ")
        else:
            print("Please Enter a number ")
    return lines



def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else:
                print("Amount must be between {0} - {1} ".format(MIN_BET,MAX_BET))
        else:
            print("Please Enter a number ")
    return amount

def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()    
        total_bet = bet*lines
        
        if total_bet > balance:
            print(f"you do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines, so your total bet is equal to ${total_bet}")
    slot = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slot)
    winings, wining_line = check_winings(slot, lines, bet, symbol_value)
    print(f"You won: ${winings}")
    print(f"You won on lines: {wining_line}")

    return winings - total_bet



def main():
    balance = deposit()
    while True:
        print(f"Your current balance is: ${balance}")
        answer = input("press enter for play (q for quit).")
        if answer == 'q':
            break
        balance += spin(balance)

    print(f"You left with ${balance}")




if __name__ == "__main__":

    main()


