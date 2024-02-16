# Author : Manoj G
# Date : 16-02-2024
# Batch : 3:30 - 5:30
# Description : Credit 5 times in an account using if and for
#               Debit 5 times in an account and if the min balance goes below 500 exit


n, amount = 5, []
print("Bank")
ch = int(input('1. Credit\n2. Debit\nEnter your choice: '))
if ch == 1:
    print('\nCredit')
    for i in range(n):
        cr = int(input('Enter amount to credit: '))
        amount.append(cr)
        balance = sum(amount)
        print('Credit Successful!')
        print('Balance = ', balance)
elif ch == 2:
    print('\nDebit')
    balance = 7000
    for i in range(n):
        cr = int(input('Enter amount to debit: '))
        amount.append(cr)
        balance = balance - sum(amount)
        print('Debit Successful!')
        if balance < 5000:
            print("Insufficient Balance, Cannot Debit!")
    else:
        print('Balance = ', balance)
else:
    print('Invalid Choice!')
