

class DiscardPile:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def add_cards(self, cards):
        self.cards += cards

    def get_cards(self):
        return self.cards

    def clear(self):
        self.cards = []
