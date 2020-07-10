""" Represents the Board for the Game """
from typing import List, Tuple
import pygame
import sys, os
from enum import Enum

# Colors (R, G, B)
WHITE_GREY = (215, 215, 215)
GREY = (75, 75, 75)

# This method can be ignored. It is for locating assets for PyInstaller
def resource_path(relative_path: str) -> str:
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class WinCondition(Enum):
    VERTICALLY = 1
    HORIZONTALLY = 2
    TOPLEFT_BOTTOMRIGHT = 3
    TOPRIGHT_BOTTOMLEFT = 4
    TIE = 5

class Board:
    ROWS = COLS = 3

    def __init__(self) -> None:
        self.board = self.create_empty_board()
        self.moves = 0
        self.match_ended = False
        self.x_turn = True
        self.tiles: List[pygame.Rect] = []
        # List of Tuples, where 1st elem is an obj and 2nd elem is a pos(x, y)
        self.player_moves: List[Tuple[pygame.Rect, Tuple[int, int]]] = []
        self.circle = self.x_mark = None
        # Storing starting and ending tiles to create a line later
        self.winning_tiles: Tuple[pygame.Rect, pygame.Rect]
        self.won_con: WinCondition
        self.load_assets()

    def __getitem__(self, row: int) -> List[str]:
        return self.board[row]

    def __setitem__(self, key: int, value: List[str]):
        self.board[key] = value

    # prints the string matrix out in the console
    def __str__(self) -> str:
        s = ""
        for row in self.board:
            for col in row:
                s += col + " "
            s += "\n"
        return s

    # returns a 3 x 3 matrix filled with '_'
    def create_empty_board(self) -> List[List[str]]:
        return [['_' for _ in range(self.COLS)] for _ in range(self.ROWS)]

    # clears the board and starts a new game
    def clear(self) -> None:
        self.board = self.create_empty_board()
        self.moves = 0
        self.match_ended = False
        self.player_moves.clear()

    # loads images and adds rectangles to tiles
    def load_assets(self) -> None:
        # creates 9 rectangles to place on screen
        for i in (0, 210, 420):
            for j in (0, 210, 420):
                self.tiles.append(pygame.Rect(j, i, 200, 200))
        # loads circle and x_mark assets
        self.circle = pygame.image.load(resource_path('assets/circle.png'))
        self.circle = pygame.transform.scale(self.circle, (195, 195))
        self.x_mark = pygame.image.load(resource_path('assets/X.png'))
        self.x_mark = pygame.transform.scale(self.x_mark, (195, 195))

    # Checks if the user clicked on any of the tiles. 
    # If they did then attempt to draw either an X or O there based on whose turn it is
    def make_move(self, pos: Tuple[int, int]) -> None:
        x, y = pos
        for index, rect in enumerate(self.tiles):
            if rect.collidepoint(x, y):
                x2, y2 = rect.topleft
                if self.x_turn:
                    self.draw_obj(self.x_mark, index, (x2 + 3, y2 + 3))
                else:
                    self.draw_obj(self.circle, index, (x2 + 3, y2 + 3))

    # :param obj either a circle or x_mark
    def draw_obj(self, obj: pygame.image, index: int, center: Tuple[int, int]) -> None:
        row = index // 3
        col = index % 3

        # only place "X" or "O" if the
        # original place is empty ("_")
        if self.place(row, col):
            self.player_moves.append((obj, center))
            self.x_turn = not self.x_turn


    # draws all the objects currently in the game onto the screen
    def update(self, screen: pygame.display):
        # Draws 9 Rectangles onto the screen
        for rect in self.tiles:
            pygame.draw.rect(screen, WHITE_GREY, rect)
        # Draws all player moves made
        for obj in self.player_moves:
            screen.blit(obj[0], obj[1])

        if self.match_ended and self.won_con != WinCondition.TIE:
            self.winning_animation(screen)

        pygame.display.update()

    # will attempt to place either an X or O at board[row][col]
    def place(self, row: int, col: int):
        if self.board[row][col] == "_":
            if self.x_turn:
                self.board[row][col] = "X"
            else:
                self.board[row][col] = "O"
            self.moves += 1
            return True
        return False

    # checks how the winner won and creates a straight line over those tiles
    def winning_animation(self, screen: pygame.display) -> None:
        start = self.winning_tiles[0]
        end = self.winning_tiles[1]
        if self.won_con == WinCondition.VERTICALLY:
            start = start.midtop
            end = end.midbottom
        elif self.won_con == WinCondition.HORIZONTALLY:
            start = start.midleft
            end = end.midright
        elif self.won_con == WinCondition.TOPLEFT_BOTTOMRIGHT:
            start = start.topleft
            end = end.bottomright
        elif self.won_con == WinCondition.TOPRIGHT_BOTTOMLEFT:
            start = start.topright
            end = end.bottomleft
        pygame.draw.line(screen, GREY, start, end, 15)

    # checks if the game is incomplete, tied or if there was a winner
    def check_if_over(self) -> bool:
        if self.match_ended: return True
        # Minimum of 5 turns before someone can win
        if self.moves < 5: return False
        if self.check_for_winner():
            self.match_ended = True
            return True
        # If board is filled and there's no winner then it's a tie
        if self.moves == 9:
            print("Tie")
            self.match_ended = True
            self.won_con = WinCondition.TIE
            return True
        return False

    # This method checks all 3 ways to win horizontally, vertically & diagonally
    # If a player won then it updates the won_condition & adds the winning tiles
    def check_for_winner(self) -> bool:
        b = self.board
        # Checks Horizontally
        for i in range(3):
            for mark in ('X', 'O'):
                if b[i].count(mark) == 3:
                    print(f'{mark} won H')
                    self.won_con = WinCondition.HORIZONTALLY
                    self.winning_tiles = (self.tiles[i * 3], self.tiles[i * 3 + 2])
                    return True

        # Checks Vertically
        for i in range(3):
            for mark in ('X', 'O'):
                if b[0][i] == b[1][i] == b[2][i] == mark:
                    print(f'{mark} won V')
                    self.won_con = WinCondition.VERTICALLY
                    self.winning_tiles = (self.tiles[i], self.tiles[6 + i])
                    return True

        # Checks Diagonals
        for mark in ('X', 'O'):
            if b[0][0] == b[1][1] == b[2][2] == mark:
                print(f'{mark} won D')
                self.won_con = WinCondition.TOPLEFT_BOTTOMRIGHT
                self.winning_tiles = (self.tiles[0], self.tiles[-1])
                return True
            if b[0][2] == b[1][1] == b[2][0] == mark:
                print(f'{mark} won D')
                self.won_con = WinCondition.TOPRIGHT_BOTTOMLEFT
                self.winning_tiles = (self.tiles[2], self.tiles[6])
                return True
        return False
