def login (database, username, password):
    for user in database:
        if user['username'] == username and user['password'] == password:
            return True
    return False