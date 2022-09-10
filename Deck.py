from Card import Card


class Deck:

    """
    Represents a standard 52 card deck
    Has some specific values that apply to only Blackjack like how face cards have the value of 10
    """

    def __init__(self):
        self.cards = []
        self.names = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
                      "King"]
        self.fill_deck()

    def fill_deck(self):
        """Adds all 52 cards to deck"""
        for suit in ["Hearts", "Spades", "Diamonds", "Clubs"]:
            for real_value in range(1, 14):
                # If 10 or higher than a face card which will have a value of 10 in blackjack (10-13)
                if real_value > 9:
                    value = 10
                else:
                    value = real_value
                card = Card(suit, value, real_value, self.names[real_value-1])
                self.cards.append(card)

    def get_deck(self):
        """Returns all the cards in deck"""
        return self.cards

    def set_deck(self, cards):
        """Takes an array of cards and replaces current cards in deck with these cards"""
        self.cards = cards

    def add_card(self, card):
        """Adds a card to deck"""
        self.cards.append(card)

    def clear_deck(self):
        """Removes all cards from deck"""
        self.cards.clear()

    def __str__(self):
        """Returns string representing all cards in the deck"""
        string = ""
        for card in self.cards:
            string += str(card.get_value())+","
        return string[:len(string)-1]
