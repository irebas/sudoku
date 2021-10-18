import numpy as np
import datetime
from random import randint
from tabulate import tabulate

def generateSudokuSolved():
    startTime = datetime.datetime.now()
    matrix = np.full((9,9),0)
    xSize = matrix.shape[0]
    ySize = matrix.shape[1]

    number = 1
    cnt = 0
    correct = False
    fail = 0
    trialsLimit = 100
    undoNumberLimit = 5

    while number <= 9:
        exitFor = False
        for i in range(0, 8, 3):
            for j in range(0, 8, 3):
                while cnt <= trialsLimit:
                    row = randint(i, i + 2)
                    col = randint(j, j + 2)
                    if matrix[row, col] == 0:
                        if not number in matrix[row, :] and not number in matrix[:, col]:
                            matrix[row, col] = number
                            break
                    cnt = cnt + 1
                if cnt >= trialsLimit:
                    fail = fail + 1
                    for x in range(xSize):
                        for y in range(ySize):
                            if matrix[x, y] == number:
                                matrix[x, y] = 0
                    if fail > undoNumberLimit:
                        number = number - 1
                        fail = 0
                    correct = False
                    cnt = 0
                    exitFor = True
                    break
                else:
                    correct = True
                cnt = 0
            if exitFor == True:
                break
        if correct == True:
            number = number + 1
            fail = 0
    print('Sudoku board generated in: ' + str(datetime.datetime.now() - startTime))
    return matrix

def generateSudokuToPlay(eFields, sudokuToPlay):
    cleared = 0
    while cleared < eFields:
        x = randint(0, 8)
        y = randint(0, 8)
        if sudokuToPlay[x, y] != 0:
            sudokuToPlay[x, y] = 0
            cleared = cleared + 1
    matrix = sudokuToPlay
    print('Numbers removed from the board: ' + str(cleared))
    return matrix

def generateSudokuBoards(eFields):
    sudokuToPlay = np.full((9, 9), 0)
    # sudokuToPlayCopy = np.full((9, 9), 0)
    sudokuSolved = generateSudokuSolved()
    for i in range(9):
        for j in range(9):
            sudokuToPlay[i, j] = sudokuSolved[i, j]

    sudokuToPlay = generateSudokuToPlay(eFields, sudokuToPlay)
    # for i in range(9):
    #     for j in range(9):
    #         sudokuToPlayCopy[i, j] = sudokuToPlay[i, j]

    print('Sudoku solved:')
    print(sudokuSolved)
    print('Sudoku to play:')
    print(tabulate(sudokuToPlay, tablefmt="fancy_grid"))
    # print('Sudoku to play copy:')
    # print(sudokuToPlayCopy)

level = input('Please select level (Easy/Medium/Hard): ')
if level == 'Easy' or level == 'E':
    eFields = 30
elif level == 'Medium' or level == 'M':
    eFields = 40
elif level == 'Hard' or level == 'H':
    eFields = 50
else:
    print('Wrong level selected!')
    quit()

generateSudokuBoards(eFields)