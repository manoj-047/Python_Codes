import datetime

class Account:
    def __init__(self, account_no, name, password, initial_deposit):
        self.account_no = account_no
        self.name = name
        self.password = password
        self.balance = initial_deposit
        self.transactions = []
        self.is_locked = False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append((datetime.datetime.now(), "Deposit", amount))
            print(f"Amount deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        min_balance = 2000
        if 0 < amount <= 2000:
            if self.balance - amount >= min_balance:
                self.balance -= amount
                self.transactions.append((datetime.datetime.now(), "Withdrawal", amount))
                print(f"Amount withdrawn: {amount}")
            else:
                print(f"Insufficient funds. Minimum balance to maintain is {min_balance}.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_no = input("Enter account number: ")
        name = input("Enter name: ")
        password = input("Enter password: ")
        initial_deposit = float(input("Enter initial deposit amount: "))

        account = Account(account_no, name, password, initial_deposit)
        self.accounts[account_no] = account
        print("Account created successfully.")

    def user_login(self, account_no, password):
        if account_no in self.accounts and not self.accounts[account_no].is_locked:
            account = self.accounts[account_no]
            if account.password == password:
                return account
        return None

    def user_menu(self, account):
        while True:
            print("User Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Logout")

            option = input("Select an option: ")

            if option == "1":
                amount = float(input("Enter the deposit amount: "))
                account.deposit(amount)

            elif option == "2":
                amount = float(input("Enter the withdrawal amount: "))
                account.withdraw(amount)

            elif option == "3":
                balance = account.get_balance()
                print(f"Account balance: {balance}")

            elif option == "4":
                break

# Main program
bank = Bank()

while True:
    print("Main Menu:")
    print("1. Create Account")
    print("2. User Login")
    print("3. Exit")

    option = input("Select an option: ")

    if option == "1":
        bank.create_account()

    elif option == "2":
        account_no = input("Enter your account number: ")
        password = input("Enter your password: ")
        user_account = bank.user_login(account_no, password)

        if user_account:
            bank.user_menu(user_account)
        else:
            print("Invalid account number or password.")

    elif option == "3":
        break
