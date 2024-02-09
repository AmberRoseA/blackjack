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


class Hand:
    def __init__(self, name):
        self.cards = []
        self.name = name

    def add_card(self, card):
        sefl.cards.append(card)

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.face in ["J", "Q", "K"]:
                value += 10
            elif card.face == "A":
                value += 11
                num_aces += 1
            return value                




# Game Welcome/ start/ rules of the game 
class TheGame:
    def __init__(self):
        delf.deck = Deck()

    def start_game():
        while True:
            print("This is Blackjack!")
            print("The goal of the game is to get as close to 21 as possible without going over")
            print("You will be dealt two cards, and you can choose to Hit or Stick.")

            player_name = input("Enter players name: \n")
            ready_to_start = input(f"Are you ready to start, {player_name} ?(y/n) \n")

            if ready_to_start == "y":
                print("Let's start the game!")
                return TheGame
            elif ready_to_start == "n":
                print("Maybe next time, Goodbye")
            else:
                print("Invalid input. please enter 'y' or 'n'.")

            player_hand =
            dealer_hand =

            # Deal first two card
            # Players turn
            # Dealers turn
            # Check winner
            # Ask player to play again     

    start_game()                






