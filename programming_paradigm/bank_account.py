class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("Sorry, you have to deposit a positive amount. Thank you")
    def withdraw(self, amount):
        if amount <= 0:
            print("Your account balance is not sufficient for this withdrawal")
            return False
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance: .2f}")
    


