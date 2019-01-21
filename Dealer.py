from Hand import Hand
from Card import Card
class Dealer:

    def __init__(self, shoe, discard_pile):
        self.shoe = shoe
        self.discard_pile = discard_pile
        self.hand = Hand()
        self.show_whole_hand = False
        self.money = 0

    # Deal 2 cards to each player and the dealer
    def deal_cards(self, players):
        for i in range(2):
            for player in players:
                self.deal_card_to_player(player, 0)
            self.deal_card_to_dealer()

    def deal_card_to_player(self, player, hand_number):
        if self.shoe.is_empty():
            self.add_discard_to_shoe()
        card = self.shoe.remove_card()
        player.add_card_to_hand(card, hand_number)

    def deal_card_to_dealer(self):
        if self.shoe.is_empty():
            self.add_discard_to_shoe()
        # test constant blackjack
        # card = Card("Hearts", 11, 1, "Ace")
        card = self.shoe.remove_card()
        self.add_card_to_hand(card)

    # If there are less than 60 cards in shoe then add the discard pile back to shoe and shuffle the shoe
    def add_discard_to_shoe(self):
        cards = self.discard_pile.get_cards()
        self.discard_pile.clear()
        self.shoe.add_cards(cards)
        self.shoe.shuffle()

    def add_card_to_hand(self, card):
        self.hand.add_card_to_hand(card)

    # def hand_to_string(self):
    #     string = ""
    #     for card in self.hand:
    #         string += str(card.get_value()) + " "
    #     return string

    # def get_hand(self):
    #     if self.show_whole_hand:
    #         return self.hand
    #     return self.hand[:1]

    def get_up_card(self):
        return self.hand.get_cards()[0]

    def pop_hand(self):
        cards = self.hand.get_cards()
        self.hand = Hand()
        return cards

    def discard_hands(self, players):
        for player in players:
            self.discard_pile.add_cards(player.pop_hand())
        self.discard_pile.add_cards(self.pop_hand())

    def has_blackjack(self):
        if self.hand.get_hand_total() == 21:
            return True
        return False

    def hand_won(self, did_win):
        if did_win:
            self.money += 10
        else:
            self.money -= 10
