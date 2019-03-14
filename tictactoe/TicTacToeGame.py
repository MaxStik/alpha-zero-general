from __future__ import print_function
import sys

sys.path.append('..')
from Game import Game
from .TicTacToeLogic import Board
import numpy as np

"""
Game class implementation for the game of TicTacToe.
Based on the OthelloGame then getGameEnded() was adapted to new rules.

Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.

Based on the OthelloGame by Surag Nair.
"""


class TicTacToeGame(Game):
    def __init__(self, n=3, p=41):
        self.n = n
        self.p = p

    def getInitBoard(self):
        # return initial board (numpy board)
        b = Board(n=self.n, p=self.p)
        return np.array(b.pieces)

    def getBoardSize(self):
        # (a,b) tuple
        return (self.n, self.p)

    def getActionSize(self):
        # return number of actions
        return self.n * self.p + 1

    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        if action == self.n * self.p:
            return board, -player
        b = Board(n=self.n, p=self.p)
        b.pieces = np.copy(board)

        hell = [
            [0, 0],
            [0, 1],
            [0, 2],
            [0, 3],
            [0, 4],
            [0, 5],
            [0, 6],
            [0, 7],
            [0, 8],
            [0, 9],
            [0, 10],
            [0, 11],
            [0, 12],
            [0, 13],
            [0, 14],
            [0, 15],
            [0, 16],
            [0, 17],
            [0, 18],
            [0, 19],
            [0, 20],
            [0, 21],
            [0, 22],
            [0, 23],
            [0, 24],
            [0, 25],
            [0, 26],
            [0, 27],
            [0, 28],
            [0, 29],
            [0, 30],
            [0, 31],
            [0, 32],
            [0, 33],
            [0, 34],
            [0, 35],
            [0, 36],
            [0, 37],
            [0, 38],
            [0, 39],
            [0, 40],

            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28],
            [1, 29],
            [1, 30],
            [1, 31],
            [1, 32],
            [1, 33],
            [1, 34],
            [1, 35],
            [1, 36],
            [1, 37],
            [1, 38],
            [1, 39],
            [1, 40],

            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23],
            [2, 24],
            [2, 25],
            [2, 26],
            [2, 27],
            [2, 28],
            [2, 29],
            [2, 30],
            [2, 31],
            [2, 32],
            [2, 33],
            [2, 34],
            [2, 35],
            [2, 36],
            [2, 37],
            [2, 38],
            [2, 39],
            [2, 40],
        ]
        move = hell[action]
        b.execute_move(move, player)
        return b.pieces, -player

    def getValidMoves(self, board, player):
        # return a fixed size binary vector
        valids = [0] * self.getActionSize()
        b = Board(n=self.n, p=self.p)
        b.pieces = np.copy(board)
        legalMoves = b.get_legal_moves(player)
        if len(legalMoves) == 0:
            valids[-1] = 1
            return np.array(valids)
        for x, y in legalMoves:
            valids[self.p * x + y] = 1
        return np.array(valids)

    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        # player = 1
        b = Board(n=self.n, p=self.p)
        b.pieces = np.copy(board)

        if b.is_win(player):
            return 1
        if b.is_win(-player):
            return -1
        if b.has_legal_moves():
            return 0
        # draw has a very little value 
        return 1e-4

    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1
        return player * board

    def getSymmetries(self, board, pi):
        # mirror, rotational
        assert (len(pi) == self.n * self.p + 1)  # 1 for pass
        # pi_board = np.reshape(pi[:-1], (self.p, self.n))
        # l = []
        #
        # for i in range(1, 5):
        #     for j in [True, False]:
        #         newB = np.rot90(board, i)
        #         newPi = np.rot90(pi_board, i)
        #         if j:
        #             newB = np.fliplr(newB)
        #             newPi = np.fliplr(newPi)
        #         l += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return [[board, pi]]

    def stringRepresentation(self, board):
        # 8x8 numpy array (canonical board)
        return board.tostring()


def display(board):
    n = board.shape[0]
    p = board.shape[1]

    print("   ", end="")
    for y in range(p):
        print(y, "", end="")
    print("")
    print("  ", end="")
    for _ in range(p):
        print("-", end="-")
    print("--")
    for y in range(n):
        print(y, "|", end="")  # print the row #
        for x in range(p):
            piece = board[y][x]  # get the piece to print
            if piece == -1:
                print("X ", end="")
            elif piece == 1:
                print("O ", end="")
            else:
                if x == n:
                    print("- ", end="")
                else:
                    print("- ", end="")
        print("|")

    print("  ", end="")
    for _ in range(p):
        print("-", end="-")
    print("--")
