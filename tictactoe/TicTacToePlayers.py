import numpy as np

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
    def __init__(self, game):
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

        allowed_moves = [
            [0, 0],
            [0, 1],
            [0, 2],
            [0, 3],
            [0, 4],
            [0, 5],
            [0, 6],
            [0, 7],
            [0, 8],

            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],

            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8]
        ]

        while True: 
            # Python 3.x
            a = input()
            # Python 2.x 
            # a = raw_input()

            move = [int(x) for x in a.split(' ')]
            i = 0
            for allowed_move in allowed_moves:
                if move == allowed_move:
                    return i
                i += 1
            return a

