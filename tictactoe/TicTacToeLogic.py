"""
Board class for the game of TicTacToe.
Default board size is 3x3.
Board data:
  1=white(O), -1=black(X), 0=empty
  first dim is column , 2nd is row:
     pieces[0][0] is the top left square,
     pieces[2][0] is the bottom left square,
Squares are stored and manipulated as (x,y) tuples.

Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.

Based on the board for the game of Othello by Eric P. Nichols.

"""
# from bkcharts.attributes import color
import numpy as np


class Board:

    # list of all 8 directions on the board, as (x,y) offsets
    __directions = [
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
    ]

    def __init__(self, n=3):
        "Set up initial board configuration."

        self.n = n
        # Create the empty board array.
        self.pieces = np.zeros(shape=(n, n))

    # add [][] indexer syntax to the Board
    def __getitem__(self, index):
        return self.pieces[index]

    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black)
        @param color not used and came from previous version.        
        """
        moves = set()  # stores the legal moves.

        # Get all the empty squares (color==0)
        for y in range(self.n):
            for x in range(self.n):
                if self[x][y] == 0:
                    newmove = (x, y)
                    moves.add(newmove)
        return list(moves)

    def has_legal_moves(self):
        for y in range(self.n):
            for x in range(self.n):
                if self[x][y] == 0:
                    return True
        return False

    def is_win(self, color):
        """Check whether the given player has collected a triplet in any direction; 
        @param color (1=white,-1=black)
        """
        win_3 = 3
        win_array = "".join(
            str(int(x)) for x in np.array([color for _ in range(win_3)])
        )
        board = np.copy(self.pieces)
        size = self.n
        transposed_array = board.transpose()

        # Ось X
        for x in range(size):
            x_array = "".join(str(int(x)) for x in board[x])
            if win_array in x_array:
                return True

        # Ось Y
        for y in range(size):
            x_array = "".join(str(int(x)) for x in transposed_array[y])
            if win_array in x_array:
                return True

        # Диагонали
        for diagonal in range(board.shape[1] - 1, -board.shape[0], -1):
            diag = board.diagonal(diagonal)
            if len(diag) > 3:
                string_diagonal = "".join(str(int(x)) for x in diag)

                if win_array in string_diagonal:
                    return True

        # Если ничего не нашли то False
        return False

    def execute_move(self, move, color):
        """Perform the given move on the board; 
        color gives the color pf the piece to play (1=white,-1=black)
        """

        (x, y) = move

        # Add the piece to the empty square.
        assert self[x][y] == 0
        self[x][y] = color
