from variables import *
import math


def draw_menu(X, IS_MENU_SELECTED):
    text = FONT_MENU.render('Select level: ', True, (0, 0, 0))
    generate_text = FONT_MENU.render('G - generate/reset', True, (0, 0, 0))
    check_text = FONT_MENU.render('C - check', True, (0, 0, 0))
    solve_text = FONT_MENU.render('S - solve', True, (0, 0, 0))
    lev_l = FONT_MENU2.render('E', True, (0, 0, 0))
    lev_m = FONT_MENU2.render('M', True, (0, 0, 0))
    lev_h = FONT_MENU2.render('H', True, (0, 0, 0))
    SCREEN.blit(text, (9 * RECT_SIZE + 70, 10))
    SCREEN.blit(generate_text, (9 * RECT_SIZE + 50, 150))
    SCREEN.blit(check_text, (9 * RECT_SIZE + 50, 200))
    SCREEN.blit(solve_text, (9 * RECT_SIZE + 50, 250))
    if IS_MENU_SELECTED:
        pygame.draw.rect(SCREEN, (180, 180, 180), (X * RECT_SIZE, RECT_SIZE, RECT_SIZE, RECT_SIZE))
    SCREEN.blit(lev_l, (LEV_E_POSITION_X * RECT_SIZE + OFFSET_X - 3, RECT_SIZE))
    SCREEN.blit(lev_m, (LEV_M_POSITION_X * RECT_SIZE + OFFSET_X - 3, RECT_SIZE))
    SCREEN.blit(lev_h, (LEV_H_POSITION_X * RECT_SIZE + OFFSET_X - 3, RECT_SIZE))


def draw_board(ARRAY_USER, ARRAY_DEF):
    for y in range(9):
        for x in range(9):
            number = ARRAY_USER[y, x]
            text = FONT_NUMBERS.render(str(number), True, (0, 0, 0))
            if number == 0:
                pygame.draw.rect(SCREEN, (240, 240, 240), (x * RECT_SIZE, y * RECT_SIZE, RECT_SIZE, RECT_SIZE))
            elif ARRAY_USER[y, x] != ARRAY_DEF[y, x]:
                pygame.draw.rect(SCREEN, (255, 242, 204), (x * RECT_SIZE, y * RECT_SIZE, RECT_SIZE, RECT_SIZE))
                SCREEN.blit(text, ((x * RECT_SIZE) + OFFSET_X, (y * RECT_SIZE) + OFFSET_Y))
            elif number != 0:
                pygame.draw.rect(SCREEN, (189, 215, 238), (x * RECT_SIZE, y * RECT_SIZE, RECT_SIZE, RECT_SIZE))
                SCREEN.blit(text, ((x * RECT_SIZE) + OFFSET_X, (y * RECT_SIZE) + OFFSET_Y))


def draw_line():
    for i in range(10):
        if i in (0, 3, 6, 9):
            line_color = (0, 0, 0)
            thick = 2
        else:
            line_color = (150, 150, 150)
            thick = 1
        pygame.draw.line(SCREEN, line_color, (i * RECT_SIZE, 0), (i * RECT_SIZE, RECT_SIZE * 9), thick)
        pygame.draw.line(SCREEN, line_color, (0, i * RECT_SIZE), (RECT_SIZE * 9, i * RECT_SIZE), thick)


def input_number(x, y, number):
    pygame.draw.rect(SCREEN, (240, 240, 240), (x * RECT_SIZE, y * RECT_SIZE, RECT_SIZE, RECT_SIZE))
    text = FONT_NUMBERS.render(str(number), True, (0, 0, 0))
    SCREEN.blit(text, ((x * RECT_SIZE) + OFFSET_X, (y * RECT_SIZE) + OFFSET_Y))
    print(x)
    print(y)
    print(number)


def get_selected_cell(mouse_position):
    x = math.ceil(mouse_position[0] / RECT_SIZE) - 1
    y = math.ceil(mouse_position[1] / RECT_SIZE) - 1
    return x, y


def highlight_cell(x, y):
    pygame.draw.line(SCREEN, (192, 0, 0), (x * RECT_SIZE, y * RECT_SIZE), (x * RECT_SIZE, (y + 1) * RECT_SIZE), 2)
    pygame.draw.line(SCREEN, (192, 0, 0), ((x + 1) * RECT_SIZE, y * RECT_SIZE),
                     ((x + 1) * RECT_SIZE, (y + 1) * RECT_SIZE), 2)
    pygame.draw.line(SCREEN, (192, 0, 0), (x * RECT_SIZE, y * RECT_SIZE), ((x + 1) * RECT_SIZE, y * RECT_SIZE), 2)
    pygame.draw.line(SCREEN, (192, 0, 0), (x * RECT_SIZE, (y + 1) * RECT_SIZE),
                     ((x + 1) * RECT_SIZE, (y + 1) * RECT_SIZE), 2)


# Checking functions
def check_sudoku(ARRAY_USER, ARRAY_DEF, ARRAY_SOLVED):
    for y in range(9):
        for x in range(9):
            number = ARRAY_USER[y, x]
            text = FONT_NUMBERS.render(str(number), True, (0, 0, 0))
            if ARRAY_SOLVED[y, x] == ARRAY_USER[y, x] and ARRAY_DEF[y, x] == 0:
                pygame.draw.rect(SCREEN, (226, 240, 210), (x * RECT_SIZE, y * RECT_SIZE, RECT_SIZE, RECT_SIZE))
                SCREEN.blit(text, ((x * RECT_SIZE) + OFFSET_X, (y * RECT_SIZE) + OFFSET_Y))
            elif ARRAY_SOLVED[y, x] != ARRAY_USER[y, x] and ARRAY_DEF[y, x] == 0 and ARRAY_USER[y, x] != 0:
                pygame.draw.rect(SCREEN, (253, 170, 190), (x * RECT_SIZE, y * RECT_SIZE, RECT_SIZE, RECT_SIZE))
                SCREEN.blit(text, ((x * RECT_SIZE) + OFFSET_X, (y * RECT_SIZE) + OFFSET_Y))
    draw_line()
