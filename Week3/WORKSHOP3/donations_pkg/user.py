
def login(database, username, password):
    if username in database and database[username] == password:
        print("Welcome,", username)
        return username
    elif username in database and database[username] != password:
        print("Incorrect password")
        return ""
    else:
        print("Username not found")
        return ""

def register(database, username, password):
    if username in database:
        print("Username already registered.")
        return ""
    else:
        database[username] = password
        print("\nUsername has been registered.\n")
        return username
