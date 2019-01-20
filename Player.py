from Hand import Hand
class Player:

    def __init__(self, rules):
        self.rules = rules
        self.hands = [Hand()]
        self.money = 1000 # User enters in how much money the players have (might not matter)
        self.money_lost = 0
        self.money_won = 0

    def add_card_to_hand(self, card, hand_number):
        self.hands[hand_number].add_card_to_hand(card)

    # def hand_to_string(self):
    #     string = ""
    #     for card in self.hand:
    #         string += str(card.get_value()) + " "
    #     return string

    #return either (H)it, (S)tand, (D)ouble down, S(P)lit,
    def make_move(self, dealers_up_card, hand_number):
        # Reference rules using my cards and dealers card
        # After initial deal round
        # Check if you bust first
        move = ""
        hand = self.hands[hand_number]
        cards_in_hand = hand.get_cards()
        if len(cards_in_hand) == 2:
            # Is hand is a pair
            if cards_in_hand[0].get_value() == cards_in_hand[1].get_value():
                move = self.rules.get_pair_move(cards_in_hand[0], dealers_up_card)
            # If hand contains a ace
            elif cards_in_hand[0].get_value() == 11 or cards_in_hand[1].get_value() == 11:
                move = self.rules.get_soft_total_move(hand.get_non_ace_card(), dealers_up_card)
            # If no ace or pair in hand
            else:
                move = self.rules.get_hard_total_move(hand.get_hand_total(), dealers_up_card)
        else:
            total = hand.get_hand_total()
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
    def pop_hand(self):
        cards = []
        for hand in self.hands:
            cards += hand.get_cards()
        self.hands = [Hand()]
        return cards

    def add_hand(self):
        self.hands.append(Hand())

    def dealer_blackjack(self):
        if self.hands[0].get_hand_total() != 21:
            self.hands[0].did_bust = True

    # def hand_won(self, did_win):
    #     if did_win:
    #         self.money += 10
    #         self.money_won += 10
    #     else:
    #         self.money -= 10
    #         self.money_lost += 10
