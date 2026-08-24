# Slot Machine Game
# 1. Deposit amount
# 2. Enter Bet Amount
# 3. Generate three random symbols
# 4. Check for win and pay if all correct
# 5. update balance

import random

balance = 100
status = True
win_state = ''

symbols = ['🍒', '🥭', '🍎']

def deposit():
    global balance
    deposit_amount = float(input('Deposit Money & place bet: '))
    if deposit_amount > 0:
        balance += deposit_amount
    else:
        print('Minumum is $1')

while status:
    # Intro Message
    print('\n')
    print('***************')
    print('Welcome to Python Slots')
    print('Symbols: 🍒 🥭 🍎')
    print('***************')
    print(f'Current balance: {balance}\n')

    # Ask for bet amount
    bet_amount = float(input('Place your bet amount: '))

    money_state = False
     
    # check if user has enough money
    while not money_state:
        if balance - bet_amount < 0:
            print('You dont have enough money')
            low_balance_question = int(input('Press 1 to deposit and 2 to exit: '))
            if low_balance_question == 1:
                deposit()
            else:
                continue
        else:
            money_state = True
            balance -= bet_amount

    # random symbol containers
    random_symbols = []
    
    # generate random sybols from the symbols
    for x in range(3):
        option = random.choice(symbols)
        random_symbols.append(option)

    # iterate and check win for random numbers
    if random_symbols[0] == random_symbols[1] == random_symbols[2]:
        win_state = 'Win 🥇'
        balance += bet_amount * 3
    elif random_symbols[0] == random_symbols[1] or random_symbols[1] == random_symbols[2] or random_symbols[0] == random_symbols[2]:
        win_state = 'Almost 😅'
    else:
        win_state = 'No Win 😭'

    print('\n')
    print(win_state.upper())
    print(f'Current balance: {balance}\n')

    # Display win
    for symbol in random_symbols:
        print(symbol, end=' ')

    # end game
    end_game = input('Do you whish to continue (yes or no): ')

    if end_game == 'yes':
        status = False
    else:
        continue


