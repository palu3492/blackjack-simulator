import config
import json


class PlayerStrategy:

    def __init__(self):
        self.hard_rules = {}  # 1 - 16 (20, 1): 'S'
        self.soft_rules = {}  # 17 - 25
        self.pair_rules = {}  # 26 - 35
        # csv file that holds the player's set of rules (strategy)
        self.file_name = config.player_settings['play_rules']
        self.read_rules_file()

    def read_rules_file(self):
        with open(self.file_name, "r") as read_file:
            data = json.load(read_file)

        # Fill in hand total rules
        for hand_total_type in data: # hard, soft, pair
            for hand_total in data[hand_total_type].keys(): # 21-5, 10-2, 10-1
                for dealer_up_card in data[hand_total_type][hand_total].keys(): #'21': 'A' or '21': '2'
                    key = (int(hand_total), int(dealer_up_card))
                    value = data[hand_total_type][hand_total][dealer_up_card]
                    if hand_total_type == 'hard':
                        self.hard_rules[key] = value
                    elif hand_total_type == 'soft':
                        self.soft_rules[key] = value
                    elif hand_total_type == 'pair':
                        self.pair_rules[key] = value

    def get_hard_total_move(self, hard_total, dealer_card):
        return self.hard_rules[(hard_total, dealer_card.get_value())]

    def get_soft_total_move(self, non_ace_total, dealer_card):
        return self.soft_rules[(non_ace_total, dealer_card.get_value())]

    def get_pair_move(self, pair_number, dealer_card):
        return self.pair_rules[(pair_number.get_value(), dealer_card.get_value())]
