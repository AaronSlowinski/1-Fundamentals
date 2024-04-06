"""
Regular Expresion Examples
By Jack Seymour
Date 6/13/22
"""

import re


def validate_username(username: str) -> bool:
    """
        Validate Username
        Return Bool
    """
    regex = "^[a-zA-Z][?=.*a-zA-Z0-9]*$"
    pattern = re.compile(regex)
    if re.search(pattern, username):
        return True
    return False


def change_passwd() -> str:
    """Validate and return password"""
    _p = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,21}$"
    regex = re.compile(_p)
    while True:
        new_passwd = input("New password: ")
        if not re.search(regex, new_passwd):
            print("Passwords must be 8-20 characters and contain: uppercase, lowercase, number, special character.")
            continue
        else:
            print(f"Password change successful! New password: {new_passwd}")
            return new_passwd


while True:
    if validate_username(input("Provide a username: ")):
        print("Valid")
        break
    else:
        print("Not Valid")


print(change_passwd())
