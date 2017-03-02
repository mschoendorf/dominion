from card import Card, print_cards
from move import Move
import random
from collections import Counter


class Player():

    def __init__(self, id, strategy):
        self.id = id
        self.strategy = strategy
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
        return sum([c.treasure for c in self.hand])

    def total_points(self):
        return sum([c.points for c in self.deck]) + sum([c.points for c in self.hand]) + sum([c.points for c in self.discard])

    def buy_card(self, pile):
        if (pile is None):
            self.moves.append(Move(self.buying_power(), Card(0, 0, 0)))
        else:
            new_card = pile.remove_card()
            self.moves.append(Move(self.buying_power(), new_card))
            self.discard.append(new_card)

    def choose_card(self, piles):
        return self.strategy.choose_card(None, piles)

    def cleanup_phase(self):
        self.discard.extend(self.hand)
        self.hand = []
        self.draw_cards_into_hand()

    def play_hand(self, board):
        piles = board.affordable_piles(self.buying_power())
        pile = self.choose_card(piles)
        self.buy_card(pile)
        self.cleanup_phase()

    def print_moves(self):
        print('moves: ' + str(self.moves))

    def __str__(self):
        return 'id: ' + str(self.id) + ', score: ' + str(self.total_points()) + ', strategy: ' + str(self.strategy) + ',\nhand: ' + str(self.hand) + ',\ndeck: ' + print_cards(self.deck) + ',\ndiscard: ' + print_cards(self.discard)

    def __repr__(self):
        return self.__str__()
