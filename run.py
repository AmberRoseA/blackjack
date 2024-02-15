import random
import os
import sys

SUITS = ["♠", "♥", "♦", "♣"]
FACES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def print_box(msg=None, indent=0, width=None, title=None):
    """Print message-box with optional title.
    Not my original code from"""
    lines = msg
    space = " " * indent
    if not width:
        width = max(len(line) for line in lines)
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'
    for line in lines:
        box += f'║{space}{line.ljust(width)}{space}║\n'
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)


def dashed_underline(text):
    """ Create dashed underline for the given text."""
    return "--" * len(text)


class Card:
    """ Class to combine the suit and face,
    to show as one card
    """
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def __str__(self):
        return f"{self.face} {self.suit}"


class Deck:
    """ A Class to represent the deck of cards.
    Making a 52 card deck
    Removes card from deck onces it has been dealt so does not deal again.
    """
    def __init__(self):
        self.cards = []

    def shuffle_deck(self):
        """ Shuffling the deck which resets them,
        by creating a new set of cards.
        """
        self.cards = [Card(suit, face) for suit in SUITS for face in FACES]
        random.shuffle(self.cards)

    def deal(self):
        """ Deals the cards from the deck,
        If deck becomes empty returns None.
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("No more cards in the deck.")
            return


class Hand:
    """ Class to represent a hand of cards.
    List to store cards in the hand.
    Name associated with the hand.
    """
    def __init__(self, name):
        self.cards = []
        self.name = name

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        """ Calculates the hands total value.
        Give number value to "A" "K" "Q" "J".
        """
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
        """ Displays the players hand
        Hides one card of dealers hand on initial first deal.
        """
        rows = ["", "", "", "", ""]  # Text to display on each row.

        for card in self.cards:
            rows[0] += " ___  "  # Top line of card.
            if hide_dealer_first_card and card == self.cards[0]:
                rows[1] += "|XX | "
                rows[2] += "|XXX| "
                rows[3] += "|_XX| "
            else:
                rows[1] += "|{} | ".format(card.face.ljust(2))
                rows[2] += "| {} | ".format(card.suit)
                rows[3] += "|_{}| ".format(card.face.rjust(2, "_"))

        for row in rows:
            print(row)

        if not hide_dealer_first_card:
            print("Total value:", self.get_value())
        else:
            print("Total value: ????")
            print()


class Game:
    """ Class representing the Blackjack game.
    Asks for input of player name and if they are ready to play.
    Ask player if they want to play again.
    Starts the Game, creates rules for hit or stick.
    """
    def __init__(self):
        self.deck = Deck()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    intro_box = [
        "The aim of the game: reach 21 without exceeding",
        "You'll be dealt two cards and can choose to Hit or Stick",
        "Hit - You get delt another card",
        "Stick - Keep what you got and hope the Dealer doesnt get higher",
        "Good Luck !"
        ]

    print_box(msg=intro_box, indent=5, title="♠ ♥ ♦ ♣BlackjackBlast!♣ ♦ ♥ ♦ ♠")

    def start_game(self):
        """ Starts the game loop,
        Ask for players name and if they are ready to start.
        If entered invalid command will request again/ wont start game.
        Deals cards, requests player enter information to hit or stick (h/s).
        Checks for winner of game or if a player got 21 or Bust.
        Asks player if they want to play again.
        """
        while True:
            player_name = input("Enter your name: \n")
            if not player_name:
                print("Please enter a name to start: \n")
            else:
                break

        ready_start = input(f"Ready to start, {player_name}?(y/n):\n").lower()
        while ready_start not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
            ready_start = input(f"Ready to start ? (y/n):\n").lower()

        if ready_start == "n":
            print_box(msg="BYE", indent=8)
            sys.exit(0)
        elif ready_start == "y":
            print_box(msg="LETS PLAY", indent=5)

            player_hand = Hand(player_name)
            dealer_hand = Hand("Dealer")

            self.deck.shuffle_deck()

            # Deal first two cards
            for _ in range(2):
                player_hand.add_card(self.deck.deal())
                dealer_hand.add_card(self.deck.deal())

            print(f"-------{player_name}'s Hand:-------")
            player_hand.display()

            print("-------Dealer's Hand:-------")
            dealer_hand.display(hide_dealer_first_card=True)

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            # Player's turn
            while player_hand_value < 21:
                choice = input("Hit or Stick? (h/s): \n").lower()
                if choice == "h":
                    player_hand.add_card(self.deck.deal())
                    player_hand_value = player_hand.get_value()
                    print(f"-------{player_name}'s Hand:-------")
                    player_hand.display()
                elif choice == "s":
                    break
                else:
                    print("Invalid entry! \n")

            # Dealer's turn
            if player_hand_value <= 21:
                while dealer_hand_value < 17:
                    dealer_hand.add_card(self.deck.deal())
                    dealer_hand_value = dealer_hand.get_value()
                print("-------Dealer's Hand:-------")
                dealer_hand.display()

            # Check winner
            if player_hand_value > 21:
                print("========You BUST! Dealer wins.========")
            elif dealer_hand_value > 21:
                print("========You WIN! Dealer BUST!========")
            elif player_hand_value == dealer_hand_value:
                print("========Tied game========")
            elif player_hand_value > dealer_hand_value:
                print("========YOU WIN!========")
            else:
                print("========Dealer WINS!========")
        return


if __name__ == "__main__":
    while True:
        game = Game()
        game.start_game()
        while True:
            play_again = input("Want to play again? (y/n): \n").lower()
            if play_again not in ['y', 'n']:
                print("Invalid entry. Please enter 'y' or 'n'.\n")
            elif play_again == "n":
                print("Thanks for playing!")
                print_box(msg="BYE", indent=8)
                sys.exit(0)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
