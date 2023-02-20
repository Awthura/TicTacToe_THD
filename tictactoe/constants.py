import pygame
from .colors import WHITE


WIDTH, HEIGHT = 600, 600 #This should be the same value
ROWS,  COLS = 3, 3
SQUARE_SIZE = HEIGHT//ROWS
LINE_WIDTH = 15
LINE_COLOR = WHITE
PADDING = 10
MARGIN = 15
TEXTMARGIN_x = HEIGHT//7
TEXTMARGIN_Y = WIDTH//20
FONTSIZE = 30

pygame.font.init() 
GAMEFONT = pygame.font.SysFont('Comic Sans MS', FONTSIZE)