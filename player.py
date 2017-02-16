from card import Card
from move import Move
import random


class Player():

    def __init__(self, id):
        self.id = id
        self.deck = 7 * [Card(0, 1, 0)] + 3 * [Card(1, 0, 2)]
        self.hand = []
        self.discard = []
        self.moves = []
        self.shuffle_deck()
        self.draw_cards_into_hand()

    def shuffle_deck(self):
        self.deck.extend(self.discard)
        self.discard = []
        random.shuffle(self.deck)

    def draw_cards_into_hand(self, num=5):
        for i in range(num):
            if (len(self.deck) == 0 and len(self.discard) > 0):
                self.shuffle_deck()
            self.hand.append(self.deck.pop())

    def buying_power(self):
        return sum([c.money for c in self.hand])

    def total_points(self):
        return sum([c.points for c in self.deck]) + sum([c.points for c in self.hand]) + sum([c.points for c in self.discard])

    def choose_card(self, piles):
        # return random.choice(piles)
        return max(piles, key=lambda p: p.card.cost)

    def buy_card(self, pile):
        new_card = pile.remove_card()
        self.moves.append(Move(self.buying_power(), new_card))
        self.discard.append(new_card)
        self.discard.extend(self.hand)
        self.hand = []
        self.draw_cards_into_hand()

    def play_hand(self, board):
        piles = board.affordable_piles(self.buying_power())
        pile = self.choose_card(piles)
        self.buy_card(pile)

    def print_state(self):
        print('hand: ' + str(self.hand) + ',\ndeck: ' +
              str(self.deck) + ',\ndiscard: ' + str(self.discard))

    def print_moves(self):
        print('moves: ' + str(self.moves))

    def __str__(self):
        return 'id: ' + str(self.id) + ', score: ' + str(self.total_points()) + ', total moves: ' + str(len(self.moves)) + ',\nmoves: ' + str(self.moves) + ',\nhand: ' + str(self.hand) + ',\ndeck: ' + str(self.deck) + ',\ndiscard: ' + str(self.discard)

    def __repr__(self):
        return self.__str__()
