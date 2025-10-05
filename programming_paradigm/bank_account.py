class BankAccount:
    def __init__(self, initial_balance=0, file_path="balance.txt"):
        self.file_path = file_path
        self.__account_balance = self._load_balance(initial_balance)

    def _load_balance(self, initial_balance):
        """Load the balance from the file if it exists; otherwise use the initial balance."""
        try:
            with open(self.file_path, "r") as f:
                return float(f.read())
        except FileNotFoundError:
            return float(initial_balance)

    def _save_balance(self):
        """Save the current balance to the file."""
        with open(self.file_path, "w") as f:
            f.write(str(self.__account_balance))

    def deposit(self, amount):
        """Deposit a specific amount into the account."""
        self.__account_balance += amount
        self._save_balance()

    def withdraw(self, amount):
        """Withdraw a specific amount from the account if sufficient balance exists."""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            self._save_balance()
            return True
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

