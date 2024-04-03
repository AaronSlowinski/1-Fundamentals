def show_homepage():
    print("")
    print("      === DonateMe Homepage ===       ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register       |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("|               5. EXIT                  |")
    print("------------------------------------------")
    
def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation_string = username + " donated $" + "{:.2f}".format(donation_amt)
    print("Thank you for your donation " + donation_string)
