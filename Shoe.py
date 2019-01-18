import random

class Shoe:

    def __init__(self):
        self.cards = []
        # Plastic insert card is placed so that the last 60 to 75 cards
        # Not dealing to the bottom of all the cards makes it more difficult for professional card counters to operate effectively

    def add_deck(self, deck):
        self.cards += deck.get_deck()

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_card(self):
        if len(self.cards)  > 60:
            return self.cards.pop(0)
        else:
            # reshuffle shoe

    def to_string(self):
        string = ""
        for card in self.cards:
            string += str(card.get_value()) + " "
        return string