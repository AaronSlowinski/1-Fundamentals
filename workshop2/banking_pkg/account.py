class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def show_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def logout(self):
        # Perform any necessary logout operations here
        pass