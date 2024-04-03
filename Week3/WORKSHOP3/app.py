"""
ATM WorkShop 3 donations
Aaron S.
Last updated: 

"""

from donations_pkg.homepage import show_homepage, donate
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
    show_homepage() 
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)
    
    option = input("Please select an option: ")
    
    if option == "1":
        print("Login")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        authorized_user = login(database, username, password)
        print("\n")
        
        
    elif option == "2":
        print("Register")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
        print("\n")
        
    elif option == "3":
        print("Donate")
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
        print("\n")
        
    elif option == "4":
        print("TODO: Write Show Donations Functionality")
        
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")

