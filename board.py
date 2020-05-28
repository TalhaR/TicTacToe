""" Represents the Board for the Game """
# import pygame


class Board:
    ROWS = COLS = 3

    def __init__(self):
        self.board = self.create_empty_board()
    
    # Operator[] Overload
    def __getitem__(self, row):
        return self.board[row]

    def __setitem__(self, key, value):
        self.board[key] = value

    def __str__(self):
        s = ""
        for row in self.board:
            for col in row:
                s += col + " "
            s += "\n"
        return s

    def create_empty_board(self):
        return [['_' for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def clear(self):
        self.board = self.create_empty_board()

    def check(self):
        b = self.board
        # Checks Horizontally
        for i in range(3):
            if self.board[i].count('X') == 3:
                print('X won')
                break
            if self.board[i].count('O') == 3:
                print('O won')
                break

        # Checks Vertically
        for i in range(3):
            if b[0][i] == b[1][i] == b[2][i] == 'X':
                print('X won')
                break
            if b[0][i] == b[1][i] == b[2][i] == 'O':
                print('O won')
                break

        # Checks Diagonals
        for _ in ('X', 'O'):
            if b[0][0] == b[1][1] == b[2][2]:
                print(f'{_} won')
                break
            if b[0][2] == b[1][1] == b[2][0]:
                print(f'{_} won')
                break
