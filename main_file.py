from functions_draw_sudoku import *
from functions_generate_boards import *
from variables import *


while RUNNING:
    SCREEN.fill((230, 230, 230))
    draw_menu(X, IS_MENU_SELECTED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            print(mouse_position)
            X = get_selected_cell(mouse_position)[0]
            Y = get_selected_cell(mouse_position)[1]
            SELECT_SQUARE = True
            print(X)
            print(Y)
        if event.type == pygame.KEYDOWN:
            print('Pressed button')
            if event.key == pygame.K_1:
                VAL = 1
            elif event.key == pygame.K_2:
                VAL = 2
            elif event.key == pygame.K_3:
                VAL = 3
            elif event.key == pygame.K_4:
                VAL = 4
            elif event.key == pygame.K_5:
                VAL = 5
            elif event.key == pygame.K_6:
                VAL = 6
            elif event.key == pygame.K_7:
                VAL = 7
            elif event.key == pygame.K_8:
                VAL = 8
            elif event.key == pygame.K_9:
                VAL = 9
            elif event.key == pygame.K_DELETE:
                VAL = 0
            elif event.key == pygame.K_LEFT:
                X = max(X - 1, 0)
            elif event.key == pygame.K_RIGHT:
                X = min(X + 1, 8)
            elif event.key == pygame.K_UP:
                Y = max(Y - 1, 0)
            elif event.key == pygame.K_DOWN:
                Y = min(Y + 1, 8)
            elif event.key == pygame.K_g:
                IS_CHECKED = False
                IS_MENU_SELECTED = False
                NUMBER_PRESSED = False
                ARRAY_SOLVED = generate_sudoku_solved()
                ARRAY_USER = generate_sudoku_to_play(EMPTY_FIELDS, ARRAY_SOLVED)
                for i in range(9):
                    for j in range(9):
                        ARRAY_DEF[i, j] = ARRAY_USER[i, j]
                X = 0
                Y = 0
                EMPTY_FIELDS = 81
            elif event.key == pygame.K_c:
                IS_CHECKED = True
            elif event.key == pygame.K_s:
                for i in range(9):
                    for j in range(9):
                        ARRAY_USER[i, j] = ARRAY_SOLVED[i, j]
                IS_CHECKED = True
            else:
                VAL = -1
            if VAL >= 0 and VAL <= 9:
                NUMBER_PRESSED = True
            else:
                NUMBER_PRESSED = False

    draw_board(ARRAY_USER, ARRAY_DEF)
    draw_line()

    if SELECT_SQUARE == True and X in (LEV_E_POSITION_X, LEV_M_POSITION_X, LEV_H_POSITION_X) and Y == 1:
        EMPTY_FIELDS = get_empty_fields(X)
        IS_MENU_SELECTED = True
    if SELECT_SQUARE == True and X < 9 and Y < 9:
        highlight_cell(X, Y)
        if NUMBER_PRESSED == True and ARRAY_DEF[Y, X] == 0:
            ARRAY_USER[Y, X] = VAL
            print('User: ' + str(ARRAY_USER[Y, X]) + ' Def: ' + str(ARRAY_DEF[Y, X]))
            NUMBER_PRESSED = False
        else:
            VAL = -1
            NUMBER_PRESSED = False

    if IS_CHECKED:
        SELECT_SQUARE = False
        NUMBER_PRESSED = False
        check_sudoku(ARRAY_USER, ARRAY_DEF, ARRAY_SOLVED)

    pygame.display.update()
