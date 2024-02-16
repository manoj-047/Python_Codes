# Author : Manoj G
# Date : 15-02-2024
# Batch : 3:30 - 5:30
# Description : Create a bank details with username and password, add a new user whose details will be appended
#               to a list, after the user logs in date will be shown using date module and account number will
#               be generated using random module


import datetime
import random

print('Welcome To Yono Bank ')
username, password, acc_no = [], [], []
print('Register User')
uname = input('Enter Username: ')
pwd = input('Enter Password: ')
if len(pwd) == 8:
    rpwd = input('Re-enter Password: ')
    if pwd == rpwd:
        username.append(uname)
        password.append(pwd)
        print('\nUser Register Success\n')
        print('User Login')
        uname = input('Enter Username: ')
        pwd = input('Enter Password: ')
        if username[0] == uname and password[0] == pwd:
            print('\nWelcome to Yono Bank ', uname, '\t\t\t Date: ', datetime.date.today())
            acc_no = random.randint(1111111111111111, 9999999999999999)
            print('Your Account Number: ', acc_no)
            print('1. Credit')
            print('2. Debit')
            ch = int(input('Enter your choice: '))
            if ch == 1:
                print('Credit')
                balance = 1000
                print('Balance: ', balance)
                cr = int(input('Enter Amount to Be Credited: '))
                balance = balance + cr
                print('Balance: ', balance)
                rate = float(input('Enter the rate of interest: '))
                interest = (balance * rate) / 100
                print('Interest added for 1 year is: ', interest)
                balance = balance + interest
                print('Total balance after 1 year: ', balance)
            elif ch == 2:
                print('Debit')
                balance = 1000
                print('Balance: ', balance)
                db = int(input('Enter Amount to Be Credited: '))
                balance = balance - db
                print('Balance: ', balance)
            else:
                print('Invalid Choice')
        else:
            print('Username or Password Do-not Exist')
    else:
        print('Password Do-not Match, Re-register')

else:
    print('Password length should be 8 characters')
