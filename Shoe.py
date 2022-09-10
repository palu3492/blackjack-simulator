import random


class Shoe:

    """
    Represents a standard blackjack shoe holding multiple decks of cards
    """

    def __init__(self, number_of_decks):
        self.cards = []
        self.number_of_decks = number_of_decks
        # Shoe insert shuffle card is placed in the last 60 to 75 cards where the shoe will be shuffled
        # Not dealing to the bottom of all the cards makes it more difficult for card counters to operate effectively
        # TODO: Should not be hard codded
        self.shoe_insert = 60

    def add_deck(self, deck):
        """Adds a deck to shoe, not cards"""
        self.cards += deck.get_deck()

    def shuffle(self):
        """Shuffles the shoe"""
        random.shuffle(self.cards)

    def is_empty(self):
        """Returns true if shoe has no cards in it"""
        if (self.number_of_decks == 1 and len(self.cards) > 0) or \
                (self.number_of_decks > 1 and len(self.cards) > self.shoe_insert):
            return False
        return True

    def remove_card(self):
        """Returns the top card from the shoe"""
        return self.cards.pop(0)

    def add_cards(self, cards):
        """Adds array of cards to shoe of cards"""
        self.cards += cards

    def __str__(self):
        """Returns string representation of shoe of cards"""
        string = ""
        for card in self.cards:
            string += str(card.get_value()) + " "
        return string
