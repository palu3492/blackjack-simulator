
class Hand:

    def __init__(self):
        self.cards = []
        self.total = 0
        self.bust = False

    def add_card_to_hand(self, card):
        self.total += card.get_value()
        self.cards.append(card)

    def hand_to_string(self):
        string = ""
        for card in self.cards:
            string += str(card.get_value()) + " "
        return string

    def get_hand_total(self):
        return self.total

    def did_bust(self):
        self.bust = True

    def is_bust(self):
        return self.bust

    def reset_bust(self):
        self.bust = False

    def set_cards(self, cards):
        # Set hand cards to array of cards
        self.cards = cards

    def get_cards(self):
        return self.cards

    def get_non_ace_card(self):
        if self.cards[0].get_value() == 1:
            return self.cards[1]
        return self.cards[0]

    def pop_hand(self):
        cards = self.cards
        # Clear hand of cards
        self.cards = []
        self.total = 0
        return cards
