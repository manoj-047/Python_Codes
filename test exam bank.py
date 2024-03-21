import datetime


class Account:
    def __init__(self, account_no, name, password, contact_no, address, initial_deposit):
        self.account_no = account_no
        self.name = name
        self.password = password
        self.contact_no = contact_no
        self.address = address
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

    def get_transactions(self):
        return self.transactions

    def update_personal_info(self):
        print("Update Personal Information:")
        print("1. Name")
        print("2. Contact No.")
        print("3. Address")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_name = input("Enter new name: ")
            self.name = new_name
            print("Name updated successfully.")
        elif choice == "2":
            new_contact_no = input("Enter new contact number: ")
            self.contact_no = new_contact_no
            print("Contact number updated successfully.")
        elif choice == "3":
            new_address = input("Enter new address: ")
            self.address = new_address
            print("Address updated successfully.")
        else:
            print("Invalid choice. No changes made.")


class Bank:
    def __init__(self):
        self.accounts = {}
        self.admin_name = 'admin'
        self.admin_password = 'admin@123'

    def create_account(self):
        account_no = input("Enter account number: ")
        name = input("Enter name: ")
        password = input("Enter password: ")
        contact_no = input("Enter contact number: ")
        address = input("Enter address: ")
        initial_deposit = float(input("Enter initial deposit amount: "))

        account = Account(account_no, name, password, contact_no, address, initial_deposit)
        self.accounts[account_no] = account
        print("Account created successfully.")

    def authenticate_user(self, account_no, password):
        if account_no in self.accounts and not self.accounts[account_no].is_locked:
            account = self.accounts[account_no]
            if account.password == password:
                return account
        return None

    def admin_login(self, admin_name, admin_password):
        return admin_name == self.admin_name and admin_password == self.admin_password

    def view_account_info(self, account_no):
        if account_no in self.accounts:
            account = self.accounts[account_no]
            print("Account Information:")
            print(f"Account Number: {account.account_no}")
            print(f"Name: {account.name}")
            print(f"Contact Number: {account.contact_no}")
            print(f"Address: {account.address}")
            print(f"Balance: {account.balance}")
        else:
            print("Account not found.")

    def lock_account(self, account_no):
        if account_no in self.accounts:
            account = self.accounts[account_no]
            account.is_locked = True
            print(f"Account {account_no} locked.")
        else:
            print("Account not found.")

    def unlock_account(self, account_no):
        if account_no in self.accounts:
            account = self.accounts[account_no]
            account.is_locked = False
            print(f"Account {account_no} unlocked.")
        else:
            print("Account not found.")

    def delete_account(self, account_no):
        if account_no in self.accounts:
            del self.accounts[account_no]
            print(f"Account {account_no} deleted.")
        else:
            print("Account not found.")

    def user_menu(self, account):
        while True:
            print("User Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Update Personal Information")
            print("6. Logout")

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
                transactions = account.get_transactions()
                for transaction in transactions:
                    print(f"{transaction[0]} - {transaction[1]}: {transaction[2]}")

            elif option == "5":
                account.update_personal_info()

            elif option == "6":
                break

    def admin_menu(self):
        while True:
            print("Admin Menu:")
            print("1. View Account Information")
            print("2. Lock Account")
            print("3. Unlock Account")
            print("4. Delete Account")
            print("5. Logout")

            option = input("Select an option: ")

            if option == "1":
                account_no = input("Enter account number: ")
                self.view_account_info(account_no)

            elif option == "2":
                account_no = input("Enter account number: ")
                self.lock_account(account_no)

            elif option == "3":
                account_no = input("Enter account number: ")
                self.unlock_account(account_no)

            elif option == "4":
                account_no = input("Enter account number: ")
                self.delete_account(account_no)

            elif option == "5":
                break


# Main program
bank = Bank()

while True:
    print("Main Menu:")
    print("1. Create Account")
    print("2. User Login")
    print("3. Admin Login")
    print("4. Exit")

    option = input("Select an option: ")

    if option == "1":
        bank.create_account()

    elif option == "2":
        account_no = input("Enter your account number: ")
        password = input("Enter your password: ")
        user_account = bank.authenticate_user(account_no, password)

        if user_account:
            if user_account.is_locked:
                print("Your account is locked. Please contact the admin.")
            else:
                bank.user_menu(user_account)
        else:
            print("Invalid account number or password.")

    elif option == "3":
        admin_name = input("Enter admin name: ")
        admin_password = input("Enter admin password: ")
        if bank.admin_login(admin_name, admin_password):
            bank.admin_menu()
        else:
            print("Invalid admin credentials.")

    elif option == "4":
        break
yy