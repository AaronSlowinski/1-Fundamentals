def show_balance(balance):
    print(f"Account balance: ${balance}")

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return balance + amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    return balance - amount

def logout(name):
    print(f"Goodbye, {name}")