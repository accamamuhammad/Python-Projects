# Python Banking Program

balance = 0
status = True
user_name = ''
user_password = 0000

# Function for Deposit
def deposit():
    # State of password check
    password_validation = False

    print('\n')
    print('Step 1 / 2')
    deposit_amount = float(input('Enter amount you want to deposit: $'))
    
    # get deposit amount from user
    while deposit_amount <= 0:
        deposit_amount = float(input('Enter a valid amount: $'))

    # get password from user
    print('Step 2 / 2')
    password = int(input('Enter 4 digit password: '))

    # Validate Password
    while not password_validation:
        if int(password) == int(user_password):
            print('\n')
            password_validation = True
        else:
            print('Invalid Password')
            password = input('Please Enter the correct password')
            print('\n')

    # Add to balance when validation is complete
    if password_validation:
       update_balance(deposit_amount, True)
       print('Deposit Succesfull')


# Function for Withdrawal
def withdrawal():
    # State of password check
    password_validation = False
    account_number_validation = False

    # get deposit amount from user
    print('\n')
    print('Step 1 / 4')
    withdrawal_amount = float(input('Enter amount you want to withdraw: $'))

    while withdrawal_amount <= 0:
        withdrawal_amount = float(input('Enter a valid amount: $'))

    # Account Number
    print('Step 2 / 4')
    account_number = input('Enter the Receivers Account Number: ')

    while not account_number_validation:
        account_number_length = len(account_number)

        if account_number_length == 10:
            account_number_validation = True
        else:
            account_number = input('Enter a Valid Account Number')
    
    # Bank Name
    print('Step 3 / 4')
    bank_name = input('Enter the Receivers Bank Name: ')
    bank_name = bank_name.capitalize()


    # get password from user
    print('Step 4 / 4')
    password = input('Enter 4 digit password: ')

    # Validate Password
    while not password_validation:
        if int(password) == int(user_password):
            print('\n')
            password_validation = True
        else:
            print('Invalid Password')
            password = input('Please Enter the correct password')
            print('\n')

    # Add to balance when validation is complete
    if password_validation and account_number_validation:
       # check if user has the money to withdraw
       check_balance = balance - withdrawal_amount
       if check_balance < 0:
           print('Withdrawal Un-Succesfull')
           print('Insufficient Funds!!!')
       else:
        print(f'{withdrawal_amount} has been sent to {account_number} {bank_name}')
        update_balance(withdrawal_amount, False)

# Update Balance
def update_balance(amount, state):
    global balance
    if state:
        balance += amount
        print(f'Your Current Balance is ${balance:.2f}')
        print('\n')
    else:
        balance -= amount
        print(f'Your Current Balance is ${balance:.2f}')
        print('\n')

# Get user info
print('\n')
print('Welcome To The Bank')
user_name = input("Enter your name: ")
user_password = input("Enter a 4 digit password: ")

# clean up & validate user info
user_name = user_name.replace(' ', '')
user_name = user_name.capitalize()

while len(user_password) != 4:
    user_password = input("Password must be 4 digits: ")
print(f'Welcome {user_name}')

while status:
    # Show Command Message Options
    print('1. Show Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')

    command = int(input('Select from the Options: '))

    # validate input command and execute them
    if command == 1:
        print('\n')
        print(f'Your Balance is ${balance:.2f}\n')
    elif command == 2:
        deposit()
    elif command == 3:
        withdrawal()
    elif command == 4:
        print('\n')
        print('Thank Your For Banking With Us')
        print('\n')
        status = False
    else:
        print('\n')
        print('Please enter a number from the options 1 to 4\n')
