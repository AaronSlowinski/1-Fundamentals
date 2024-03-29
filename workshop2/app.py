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
name = input("Enter name to register: ")
    
#declare a variable named pin
pin = input("Enter PIN: ")
    
#declare a variable named balance
balance = 0
balance = str(input("Enter initial balance: "))

print (name + " has been registered with a balance of $" + balance)
    
