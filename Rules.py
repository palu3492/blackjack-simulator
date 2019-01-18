
class Rules:

    def __init__(self):
        self.hard_rules = {} # 1 - 16 (20, 1): 'S'
        self.soft_rules = {} # 17 - 25
        self.pair_rules = {} # 26 - 35
        self.file_name = "rules.csv"
        self.read_rules_file()

    def read_rules_file(self):
        file = open(self.file_name, "r")
        lines = file.readlines()

        # Read and save hard total rules
        for line in lines[1:17]:
            moves = line.strip('\n').split(',')
            hard_total = moves[0]
            for dealer_card in range(1,11):
                self.hard_rules[(int(hard_total), dealer_card)] = moves[dealer_card]

        # Read and save soft total rules
        for line in lines[18:27]:
            moves = line.strip('\n').split(',')
            non_ace_card = moves[0]
            for dealer_card in range(1,11):
                self.soft_rules[(int(non_ace_card), dealer_card)] = moves[dealer_card]

        # Read and save pair rules
        for line in lines[28:]:
            moves = line.strip('\n').split(',')
            pair_number = moves[0].split(' ')[1]
            for dealer_card in range(1, 11):
                self.pair_rules[(int(pair_number), dealer_card)] = moves[dealer_card]

    def get_hard_total_move(self, hard_total, dealer_card):
        return self.hard_rules[(hard_total, dealer_card)]

    def get_soft_total_move(self, soft_card, dealer_card):
        return self.soft_rules[(soft_card, dealer_card)]

    def get_pair_move(self, pair_number, dealer_card):
        return self.pair_rules[(pair_number, dealer_card)]