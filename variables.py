import pygame
import numpy as np

# Pygame window start parameters
pygame.init()
# Pygame window parameters
SCREEN = pygame.display.set_mode((700, 500))
ICON = pygame.image.load('duck.png')
pygame.display.set_caption('Sudoku')
pygame.display.set_icon(ICON)
RECT_SIZE = 50
FONT_NUMBERS = pygame.font.Font('freesansbold.ttf', 30)
FONT_MENU = pygame.font.SysFont('verdana', 20)
FONT_MENU2 = pygame.font.SysFont('verdana', 30)

# Default variables
VAL = -1
X = -1
Y = - 1

# Boolean variables
RUNNING = True
SELECT_SQUARE = False
NUMBER_PRESSED = False
IS_MENU_SELECTED = False
IS_CHECKED = False

# Screen position offsets
OFFSET_X = 17
OFFSET_Y = 12
LEV_E_POSITION_X = 10
LEV_M_POSITION_X = 11
LEV_H_POSITION_X = 12

# Arrays
ARRAY_DEF = np.full((9, 9), 0)
ARRAY_USER = np.full((9, 9), 0)
ARRAY_SOLVED = np.full((9, 9), 0)