import random
from Card import Card

class Deck:

    names = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "10", "Jack", "Queen", "King"]

    def __init__(self):
        self.deck = []
        self.fill_deck()

    def fill_deck(self):
        for suit in ["Hearts", "Spades", "Diamonds", "Clubs"]:
            for real_value in range(1, 14):
                if real_value > 9:
                    value = 10
                else:
                    value = real_value
                card = Card(suit, value, real_value, Deck.names[real_value-1])
                self.deck.append(card)

    def get_deck(self):
        return self.deck

    def set_deck(self, cards):
        self.deck = cards

    def add_card(self, card):
        self.deck.append(card)

    def clear_deck(self):
        self.deck.clear()

    def to_string(self):
        string = ""
        for card in self.deck:
            string += str(card.get_value())+","
        return string[:len(string)-1]