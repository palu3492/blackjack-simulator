from Hand import Hand


class Player:

    def __init__(self, rules):
        self.rules = rules
        self.hands = [Hand()]
        self.money = 0 # User enters in how much money the players have (might not matter)
        self.money_lost = 0
        self.money_won = 0

    def add_card_to_hand(self, card, hand_number):
        hand = self.hands[hand_number]
        hand.add_card_to_hand(card)
        if hand.get_hand_total() > 21:
            hand.busted()

    # def hand_to_string(self):
    #     string = ""
    #     for card in self.hand:
    #         string += str(card.get_value()) + " "
    #     return string

    #return either (H)it, (S)tand, (D)ouble down, S(P)lit,
    def make_move(self, dealers_up_card, hand_number):
        # Reference rules using my cards and dealer up card
        # Check if you bust first
        hand = self.hands[hand_number]
        cards_in_hand = hand.get_cards()
        if hand.get_hand_total() > 21:
            hand.busted()
        else:
            if len(cards_in_hand) == 2:
                # Is hand is a pair
                if cards_in_hand[0].get_value() == cards_in_hand[1].get_value():
                    return self.rules.get_pair_move(cards_in_hand[0], dealers_up_card)
            else:
                # If hand contains a ace
                # Only soft when ace is 11 so check that it can be 11 without bust
                if hand.is_ace_in_hand() and hand.get_soft_total() <= 21:
                    return self.rules.get_soft_total_move(hand.get_hand_total()-1, dealers_up_card)
                # If no ace or pair in hand
                # Or ace is treated as 1 because 11 would bust
                else:
                    return self.rules.get_hard_total_move(hand.get_hand_total(), dealers_up_card)

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

    def add_hand(self, card):
        hand = Hand()
        hand.add_card_to_hand(card)
        self.hands.append(hand)

    def dealer_blackjack(self):
        if self.hands[0].get_hand_total() != 21:
            self.hands[0].did_bust = True

    def get_hands(self):
        return self.hands

    def hand_won(self, did_win, hand):
        bet = hand.get_bet()
        if did_win:
            self.money += bet
            self.money_won += bet
        else:
            self.money -= bet
            self.money_lost += bet

    def print_winnings(self):
        print("Money: " + str(self.money))
        print("Money lost: " + str(self.money_lost))
        print("Money won: " + str(self.money_won))
