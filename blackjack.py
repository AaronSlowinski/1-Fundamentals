import random, sys

# Constants
HEARTS = 'Hearts'
DIAMONDS = 'Diamonds'
SPADES = 'Spades'
CLUBS = 'Clubs'

BACKSIDE='backside'

def main():
    print('Welcome to Blackjack!')
    print('You will be playing against the computer.')
    print('You start with $1000. Bet wisely.')
    
while True:
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank} of {suit}")
    random.shuffle(deck)