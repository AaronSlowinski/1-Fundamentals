"""
ATM WorkShop 3 donations
Aaron S.
Last updated: 

"""

from donations_pkg.homepage import show_homepage

database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
    show_homepage() 
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)
    break