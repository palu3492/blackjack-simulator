
class Dealer:

    def __init__(self, shoe):
        self.shoe = shoe
        self.hand = []
        self.show_whole_hand = False

    # Give 2 cards to each player and the dealer
    def deal_cards(self, players):
        for i in range(2):
            for player in players:
                self.deal_card_to_player(player)
            self.deal_card_to_dealer()

    def deal_card_to_player(self, player):
        card = self.shoe.remove_card()
        player.add_card_to_hand(card)

    def deal_card_to_dealer(self):
        card = self.shoe.remove_card()
        self.add_card_to_hand(card)

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