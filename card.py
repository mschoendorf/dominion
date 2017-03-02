from collections import Counter


class Card():

    def __init__(self, points, treasure, cost):
        self.points = points
        self.treasure = treasure
        self.cost = cost

    def __str__(self):
        if (self.points != 0):
            return 'V' + str(self.points)
        if (self.treasure != 0):
            return 'T' + str(self.treasure)
        return 'Pass'

    def __repr__(self):
        return self.__str__()


class PileOfCards():

    def __init__(self, card, number):
        self.card = card
        self.number = number

    def remove_card(self):
        if (self.number > 0):
            self.number -= 1
            return Card(self.card.points, self.card.treasure, self.card.cost)
        else:
            raise Error('cannot remove card from pile')

    def __str__(self):
        return str(self.number) + ": " + str(self.card)

    def __repr__(self):
        return self.__str__()


def print_cards(cards):
    cardSet = Counter(cards)
    return str(cardSet)
