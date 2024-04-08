"""
class Player:
    max_hp = 4000 #class attribute shared by all instances of the class
    
player1 = Player()
print(player1.max_hp)

player2 = Player()
print(player2.max_hp)

Player.max_hp = 5000 #changing the class attribute
print(player1.max_hp)
print(player2.max_hp)
"""

class Player: 
    def __init__(self, name, hp): #constructor method with parameters list
        self.name = name
        self.hp = hp
        self.score = 0 
        
player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)

print("P1:", player1.name, "--HP", player1.hp, "--SCORE:", player1.score)
print("P2:", player2.name, "--HP", player2.hp, "--SCORE:", player2.score)

        
player1.hp += 500
player1.score += 100

print("P1:", player1.name, "--HP", player1.hp, "--SCORE:", player1.score)
print("P2:", player2.name, "--HP", player2.hp, "--SCORE:", player2.score)






    
    