import random

pips= random.randint(1,6)
print("You rolled the die .... it lands with", pips, "pips showing.")

prizes = ['car', '$10000', 'a pony', 'boat', '$1000000']

prize_won = random.choice(prizes)
print("You turn the wheel of fortune... it land on a prize of", prize_won + "!!!")

cards = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
random.shuffle(cards)
print("the cards are now in this order: ")
print(cards)
