import datetime
from random import randint
from variables import *


def generate_sudoku_solved():
    start_time = datetime.datetime.now()
    matrix = np.full((9, 9), 0)
    x_size = matrix.shape[0]
    y_size = matrix.shape[1]

    number = 1
    cnt = 0
    correct = False
    fail = 0
    trials_limit = 100
    undo_number_limit = 5

    while number <= 9:
        exit_for = False
        for i in range(0, 8, 3):
            for j in range(0, 8, 3):
                while cnt <= trials_limit:
                    row = randint(i, i + 2)
                    col = randint(j, j + 2)
                    if matrix[row, col] == 0:
                        if not number in matrix[row, :] and not number in matrix[:, col]:
                            matrix[row, col] = number
                            break
                    cnt = cnt + 1
                if cnt >= trials_limit:
                    fail = fail + 1
                    for x in range(x_size):
                        for y in range(y_size):
                            if matrix[x, y] == number:
                                matrix[x, y] = 0
                    if fail > undo_number_limit:
                        number = number - 1
                        fail = 0
                    correct = False
                    cnt = 0
                    exit_for = True
                    break
                else:
                    correct = True
                cnt = 0
            if exit_for:
                break
        if correct:
            number = number + 1
            fail = 0
    print('sudoku board generated in: ' + str(datetime.datetime.now() - start_time))
    return matrix


def generate_sudoku_to_play(empty_fields, sudoku_solved):
    sudoku_to_play = np.full((9, 9), 0)
    cleared = 0
    for i in range(9):
        for j in range(9):
            sudoku_to_play[i, j] = sudoku_solved[i, j]
    while cleared < empty_fields:
        x = randint(0, 8)
        y = randint(0, 8)
        if sudoku_to_play[x, y] != 0:
            sudoku_to_play[x, y] = 0
            cleared = cleared + 1
    print('Numbers removed from the board: ' + str(cleared))
    return sudoku_to_play


def get_empty_fields(X):
    if X == LEV_E_POSITION_X:
        empty_fields = 30
    elif X == LEV_M_POSITION_X:
        empty_fields = 40
    elif X == LEV_H_POSITION_X:
        empty_fields = 50

    return empty_fields