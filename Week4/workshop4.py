class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        if 2 <= len(new_name) <= 10:
            self.name = new_name
        else:
            print("Name must be between 2 and 10 characters.")

    def change_pin(self, new_pin):
        if len(str(new_pin)) == 4:
            self.pin = new_pin
        else:
            print("PIN must be exactly 4 numbers.")

    def change_password(self, new_password):
        if len(new_password) >= 5:
            self.password = new_password
        else:
            print("Password must be at least 5 characters.")


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    def toggle_hold(self):
        self.on_hold = not self.on_hold

    def show_balance(self):
        print(f"{self.name}'s balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if self.on_hold:
            print("Account is on hold.")
        elif amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.on_hold:
            print("Account is on hold.")
        elif amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def transfer_money(self, other_user, amount, pin):
        if self.on_hold or other_user.on_hold:
            print("One of the accounts is on hold.")
        elif self.pin == pin and amount <= self.balance:
            self.balance -= amount
            other_user.balance += amount
            return True
        else:
            return False

    def request_money(self, other_user, amount, pin, password):
        if self.on_hold or other_user.on_hold:
            print("One of the accounts is on hold.")
        elif other_user.pin == pin and self.password == password and amount <= other_user.balance:
            other_user.balance -= amount
            self.balance += amount
            return True
        else:
            return False
        


user1 = User("Bob", 1234, "password")
print(f"Name: {user1.name}, PIN: {user1.pin}, Password: {user1.password}")        
        



"""driver code for task 2
user1 = User("Bob", 1234, "password")
print(f"Name: {user1.name}, PIN: {user1.pin}, Password: {user1.password}")

user1.change_name("Alice")
user1.change_pin(4321)
user1.change_password("new_password")

print(f"Updated Name: {user1.name}, Updated PIN: {user1.pin}, Updated Password: {user1.password}")
       
"""

"""driver code for task 3

bank_user1 = BankUser("Alice", 4321, "new_password")
print(f"Name: {bank_user1.name}, PIN: {bank_user1.pin}, Password: {bank_user1.password}, Balance: {bank_user1.balance}")

        
        
"""

"""driver code for task 4

bank_user1 = BankUser("Alice", 4321, "new_password")

bank_user1.show_balance()

bank_user1.deposit(500)
bank_user1.show_balance()

bank_user1.withdraw(200)
bank_user1.show_balance()

  
"""

"""driver code for task 5

bank_user1 = BankUser("Alice", 4321, "new_password")
bank_user2 = BankUser("Bob", 1234, "password")

bank_user2.deposit(5000)
bank_user2.show_balance()
bank_user1.show_balance()

if bank_user2.transfer_money(bank_user1, 500, 1234):
    bank_user2.show_balance()
    bank_user1.show_balance()

    if bank_user2.request_money(bank_user1, 200, 4321, "new_password"):
        bank_user2.show_balance()
        bank_user1.show_balance()


        
        
"""