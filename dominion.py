from card import Card, PileOfCards
from move import Move
from player import Player
from board import Board
import strategy
from collections import Counter


class Game():

    def __init__(self, players):
        self.players = players
        victory_cards = 8
        if (len(self.players) > 3):
            victory_cards = 10
        self.board = Board(victory_cards)
        self.whose_turn = 0

    def play_turn(self):
        current_player = self.players[self.whose_turn]

        # play the turn
        current_player.play_hand(self.board)

        # check to see if it is over:
        if (self.board.is_game_over()):
            return False
        else:
            self.whose_turn = (self.whose_turn + 1) % len(self.players)
            return True

    def play_game(self):
        i = 0
        while(self.play_turn()):
            i += 1
            if (i > 200):
                print('Too many turns! Ending game')
                break

    def who_won(self):
        return max(self.players, key=lambda p: p.total_points())

    def print_game_over_stats(self):
        winner = self.who_won()
        print("Winner: " + str(winner))
        print("Losers: ")
        print([p for p in self.players if p.id != winner.id])
        print(self.board)


def main():
    winners = Counter()
    for i in range(1000):
        players = [
            Player(0, strategy.Random()),
            Player(1, strategy.MostExpensive()),
            Player(2, strategy.MostExpensiveNoCheap())
        ]
        game = Game(players)
        game.play_game()
        winners.update([game.who_won().id])
    print(winners)

if __name__ == "__main__":
    main()
