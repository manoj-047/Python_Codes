

class Bank:
    def __init__(self, bal):
        self.bal = bal

    def credit(self):
        c = float(input("Enter the amount to be credit: "))
        self.bal = self.bal + c
        print(f"Available Balance: {self.bal}")

    def debit(self):
        d = float(input("Enter the amount to be credit: "))
        self.bal = self.bal - d
        print(f"Available Balance: {self.bal}")


amt = Bank(1234)
i = 0
while i < 5:
    ch = int(input("1.Credit\n2.Debit\n3.Exit\nEnter the choice: "))
    if ch == 1:
        print("Credit")
        amt.credit()
    elif ch == 2:
        print("Debit")
        amt.debit()
    else:
        exit()
