import numpy as np

from tictactoe.TicTacToeGame import TicTacToeGame

"""
Random and Human-ineracting players for the game of TicTacToe.

Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.

Based on the OthelloPlayers by Surag Nair.

"""
class RandomPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        a = np.random.randint(self.game.getActionSize())
        valids = self.game.getValidMoves(board, 1)
        while valids[a]!=1:
            a = np.random.randint(self.game.getActionSize())
        return a


class HumanTicTacToePlayer():
    def __init__(self, game: TicTacToeGame):
        self.game = game

    def find_subsequence(self, seq, subseq):
        target = np.dot(subseq, subseq)
        candidates = np.where(np.correlate(seq,
                                           subseq, mode='valid') == target)[0]
        # some of the candidates entries may be false positives, double check
        check = candidates[:, np.newaxis] + np.arange(len(subseq))
        mask = np.all((np.take(seq, check) == subseq), axis=-1)
        return candidates[mask]

    def play(self, board):
        # display(board)
        valid = self.game.getValidMoves(board, 1)

        allowed_moves = self.game.action_list()

        while True: 
            # Python 3.x
            unparsed_move = input("\nВведите координаты в формате 'Y X': ")
            # Python 2.x 
            # a = raw_input()

            splitted_move = unparsed_move.split(" ")

            parsed_move = []
            exc_raised = False
            for unparsed_literal in splitted_move:
                try:
                    parsed_literal = int(unparsed_literal)
                    parsed_move.append(parsed_literal)
                except ValueError:
                    if not exc_raised:
                        print('Неверные символы')
                    exc_raised = True

            if len(parsed_move) == 2:
                try:
                    index = allowed_moves.index(parsed_move)
                    return index
                except ValueError:
                    if not exc_raised:
                        print('Неверные координаты Value Error')
                    exc_raised = True
                except IndexError:
                    if not exc_raised:
                        print('Неверные координаты Index Error')
                    exc_raised = True
            else:
                if not exc_raised:
                    print('Длина  не совпадает')
                exc_raised = True
