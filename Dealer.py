from Hand import Hand

class Dealer:

    def __init__(self, shoe, discard_pile):
        self.shoe = shoe
        self.discard_pile = discard_pile
        self.hand = []
        self.show_whole_hand = False

    # Deal 2 cards to each player and the dealer
    def deal_cards(self, players):
        for i in range(2):
            for player in players:
                self.deal_card_to_player(player)
            self.deal_card_to_dealer()

    def deal_card_to_player(self, player):
        if self.shoe.is_empty():
            self.add_discard_to_shoe()
        card = self.shoe.remove_card()
        player.add_card_to_hand(card)

    def deal_card_to_dealer(self):
        if self.shoe.is_empty():
            self.add_discard_to_shoe()
        card = self.shoe.remove_card()
        self.add_card_to_hand(card)

    # If there are less than 60 cards in shoe then add the discard pile back to shoe and shuffle the shoe
    def add_discard_to_shoe(self):
        cards = self.discard_pile.get_cards()
        self.discard_pile.clear()
        self.shoe.add_cards(cards)
        self.shoe.shuffle()

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def hand_to_string(self):
        string = ""
        for card in self.hand:
            string += str(card.get_value()) + " "
        return string

    def get_hand(self):
        if self.show_whole_hand:
            return self.hand
        return self.hand[:1]

    def get_up_card(self):
        return self.hand[0]

    def pop_hand(self):
        hand = self.hand
        self.hand = []
        return hand

    def discard_hands(self, players):
        for player in players:
            self.discard_pile.add_cards(player.pop_hand())
        self.discard_pile.add_cards(self.pop_hand())

    def has_blackjack(self):
        if self.hand.get_hand_total() == 21:
            return True
        return False
