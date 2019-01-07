
class Card:

    def __init__(self, suit, value, real_value, card_name):
        self.suit = suit
        self.value = value
        self.real_value = real_value
        self.card_name = card_name

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def get_real_value(self):
        return self.real_value

    def get_card_name(self):
        return self.card_name