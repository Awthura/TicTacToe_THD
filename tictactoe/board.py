import pygame
from .colors import RED, GREEN, WHITE, BLACK, BLUE, GREY, YELLOW
from .constants import GAMEFONT, WIDTH, HEIGHT, ROWS,  COLS, SQUARE_SIZE, LINE_WIDTH,  LINE_COLOR, PADDING, MARGIN

import numpy as np

class Board:
    def __init__(self):
        self.board=[] 
        self.initialize()
        self.occupied_squares = 0
        self.moves=[]
        self.state = "not_full"

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS-1):
            for col in range(row%2,COLS,2):
                pygame.draw.line(win, LINE_COLOR, ((row+1)*SQUARE_SIZE,0), ((row+1)*SQUARE_SIZE,WIDTH), LINE_WIDTH)
                pygame.draw.line(win, LINE_COLOR, (0, col*SQUARE_SIZE), (WIDTH, col*SQUARE_SIZE), LINE_WIDTH)

    def initialize(self):
        self.board = np.zeros((ROWS,COLS))
        self.occupied_squares = 0
        self.state = "not_full"

    def check_availablity(self, row, col):
        return self.board[row][col] == 0

    def available_squares(self):
        available_squares = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.check_availablity(row, col):
                    available_squares.append((row, col))
        return available_squares

    def occupy(self, row, col, turn):
        self.board[row][col] = turn
        self.occupied_squares += 1
        self.moves.append((row,col))
        self.check_fullstate()

    def is_empty(self):
        if np.sum(self.board) == 0:
            return True
        else:
            return False
    
    def is_full(self):
        if 0 in self.board:
            return False
        else:
            return True

    def check_fullstate(self):
        if self.is_full():
            self.state = "full"

    def determine_color(self, row ,col):
        if self.board[row][col] == 1:
            color = RED
        if self.board[row][col] == 2:
            color = GREEN
        return color

    def calc_pos(self,row,col):
        x = SQUARE_SIZE * col + SQUARE_SIZE //2 
        y = SQUARE_SIZE * row + SQUARE_SIZE //2 
        return x,y

    def update_board(self,win):
        RINGSIZE = 30
        radius = SQUARE_SIZE//2-PADDING

        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    color = self.determine_color(row,col)
                    x,y = self.calc_pos(row,col)
                    pygame.draw.circle(win,color,(x,y),radius)
                    pygame.draw.circle(win,BLACK,(x,y),radius-RINGSIZE)

    def catch_coordinate(self, x, y):
        row = int(y // SQUARE_SIZE)
        col = int(x // SQUARE_SIZE)
        return row,col

    def vertical_winline(self, screen, col):
        x = col * SQUARE_SIZE + SQUARE_SIZE//2
        pygame.draw.line( screen, YELLOW, (x, MARGIN), (x, HEIGHT - MARGIN), LINE_WIDTH)

    def horizontal_winline(self, screen, row):
        y = row * SQUARE_SIZE + SQUARE_SIZE//2
        pygame.draw.line( screen, YELLOW, (MARGIN, y), (HEIGHT - MARGIN, y), LINE_WIDTH)

    def slash_winline(self, screen):
        pygame.draw.line( screen, YELLOW, (MARGIN, HEIGHT-MARGIN) , (WIDTH-MARGIN,MARGIN), LINE_WIDTH)

    def backslash_winline(self, screen):
        pygame.draw.line( screen, YELLOW, (MARGIN,MARGIN) , (WIDTH-MARGIN, HEIGHT-MARGIN), LINE_WIDTH)

    def draw_winline(self, screen, cond):
        if cond != 0:
            if 1 <= cond and cond <= 3:
                self.vertical_winline(screen, cond - 1)
            if 4 <= cond and cond <= 6:
                self.horizontal_winline(screen, cond - 4)
            if cond == 7:
                self.slash_winline(screen)
            if cond == 8:
                self.backslash_winline(screen)

    