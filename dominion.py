from card import Card, PileOfCards
from move import Move
from player import Player


class Board():

    def __init__(self, numberOfVictoryCards):
        self.piles_by_cost = {
            0: [PileOfCards(Card(0, 1, 0), 100)],
            2: [PileOfCards(Card(1, 0, 2), numberOfVictoryCards)],
            3: [PileOfCards(Card(0, 2, 3), 100)],
            5: [PileOfCards(Card(3, 0, 5), numberOfVictoryCards)],
            6: [PileOfCards(Card(0, 3, 6), 100)],
            8: [PileOfCards(Card(6, 0, 8), numberOfVictoryCards)]
        }
        self.province_cards = self.piles_by_cost[8][0]

    def is_game_over(self):
        return self.province_cards.number == 0

    def affordable_piles(self, max_cost):
        piles = []
        for i in range(max_cost + 1):
            if (i in self.piles_by_cost and len(self.piles_by_cost[i]) > 0):
                for pile in self.piles_by_cost[i]:
                    if pile.number > 0:
                        piles.append(pile)
        return piles

    def __str__(self):
        return str(self.piles_by_cost)

    def __repr__(self):
        return self.__str__()


class Game():

    def __init__(self, num_players):
        self.players = [Player(i) for i in range(num_players)]
        victory_cards = 8
        if (self.players > 3):
            victory_cards = 10
        self.board = Board(victory_cards)
        self.whose_turn = 0

    def play_turn(self):
        current_player = self.players[self.whose_turn]

        # play the turn
        current_player.play_hand(self.board)

        # check to see if it is over:
        if (self.board.is_game_over()):
            print('current player: ' + str(self.whose_turn))
            winner = self.who_won()
            print("winner: " + str(winner))
            print("losers: " +
                  str([p for p in self.players if p.id != winner.id]))
            print(self.board)
            return True
        else:
            self.whose_turn = (self.whose_turn + 1) % len(self.players)
            return False

    def who_won(self):
        return max(self.players, key=lambda p: p.total_points())


def main():
    game = Game(2)
    while(True):
        if (game.play_turn()):
            break

if __name__ == "__main__":
    main()
