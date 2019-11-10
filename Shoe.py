import random

# Represents a standard blackjack shoe of cards that holds multiple decks of cards
class Shoe:

    def __init__(self, number_of_decks):
        self.cards = []
        self.number_of_decks = number_of_decks
        # Shoe insert shuffle card is placed in the last 60 to 75 cards where the shoe will be shuffled
        # Not dealing to the bottom of all the cards makes it more difficult for card counters to operate effectively
        self.shoe_insert = 60

    # Adds a deck to shoe, not cards
    def add_deck(self, deck):
        self.cards += deck.get_deck()

    # Shuffles the shoe
    def shuffle(self):
        random.shuffle(self.cards)

    # Returns true if shoe has no cards in it
    def is_empty(self):
        # I think this > 60 is a poor implementation of the shoe insert card, I don't remember
        # Whatever it is, it's wrong
        if (self.number_of_decks == 1 and len(self.cards) > 0) or (self.number_of_decks > 1 and len(self.cards) > 60):
            return False
        return True

    # Returns the top card from the shoe
    def remove_card(self):
        return self.cards.pop(0)

    # Adds array of cards to shoe of cards
    def add_cards(self, cards):
        self.cards += cards

    # Returns string representation of shoe of cards
    def to_string(self):
        string = ""
        for card in self.cards:
            string += str(card.get_value()) + " "
        return string