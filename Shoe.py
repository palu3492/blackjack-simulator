import random

class Shoe:

    def __init__(self, number_of_decks):
        self.cards = []
        self.number_of_decks = number_of_decks
        # Cut card is placed so that the last 60 to 75 cards
        # Not dealing to the bottom of all the cards makes it more difficult for card counters to operate effectively

    def add_deck(self, deck):
        self.cards += deck.get_deck()

    def shuffle(self):
        random.shuffle(self.cards)

    def is_empty(self):
        if (self.number_of_decks == 1 and len(self.cards) >= 1) or (self.number_of_decks > 1 and len(self.cards) > 60):
            return False
        return True

    def remove_card(self):
        return self.cards.pop(0)

    def add_cards(self, cards):
        self.cards += cards

    def to_string(self):
        string = ""
        for card in self.cards:
            string += str(card.get_value()) + " "
        return string