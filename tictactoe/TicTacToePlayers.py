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
            # [0, 8],
            # [0, 9],
            # [0, 10],
            # [0, 11],
            # [0, 12],
            # [0, 13],
            # [0, 14],
            # [0, 15],
            # [0, 16],
            # [0, 17],
            # [0, 18],
            # [0, 19],
            # [0, 20],
            # [0, 21],
            # [0, 22],
            # [0, 23],
            # [0, 24],
            # [0, 25],
            # [0, 26],
            # [0, 27],
            # [0, 28],
            # [0, 29],
            # [0, 30],
            # [0, 31],
            # [0, 32],
            # [0, 33],
            # [0, 34],
            # [0, 35],
            # [0, 36],
            # [0, 37],
            # [0, 38],
            # [0, 39],
            # [0, 40],

            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            # [1, 8],
            # [1, 9],
            # [1, 10],
            # [1, 11],
            # [1, 12],
            # [1, 13],
            # [1, 14],
            # [1, 15],
            # [1, 16],
            # [1, 17],
            # [1, 18],
            # [1, 19],
            # [1, 20],
            # [1, 21],
            # [1, 22],
            # [1, 23],
            # [1, 24],
            # [1, 25],
            # [1, 26],
            # [1, 27],
            # [1, 28],
            # [1, 29],
            # [1, 30],
            # [1, 31],
            # [1, 32],
            # [1, 33],
            # [1, 34],
            # [1, 35],
            # [1, 36],
            # [1, 37],
            # [1, 38],
            # [1, 39],
            # [1, 40],

            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            # [2, 8],
            # [2, 9],
            # [2, 10],
            # [2, 11],
            # [2, 12],
            # [2, 13],
            # [2, 14],
            # [2, 15],
            # [2, 16],
            # [2, 17],
            # [2, 18],
            # [2, 19],
            # [2, 20],
            # [2, 21],
            # [2, 22],
            # [2, 23],
            # [2, 24],
            # [2, 25],
            # [2, 26],
            # [2, 27],
            # [2, 28],
            # [2, 29],
            # [2, 30],
            # [2, 31],
            # [2, 32],
            # [2, 33],
            # [2, 34],
            # [2, 35],
            # [2, 36],
            # [2, 37],
            # [2, 38],
            # [2, 39],
            # [2, 40],
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

