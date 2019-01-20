
class Player:

    def __init__(self, rules):
        self.rules = rules
        self.hands = []

    def add_card_to_hand(self, card, hand_number):
        hand = self.hands[hand_number]
        hand.add_card_to_hand(card)

    # def hand_to_string(self):
    #     string = ""
    #     for card in self.hand:
    #         string += str(card.get_value()) + " "
    #     return string

    #return either (H)it, (S)tand, (D)ouble down, S(P)lit,
    def make_move(self, dealers_up_card):
        # Reference rules using my cards and dealers card
        # After initial deal round
        # Check if you bust first
        move = ""
        if len(self.hand) == 2:
            # Are hand is a pair
            if self.hand[0].get_value() == self.hand[1].get_value():
                move = self.rules.get_pair_move(self.hand[0].get_value(), dealers_up_card)
            # If hand contains a ace
            elif self.hand[0].get_value() == 1 or self.hand[1].get_value() == 1:
                move = self.rules.get_soft_total_move(self.get_non_ace(), dealers_up_card)
            # If no ace or pair in hand
            else:
                move = self.rules.get_hard_total_move(self.get_hand_total(), dealers_up_card)
        else:
            total = self.get_hand_total()
            if total >= 17:
                move = "S"
            else:
                move = "H"
        return move

    # def get_hand_total(self):
    #     return self.hand_total
    #
    # def is_bust(self):
    #     return self.bust
    #
    # def reset_bust(self):
    #     self.bust = False
    #
    # def set_hand(self, hand):
    #     self.hand = hand

    # def get_hand(self):
    #     return self.hand

    # def get_non_ace(self):
    #     if self.hand[0].get_value() == 1:
    #         return self.hand[1].get_value()
    #     return self.hand[0].get_value()
    #
    # def pop_hand(self):
    #     hand = self.hand
    #     self.hand = []
    #     self.hand_total = 0
    #     return hand
