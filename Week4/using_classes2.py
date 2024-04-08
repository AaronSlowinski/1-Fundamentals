class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    def change_password(self, password):
        self.password = password
        print("Password changed successfully", self.password)
            
user1 = User ("Jane","jane@nucamps.co","janespassword")
print(user1.password)

user1.change_password("bestpassword")