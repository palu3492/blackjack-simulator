import random

class Shoe:

    def __init__(self):
        self.cards = []

    def add_deck(self, deck):
        self.cards += deck.get_deck()

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_card(self):
        return self.cards.pop(0)

    def to_string(self):
        string = ""
        for card in self.cards:
            string += str(card.get_value()) + " "
        return string