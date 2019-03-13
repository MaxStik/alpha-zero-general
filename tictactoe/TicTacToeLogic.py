'''
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

'''
# from bkcharts.attributes import color
import numpy as np


class Board():

    # list of all 8 directions on the board, as (x,y) offsets
    __directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]

    def __init__(self, p, n=3):
        "Set up initial board configuration."

        self.n = n
        self.p = p
        # Create the empty board array.
        self.pieces = np.zeros(shape=(n, p))

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
        for y in range(self.p):
            for x in range(self.n):
                if self[x][y]==0:
                    newmove = (x,y)
                    moves.add(newmove)
        return list(moves)

    def has_legal_moves(self):
        for y in range(self.p):
            for x in range(self.n):
                if self[x][y]==0:
                    return True
        return False

    def get_values_from_board(self, board: list):
        seq = []
        winners = [
            [
                [0, 0],
                [1, 0],
                [2, 0]
            ],
            [
                [0, 1],
                [1, 1],
                [2, 1]
            ],
            [
                [0, 2],
                [1, 2],
                [2, 2]
            ],
            [
                [0, 3],
                [1, 3],
                [2, 3]
            ],
            [
                [0, 4],
                [1, 4],
                [2, 4]
            ],
            [
                [0, 5],
                [1, 5],
                [2, 5]
            ],
            [
                [0, 6],
                [1, 6],
                [2, 6]
            ],
            [
                [0, 7],
                [1, 7],
                [2, 7]
            ],
            [
                [0, 8],
                [1, 8],
                [2, 8]
            ],
        ]
        for vector in winners:
            local_seq = []
            for item in vector:
                local_seq.append(board[item[0], item[1]])
            seq.append(local_seq)
        return seq

    def is_win_from_seq(self, board, winner):
        winners_combs = self.get_values_from_board(board)
        if winner in winners_combs:
            return True
        return False

    def is_win_old(self, color):
        """Check whether the given player has collected a triplet in any direction; 
        @param color (1=white,-1=black)
        """
        win = 3

        # check y-strips
        for y in range(self.p):
            count = 0
            for x in range(self.n):
                if self[x][y]==color:
                    count += 1
            if count==win:
                return True
        # # check x-strips
        for x in range(self.n):
            count = 0
            for y in range(self.p):
                if self[x][y]==color:
                    count += 1
            if count==win:
                return True
        # check two diagonal strips
        count = 0
        for d in range(self.n):
            if self[d][d]==color:
                count += 1
        if count==win:
            return True
        count = 0
        for d in range(self.n):
            if self[d][self.n-d-1]==color:
                count += 1
        if count==win:
            return True

        return False

    def find_subsequence(self, seq, subseq):
        target = np.dot(subseq, subseq)
        candidates = np.where(np.correlate(seq,
                                           subseq, mode='valid') == target)[0]
        # some of the candidates entries may be false positives, double check
        check = candidates[:, np.newaxis] + np.arange(len(subseq))
        mask = np.all((np.take(seq, check) == subseq), axis=-1)
        return candidates[mask]

    def is_win(self, color):
        """Check whether the given player has collected a triplet in any direction;
        @param color (1=white,-1=black)
        """
        win_array_3 = [color for _ in range(3)]
        board = np.copy(self.pieces)
        transposed_array = board.transpose()
        flipped_array = np.flip(board)

        # Ось X
        for x in range(self.n):
            x_array = board[x]
            if len(self.find_subsequence(x_array, win_array_3)) > 0:
                return True

        # Ось Y
        for y in range(self.p):
            x_array = transposed_array[y]
            if len(self.find_subsequence(x_array, win_array_3)) > 0:
                return True

        # Диагонали - главная
        for diagonal in range(board.shape[1] - 1, -board.shape[0], -1):
            diag = board.diagonal(diagonal)
            if self.find_subsequence(diag, win_array_3):
                return True

        # Диагонали - побочная
        for diagonal in range(flipped_array.shape[1] - 1, -flipped_array.shape[0], -1):
            diag = flipped_array.diagonal(diagonal)
            if self.find_subsequence(diag, win_array_3):
                return True

        # Если ничего не нашли то False
        return False

    def execute_move(self, move, color):
        """Perform the given move on the board; 
        color gives the color pf the piece to play (1=white,-1=black)
        """

        (x,y) = move

        # Add the piece to the empty square.
        assert self[x][y] == 0
        self[x][y] = color

