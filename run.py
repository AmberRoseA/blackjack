import random

class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def __str__(self):
        return f"{self.face} of {self.suit}"    
"""
Deck of cards and values
"""
class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards = [Card(suit, face) for suit in ["♠", "♥", "♦", "♣"]
                    for face in ["A", "2", "3", "4", "5", "6", "7", "8", "9", 
                "10", "J", "Q", "K"]]   
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("No more cards in the deck.")
            return None                 
    
    """
    cards = []
    suits = ["♠", "♥", "♦", "♣"]
    faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", 
                "10", "J", "Q", "K"]
    """            

    for suit in suits:
        for face in faces:
            cards.append([suit, face])

    def shuffle():
        random.shuffle(cards)

    def deal(number):
        dealt_cards = []
        for x in range(number):
            card = cards.pop()
            dealt_cards.append(card)
        return dealt_cards

    shuffle()
    print(cards)

"""
Dealing the cards
"""


"""
Calculate the totalof each hand
"""


"""
Check the winner
"""

# Game Welcome/ start/ rules of the game 
"""
def start_game():
   
    Start Game and explains the rules
   
    print("This is Blackjack !!!")
    print("The goal of the game is to get as close to 21 as possible without going over")
    print("You will be dealt two cards, and you can choose to hit or stick.")
    print("If you hit, you will be dealt another card. If you stick, your turn will end.")
    print("If you go over 21, you lose. If you get 21, you win. If you get closer to 21 than the dealer, you win. If the dealer gets closer to 21 than you, you lose. If you get 21 and the dealer gets 21, it's a tie.")

    player_name = input("Enter players name: \n")
    ready_to_start = input(f"Are you ready to start, {player_name} ?(y/n) \n")

    if ready_to_start == "y":
        print("Let's start the game!")
    elif ready_to_start == "n":
        print("Maybe next time, Goodbye")
    else:
        print("Invalid input. please enter 'y' or 'n'.")

start_game()                

"""




