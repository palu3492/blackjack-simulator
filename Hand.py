
class Hand:

    def __init__(self):
        self.cards = []
        self.hand_total = 0
        self.bust = False

    def add_card_to_hand(self, card):
        self.hand_total += card.get_value()
        self.cards.append(card)

    def hand_to_string(self):
        string = ""
        for card in self.cards:
            string += str(card.get_value()) + " "
        return string

    def get_hand_total(self):
        return self.hand_total

    def is_bust(self):
        return self.bust

    def reset_bust(self):
        self.bust = False

    def set_cards(self, cards):
        self.cards = cards

    def get_cards(self):
        return self.cards

    def get_non_ace(self):
        if self.cards[0].get_value() == 1:
            return self.cards[1].get_value()
        return self.cards[0].get_value()

    def pop_hand(self):
        hand = self.cards
        self.cards = []
        self.hand_total = 0
        return hand