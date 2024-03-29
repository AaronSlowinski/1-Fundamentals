"""
ATM Work Shop 2
Aaron S.
Last updated: 03/30/2024

"""

from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
    
#declare a variable named name
while len(name) < 1 or len(name) > 10:
    name = input("Enter name to register: ")
    if len(name) < 1:
        print("Name must be at least 1 character long.")
    elif len(name) > 10:
        print("Name must be at most 10 characters long.")
        

#declare a variable named pin
pin = input("Enter PIN: ")
    
#declare a variable named balance
balance = 0

print(f"{name} has been registered with a starting balance of $: {str(balance)}")
    
while True:
    name_to_validate = input("Enter name to login: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("\n Login successful! ")
        break
    else:
        print("Invalid credentials!")
        

while True:
    atm_menu(name)  
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount > balance:
            print("Error: Insufficient funds. Current balance is $" + str(balance))
        else:
            balance -= withdraw_amount
            account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
    else:
        print("Invalid option, please try again.")
