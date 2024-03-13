# Author : Manoj G
# Date : 15-02-2024
# Batch : 3:30 - 5:30
# Description : Create a bank details with username and password, add a new user whose details will be appended
#               to a list, after the user logs in date will be shown using date module and account number will
#               be generated using random module


import datetime
import random

print('Welcome To My Bank')
username, password = [], []

# Register User
print('Register User')
uname = input('Enter Username: ')
pwd = input('Enter Password: ')
if len(pwd) == 8:
    rpwd = input('Re-enter Password: ')
    if pwd == rpwd:
        username.append(uname)
        password.append(pwd)
        print('\nUser Register Success\n')
    else:
        print('Passwords do not match, please re-register with the correct password.')
        exit(1)
else:
    print('Password length should be 8 characters')
    exit(1)

# User Login
print('User Login')
uname = input('Enter Username: ')
pwd = input('Enter Password: ')
if username[0] == uname and password[0] == pwd:
    print('\nWelcome to Yono Bank', uname, '\t\t\t Date:', datetime.date.today())
    acc_no = random.randint(1111111111111111, 9999999999999999)
    print('Your Account Number:', acc_no)
    balance = 2000  # Assuming initial balance

    while True:
        print('\nMain Menu:')
        print('1. Credit')
        print('2. Debit')
        print('3. Check Account Balance')
        print('4. Exit')
        ch = int(input('Enter your choice: '))
        if ch == 1:
            print('Credit')
            print('Balance:', balance)
            cr = int(input('Enter Amount to Be Credited: '))
            balance += cr
            print('New Balance:', balance)
        elif ch == 2:
            print('Debit')
            print('Balance:', balance)
            db = int(input('Enter Amount to Be Debited: '))
            if balance - db < 2000:
                print('Debit unsuccessful. Minimum balance limit reached.')
            else:
                balance -= db
                print('New Balance:', balance)
        elif ch == 3:
            print('Account Balance:', balance)
        elif ch == 4:
            print("Thank You!!")
            exit(0)
        else:
            print('Invalid Choice')
else:
    print('Username or Password Do-not Exist')
