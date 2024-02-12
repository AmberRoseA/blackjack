import random

SUITS = ["♠", "♥", "♦", "♣"]
FACES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


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
        self.reset()

    def reset(self):
        """ Reset the deck by creating a new set of cards.
        Also shuffling them.
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
            return None


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

        if self.name:
            print_msg_box(f"{self.name}'s Total:", self.get_value()) # revisit 
        if not hide_dealer_first_card:
            print("Dealers Total:", self.get_value())
            print()  



# This code was taken from stackoverflow.com link in README.md
def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'
    box += ''.join([f'║{space}{line:<{width}}{space}║\n'for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)
    # This code was taken from stackoverflow.com link in README.md
       

class Game:
    """ Class representing the Blackjack game.
    Asks for input of player name and if they are ready to play.
    Ask player if they want to play again.
    Starts the Game, creates rules for hit or stick.
    """
    msg = "The aim of the game: reach 21 without exceeding\n" \
        "You'll be dealt two cards and can choose to Hit or Stick,\n" \
        "Hit - You get delt another card,\n" \
        "Stick - Keep what you got and hope the Dealer doesnt get higher.\n" \
        "Good Luck !"

    print_msg_box(msg=msg, indent=5, title="♠ ♥ ♦ ♣ Welcome to Blackjack Blast! ♣ ♦ ♥ ♦ ♠")

    def __init__(self):
        self.deck = Deck()



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
                print("Please enter a name to start")
                continue

            ready_start = input(f"Ready to start, {player_name}?(y/n):\n")
            while ready_start not in ['y', 'n']:
                print("Invalid input. Please enter 'y' or 'n'.")
                ready_start = input(f"Ready to start, {player_name}?(y/n):\n")

            if ready_start == "y":
                print_msg_box('\nLets Play !\n', indent=10)
            elif ready_start == "n":
                print_msg_box('\nMaybe next time. Goodbye!\n', indent=10)
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

            player_hand = Hand(player_name)
            dealer_hand = Hand("Dealer")
            # Deal first two cards
            for _ in range(2):
                player_hand.add_card(self.deck.deal())
                dealer_hand.add_card(self.deck.deal())

            player_hand.display()
            dealer_hand.display(hide_dealer_first_card=True)

            # Player's turn
            while player_hand.get_value() < 21:
                choice = input("Hit or Stick? (h/s): \n").lower()
                if choice == "h":
                    player_hand.add_card(self.deck.deal())
                    player_hand.display()
                elif choice == "s":
                    break
                else:
                    print("Invalid entry!")

            player_score = player_hand.get_value()
            # Dealer's turn
            dealer_hand.display()
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(self.deck.deal())
                dealer_hand.display()

            dealer_score = dealer_hand.get_value()

            # Check winner
            if player_score > 21:
                print_msg_box('\nYou BUST! Dealer wins.\n', indent=10)
            elif dealer_score > 21:
                print_msg_box('\nYou WIN! Dealer BUST!\n', indent=10)
            elif player_score == dealer_score:
                print_msg_box('\nTied game.\n', indent=10)
            elif player_score > dealer_score:
                print_msg_box('\nYOU WIN!\n', indent=10)
            else:
                print_msg_box('\nDealer WINS!\n', indent=10)

            while True:
                play_again = input("Want to play again? (y/n): \n").lower()
                if play_again == "y":
                    break
                elif play_again == "n":
                    print("Thanks for playing!")
                    return
                else:
                    print("Invalid entry. Please enter 'y' or 'n'.\n")


if __name__ == "__main__":
    game = Game()
    game.start_game()

