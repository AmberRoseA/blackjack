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
            else:
                value += int(card.face)

        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1            
            return value     

    def display(self, hide_dealer_first_card=False):
        print(f"{self.name}'s Hand")  
        for i, card in enumerate(self.cards):
            if hide_dealer_first_card and i == 0:
                print("?? Hidden Card ??")
            else:
                print(card)

        if not hide_dealer_first_card:
            print("Total value:", self.get_value())
            print()                             




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

            player_hand = Hand(player_name)
            dealer_hand = Hand("Dealer")

            # Deal first two card


            for _ in range(2)
                player_hand.add_card(self.deck.deal())
                dealer_hand.add_card(self.deck.deal())

            player_hand.display()
            dealer_hand.display(hide_dealer_first_card=True)  

            # Players turn
            while player_hand.get_value() < 21:
                choice = input("Hit or Stick? (h/s: ".lower())
                if choice == "h":
                    player_hand.add_card(self.deck.deal())
                    player_hand.display()
                elif choice == "s":
                    break
                else:
                    print("Invalid Entry!")

            player_score = player_hand.get_value()        
            # Dealers turn
            dealer_hand.display()
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(self.deck.deal())
                dealer_hand.display()

            dealer_score = dealer_hand.get_value()

            # Check winner
            if player_score > 21:
                print("BUST!! ... Dealer wins")
            elif dealer_score > 21:
                print("You WIN!! ... Dealer BUST!")  
            elif player_score == dealer_score:
                ("Tied Game")
            elif player_score > dealer_score:
                print(YOU WIN!!)
            else:
                print(Dealer WINS!!)              
            # Ask player to play again     

    start_game()                






