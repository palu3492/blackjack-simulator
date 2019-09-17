from Hand import Hand


class Player:

    def __init__(self, player_strategy, id, house_rules):
        self.player_strategy = player_strategy
        self.hands = [Hand()]
        self.money = 0 # User enters in how much money the players have (might not matter)
        self.money_lost = 0
        self.money_won = 0
        self.player_id = id
        self.split_number = 0
        self.house_rules = house_rules

    def add_card_to_hand(self, card, hand_number):
        hand = self.hands[hand_number]
        hand.add_card_to_hand(card)

    # def hand_to_string(self):
    #     string = ""
    #     for card in self.hand:
    #         string += str(card.get_value()) + " "
    #     return string

    # return either (H)it, (S)tand, (D)ouble down, S(P)lit,
    def make_move(self, dealer_up_card, hand_number):
        # Reference player rules using my cards and dealer up card
        # Check if you bust first
        hand = self.hands[hand_number]
        cards_in_hand = hand.get_cards()
        move = ""
        # print(str(hand.hand_to_string()) + "= " + str(hand.get_hand_total()))
        # print(dealers_up_card.get_value())
        if hand.get_hand_total() > 21:
            hand.busted()
            move = "B"
        else:
            # Is hand is a pair
            if hand.is_pair() and self.house_rules.can_split():
                move = self.player_strategy.get_pair_move(cards_in_hand[0], dealer_up_card)
            # If hand contains a ace
            # Only soft when ace is 11 so check that it can be 11 without bust
            # A soft hand contains an Ace that is being counted as eleven
            # Use total of all cards besides ace because more than two cards can still be soft total
            # Ace and a Six = soft 17
            elif hand.is_ace_in_hand() and hand.is_soft() and hand.get_soft_total() <= 21:
                move = self.player_strategy.get_soft_total_move(hand.get_non_ace_total(), dealer_up_card)
            # If no ace or pair in hand
            # Or ace is treated as 1 because 11 would bust the hand
            # Ace, Six and a Ten = hard 17
            else:
                move = self.player_strategy.get_hard_total_move(hand.get_hand_total(), dealer_up_card)
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
    def pop_hands(self):
        cards = []
        for hand in self.hands:
            cards += hand.get_cards()
        self.hands = [Hand()]
        return cards

    def split_hand(self, hand_number):
        self.split_number += 1
        card = self.hands[hand_number].pull_last_card()
        new_hand = Hand()
        new_hand.add_card_to_hand(card)
        self.hands.append(new_hand)

    def dealer_blackjack(self):
        if self.hands[0].get_hand_total() != 21:
            self.hands[0].did_bust = True

    def get_hands(self):
        return self.hands

    def hand_won(self, did_win, hand):
        bet = hand.get_bet()
        # print(bet)
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

    def get_player_id(self):
        return self.player_id

    def has_blackjack(self, hand):
        if hand.get_hand_total() == 21:
            return True
        return False

    def is_split(self):
        if len(self.hands) > 1:
            return True
        return False
