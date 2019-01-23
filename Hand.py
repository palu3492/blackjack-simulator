
class Hand:

    def __init__(self):
        self.cards = []
        self.cards_value = 0
        self.bust = False
        self.bet = 10

    def add_card_to_hand(self, card):
        self.cards_value += card.get_value()
        self.cards.append(card)

    def hand_to_string(self):
        string = ""
        for card in self.cards:
            string += str(card.get_value()) + ", "
        return string

    # def get_hand_total(self):
    #     return self.cards_value

    def get_hand_total(self):
        # Adds up card values and returns hard total or soft total if ace and not over 21
        total = 0
        ace = False
        for card in self.cards:
            value = card.get_value()
            total += value
            if value == 1:
                ace = True
        if ace and total <= 11:
                total += 10
        return total

    def get_soft_total(self):
        # Treat ace as 11 (since ace value is 1 add 11)
        return self.cards_value + 10

    def get_non_ace_total(self):
        total = 0
        for card in self.cards:
            value = card.get_value()
            if value != 1:
                total += value
        return total

    def busted(self):
        self.bust = True

    def is_bust(self):
        return self.bust

    def set_cards(self, cards):
        # Set hand cards to array of cards
        self.cards = cards

    def get_cards(self):
        return self.cards

    def get_non_ace_card(self):
        if self.cards[0].get_value() == 1:
            return self.cards[1]
        return self.cards[0]

    # def pop_hand(self):
    #     cards = self.cards
    #     # Clear hand of cards
    #     self.cards = []
    #     self.cards_value = 0
    #     return cards

    def pull_last_card(self):
        card = self.cards.pop()
        self.cards_value -= card.get_value()
        return card

    def double_down(self):
        self.bet *= 2
        if self.get_hand_total() > 21:
            self.busted()

    def is_blackjack(self):
        if self.get_hand_total() == 21 and len(self.cards) == 2:
            return True
        return False
    def is_twenty_one(self):
        if self.get_hand_total() == 21:
            return True
        return False

    # Player gets paid 3:2 when they have blackjack
    def blackjack_multiplier(self):
        self.bet *= 1.5

    def push_blackjack_multiplier(self):
        self.bet *= 0.5

    def get_bet(self):
        return self.bet

    def is_ace_in_hand(self):
        for card in self.cards:
            if card.get_value() == 1:
                return True

    def is_pair(self):
        if self.cards[0].get_value() == self.cards[1].get_value():
            return True
        return False

    def is_soft(self):
        total = 0
        ace = False
        for card in self.cards:
            value = card.get_value()
            total += value
            if value == 1:
                ace = True
        if ace and total <= 11:
                return True
        return False
