""" Represents the Board for the Game """
# import pygame


class Board:
    ROWS = COLS = 3

    def __init__(self):
        self.board = self.create_empty_board()
        self.moves = 0
    
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
        self.moves = 0

    def place(self, row, col, x_turn):
        if self.board[row][col] == "_":
            if x_turn:
                self.board[row][col] = "X"
            else:
                self.board[row][col] = "O"
            self.moves += 1
            return True
        return False

    def check_for_winner(self):
        b = self.board

        if self.moves == 9:
            print("Tie")
            return True

        # Checks Horizontally
        for i in range(3):
            for mark in ('X', 'O'):
                if b[i].count(mark) == 3:
                    print(f'{mark} won H')
                    return True

        # Checks Vertically
        for i in range(3):
            for mark in ('X', 'O'):
                if b[0][i] == b[1][i] == b[2][i] == mark:
                    print(f'{mark} won V')
                    return True

        # Checks Diagonals
        for mark in ('X', 'O'):
            if b[0][0] == b[1][1] == b[2][2] == mark\
                    or b[0][2] == b[1][1] == b[2][0] == mark:
                print(f'{mark} won D')
                return True
        return False
