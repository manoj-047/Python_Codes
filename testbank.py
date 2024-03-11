class Bank:
    def __init__(self):
        # Initializing dictionary to store the account information.
        self.accounts = {}

    def signup(self, username, password, initial_balance=0):
        if username in self.accounts:
            print("Username already exists. Please choose a different one.")
        else:
            self.accounts[username] = {'password': password, 'balance': initial_balance}
            print("Account created successfully.")

    def login(self, username, password):
        # Login to the user account if the username and password matches in the dictionary
        if username in self.accounts and self.accounts[username]['password'] == password:
            print("Login successful.\nWelcome to Bank,", username.capitalize())
            return True
        else:
            print("Invalid username or password.")
            return False

    def credit(self, username, amount):
        # Credit the specified amount to the user account
        if username in self.accounts:
            self.accounts[username]['balance'] += amount
            print(f"Amount {amount} credited successfully.")
            self.check_balance(username)
        else:
            print("Username not found.")

    def debit(self, username, amount):
        # Debit the specified amount from the user account
        if username in self.accounts:
            if self.accounts[username]['balance'] >= amount:
                self.accounts[username]['balance'] -= amount
                print(f"Amount {amount} debited successfully.")
                self.check_balance(username)
            else:
                print("Insufficient balance.")
        else:
            print("Username not found.")

    def check_balance(self, username):
        # Display the account balance of the user account
        if username in self.accounts:
            print(f"Your balance: {self.accounts[username]['balance']}")
        else:
            print("Username not found.")


bank = Bank()

# Sign up
bank.signup('sam', 'password', 1000)

# Login
if bank.login('sam', 'password'):
    # Check balance
    bank.check_balance('sam')
    # Credit
    bank.credit('sam', 500)
    # Debit
    bank.debit('sam', 200)

