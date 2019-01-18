
class Player:

    def __init__(self, rules):
        self.rules = rules
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
    def make_move(self, dealers_card):
        # Ace can be 1 or 11
        # reference rules using my cards and dealers card

        # After initial deal round
        if len(self.hand) == 2:
            # Are hand is a pair
            if self.hand[0].get_value() == self.hand[1].get_value():
                return self.rules.get_pair_move(self.hand[0].get_value(), dealers_card)
            # If hand contains a ace
            elif self.hand[0].get_value() == 1 or self.hand[1].get_value() == 1:
                return self.rules.get_soft_total_move(self.get_non_ace(), dealers_card)
            # If no ace or pair in hand
            else:
                return self.rules.get_hard_total_move(self.get_hand_total(), dealers_card)
        else:
            total = self.get_hand_total()
            if total >= 17:
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

    def get_non_ace(self):
        if self.hand[0].get_value() == 1:
            return self.hand[1].get_value()
        return self.hand[0].get_value()

    def pop_hand(self):
        hand = self.hand
        self.hand = []
        self.hand_total = 0
        return hand
