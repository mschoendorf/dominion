class Move():

    def __init__(self, buying_power, card):
        self.buying_power = buying_power
        self.card = card

    def __str__(self):
        return '$' + str(self.buying_power) + ': ' + str(self.card)

    def __repr__(self):
        return self.__str__()
