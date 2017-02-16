class Card():

    def __init__(self, points, money, cost):
        self.points = points
        self.money = money
        self.cost = cost

    def __str__(self):
        if (self.points != 0):
            return 'V' + str(self.points)
        return 'C' + str(self.money)

    def __repr__(self):
        return self.__str__()


class PileOfCards():

    def __init__(self, card, number):
        self.card = card
        self.number = number

    def remove_card(self):
        if (self.number > 0):
            self.number -= 1
            return Card(self.card.points, self.card.money, self.card.cost)
        else:
            raise Error('cannot remove card from pile')

    def __str__(self):
        return str(self.number) + ": " + str(self.card)

    def __repr__(self):
        return self.__str__()
