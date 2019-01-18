from Rules import Rules

class Player:

    rules = Rules()

    def __init__(self):
        self.hand = []
        self.hand_total = 0
        self.bust = False

    def add_card_to_hand(self, card):
        self.hand_total += card.get_value()
        self.hand.append(card)

    def hand_to_string(self):
        string = ""
        for card in self.hand:
            string += str(card.get_value()) + " "
        return string

    #return either (H)it, (S)tand, (D)ouble down, (Sp)lit,
    def make_move(self, dealers_cards):
        #See if player has pair or one card is an ace
        total = self.get_hand_total()
        if total >=17:
            return "S"
        else:
            return "H"

    def get_hand_total(self):
        return self.hand_total

    def is_bust(self):
        return self.bust

    def reset_bust(self):
        self.bust = False

    def set_hand(self, hand):
        self.hand = hand

    def get_hand(self):
        return self.hand

    def pop_hand(self):
        hand = self.hand
        self.hand = []
        return hand
