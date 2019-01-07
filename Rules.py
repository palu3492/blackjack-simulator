
class Rules:

    def __init__(self):
        rules_set = {}
        self.read_rules_file()

    def read_rules_file(self):
        file = open("rules.csv", "r")
        lines = file.readlines()
        for i in range(1):
            for line in lines[1:]:
                line_split = line.split(",")
                card_value = line_split[0]
                print(card_value)