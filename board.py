""" Represents the Board for the Game """
import pygame
# import game
# from game import screen

# Colors (R, G, B)
BLACK = (0, 0, 0)
GREY_WHITE = (215, 215, 215)
BLUE = (0, 0, 255)


class Board:
    ROWS = COLS = 3

    def __init__(self):
        self.board = self.create_empty_board()
        self.moves = 0
        self.match_ended = False
        self.x_turn = True
        self.tiles = []
        self.player_moves = []
        self.circle, self.x_mark = None, None
        self.load_assets()
    
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

    def load_assets(self):
        # creates 9 rectangles to place on screen
        for i in (0, 210, 420):
            for j in (0, 210, 420):
                self.tiles.append(pygame.Rect(j, i, 200, 200))
        # loads circle and x_mark assets
        self.circle = pygame.image.load('assets/circle.png')
        self.circle = pygame.transform.scale(self.circle, (195, 195))
        self.x_mark = pygame.image.load('assets/X.png')
        self.x_mark = pygame.transform.scale(self.x_mark, (195, 195))

    def make_move(self, pos):
        x, y = pos
        for index, rect in enumerate(self.tiles):
            if rect.collidepoint(x, y):
                x2, y2 = rect.topleft
                if self.x_turn:
                    self.draw_obj(self.x_mark, index, (x2 + 3, y2 + 3))
                else:
                    self.draw_obj(self.circle, index, (x2 + 3, y2 + 3))

    def draw_obj(self, obj, index, center):
        row = index // 3
        col = index % 3

        # only place "X" or "O" if the
        # original place is empty ("_")
        if self.place(row, col, self.x_turn):
            self.player_moves.append((obj, center))
            # print(board)
            self.x_turn = not self.x_turn

    # def update(self):
    #     # Draws 9 Rectangles onto the screen
    #     for rect in self.tiles:
    #         pygame.draw.rect(screen, GREY_WHITE, rect)
    #     # Draws all player moves made
    #     for obj in self.player_moves:
    #         screen.blit(obj[0], obj[1])
    #
    #     # pygame.draw.line(screen, (0, 0, 255), (0, 0), (200, 200), 15)
    #
    #     pygame.display.update()

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
        if self.moves == 9:
            print("Tie")
            return True

        b = self.board
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
