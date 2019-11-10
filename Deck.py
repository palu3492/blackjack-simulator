from Card import Card

# Represents a standard deck of cards that starts with 52 cards
# Has some specific values that apply to only Blackjack like how face cards have the value of 10
class Deck:

    def __init__(self):
        self.cards = []
        self.names = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        self.fill_deck()

    # Add all 52 cards to deck
    def fill_deck(self):
        for suit in ["Hearts", "Spades", "Diamonds", "Clubs"]:
            for real_value in range(1, 14):
                # if 10 or higher than a face card which will have a value of 10 in blackjack (10-13)
                if real_value > 9:
                    value = 10
                else:
                    value = real_value
                card = Card(suit, value, real_value, self.names[real_value-1])
                self.cards.append(card)

    # Returns all the cards in deck
    def get_deck(self):
        return self.cards

    # Takes an array of cards and replaces current cards in deck with these cards
    def set_deck(self, cards):
        self.cards = cards

    # Adds a card to deck
    def add_card(self, card):
        self.cards.append(card)

    # Removes all cards from deck
    def clear_deck(self):
        self.cards.clear()

    # Returns string representing all cards in deck
    def to_string(self):
        string = ""
        for card in self.cards:
            string += str(card.get_value())+","
        return string[:len(string)-1]