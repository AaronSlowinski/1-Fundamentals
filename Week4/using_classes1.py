class Player:
    max_hp = 4000 #class attribute shared by all instances of the class
    
player1 = Player()
print(player1.max_hp)

player2 = Player()
print(player2.max_hp)

Player.max_hp = 5000 #changing the class attribute
print(player1.max_hp)
print(player2.max_hp)
   