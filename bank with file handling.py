# Author : Manoj G
# Date : 29-02-2024
# Batch : 3:30 - 5:30
# Description :


import datetime
import random

with open("output.txt", "w") as file:
    print('Welcome To ** Bank ')
    username, password, acc_no, balance = [], [], [], 10000
    print('Register User')
    uname = input('Enter Username: ')
    pwd = input('Enter Password: ')
    if len(pwd) >= 8:
        rpwd = input('Re-enter Password: ')
        if pwd == rpwd:
            username.append(uname)
            password.append(pwd)
            print('\nUser Register Success\n')
            print('User Login')
            uname = input('Enter Username: ')
            pwd = input('Enter Password: ')
            if username[0] == uname and password[0] == pwd:
                file.write(f'\nWelcome to ** Bank, {uname.capitalize()} \t\t\t Date: {datetime.datetime.today()}\n')
                file.write("-"*85)
                accno = random.randint(1111111111111111, 9999999999999999)
                file.write(f'\nYour Account Number: {accno}')
                acc_no.append(accno)
                file.write(f"\nAccount Balance: {balance}\n")
                print(f"Credit\nBalance:{balance}")
                file.write("\nCredit")
                for i in range(5):
                    cr = int(input("Enter Amount to be credited: "))
                    file.write(f"\nBalance before credit: {balance}")
                    balance = balance + cr
                    file.write(f"\nBalance : {balance}\n")
                file.write("\n\nDebit")
                print(f"\nDebit\nBalance:{balance}")
                for i in range(5):
                    if balance > 2000:
                        db = int(input("\nEnter Amount to be debited: "))
                        file.write(f"\nBalance before debit: {balance}")
                        bal = balance - db
                        if balance <= 2000:
                            print("Insufficient Balance")
                            exit()
                        file.write(f"\nBalance : {balance}\n")
            else:
                print('Username or Password Do-not Exist', exit())
        else:
            print('Password Do-not Match, Re-register', exit())

    else:
        print('Password length should be 8 or more characters', exit())
file.close()