
class Dealer:

    def __init__(self, shoe):
        self.shoe = shoe
        self.hand = []
        self.show_whole_hand = False

    def deal_card_to_palyer(self, player):
        player.add_card_to_hand(self.shoe.remove_card())

    def deal_card_to_dealer(self):
        card = self.shoe.remove_card()
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