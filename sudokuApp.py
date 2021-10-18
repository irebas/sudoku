import numpy as np
import math
import pygame
import datetime
from random import randint

# Functions generating sudokuSolved / sudokuToPlay
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

def generateSudokuBoards(levelPosition):
    global arrayDef
    global arrayUser
    global arraySolved
    eFields = 0
    if levelPosition == levEpositionX:
        eFields = 30
    elif levelPosition == levMpositionX:
        eFields = 40
    elif levelPosition == levHpositionX:
        eFields = 50
    else:
        arrayDef = np.full((9, 9), 0)
        arrayUser = np.full((9, 9), 0)
        arraySolved = np.full((9, 9), 0)
        print('No level selected')
    if eFields > 0:
        sudokuToPlay = np.full((9, 9), 0)
        sudokuToPlayCopy = np.full((9, 9), 0)
        sudokuSolved = generateSudokuSolved()
        for i in range(9):
            for j in range(9):
                sudokuToPlay[i, j] = sudokuSolved[i, j]

        sudokuToPlay = generateSudokuToPlay(eFields, sudokuToPlay)
        for i in range(9):
            for j in range(9):
                sudokuToPlayCopy[i, j] = sudokuToPlay[i, j]

        arrayDef = sudokuToPlay
        arrayUser = sudokuToPlayCopy
        arraySolved = sudokuSolved

# Drawing functions
def drawMenu(x, isMenuSelected):
    text = font2.render('Select level: ', True, (0, 0, 0))
    generateText = font2.render('G - generate/reset', True, (0, 0, 0))
    checkText = font2.render('C - check', True, (0, 0, 0))
    solveText = font2.render('S - solve', True, (0, 0, 0))
    l = font3.render('E', True, (0, 0, 0))
    m = font3.render('M', True, (0, 0, 0))
    h = font3.render('H', True, (0, 0, 0))
    screen.blit(text, (9 * rectSize + 70, 10))
    screen.blit(generateText, (9 * rectSize + 50, 150))
    screen.blit(checkText, (9 * rectSize + 50, 200))
    screen.blit(solveText, (9 * rectSize + 50, 250))
    if isMenuSelected == True:
        pygame.draw.rect(screen, (180, 180, 180), (x * rectSize, rectSize, rectSize, rectSize))
    screen.blit(l, (levEpositionX * rectSize + offsetX - 3, rectSize))
    screen.blit(m, (levMpositionX * rectSize + offsetX - 3, rectSize))
    screen.blit(h, (levHpositionX * rectSize + offsetX - 3, rectSize))

def drawBoard():
    for y in range(9):
        for x in range(9):
            number = arrayUser[y, x]
            text = font.render(str(number), True, (0, 0, 0))
            if number == 0:
                pygame.draw.rect(screen, (240, 240, 240), (x * rectSize, y * rectSize, rectSize, rectSize))
            elif arrayUser[y, x] != arrayDef[y, x]:
                pygame.draw.rect(screen, (255, 242, 204), (x * rectSize, y * rectSize, rectSize, rectSize))
                screen.blit(text, ((x * rectSize) + offsetX, (y * rectSize) + offsetY))
            elif number != 0:
                pygame.draw.rect(screen, (189, 215, 238), (x * rectSize, y * rectSize, rectSize, rectSize))
                screen.blit(text, ((x * rectSize) + offsetX, (y * rectSize) + offsetY))

def drawLine():
    for i in range(10):
        if i in (0, 3, 6, 9):
            lineColor = (0, 0, 0)
            thick = 2
        else:
            lineColor = (150, 150, 150)
            thick = 1
        pygame.draw.line(screen, lineColor, (i * rectSize, 0), (i * rectSize, rectSize * 9), thick)
        pygame.draw.line(screen, lineColor, (0, i * rectSize), (rectSize * 9, i * rectSize), thick)

def inputNumber(x, y, number):
    pygame.draw.rect(screen, (240, 240, 240), (x * rectSize, y * rectSize, rectSize, rectSize))
    text = font.render(str(number), True, (0, 0, 0))
    screen.blit(text, ((x * rectSize) + offsetX, (y * rectSize) + offsetY))
    print(x)
    print(y)
    print(number)

def getSelectedCell(mousePosition):
    x = math.ceil(mousePosition[0] / rectSize) - 1 #x = round(x + 0.5) - 1
    y = math.ceil(mousePosition[1] / rectSize) - 1 #y = round(y + 0.5) - 1
    return x,y

def highlightCell(x, y):
    pygame.draw.line(screen, (192, 0, 0), (x * rectSize, y * rectSize), (x * rectSize, (y + 1) * rectSize), 2) #pionowaLewa
    pygame.draw.line(screen, (192, 0, 0), ((x + 1) * rectSize, y * rectSize), ((x + 1) * rectSize, (y + 1) * rectSize), 2) #pionowaPrawa
    pygame.draw.line(screen, (192, 0, 0), (x * rectSize, y * rectSize), ((x + 1) * rectSize, y * rectSize), 2) #poziomaGórna
    pygame.draw.line(screen, (192, 0, 0), (x * rectSize, (y + 1) * rectSize), ((x + 1) * rectSize, (y + 1) * rectSize), 2) #poziomaDolna

# Checking functions
def checkSudoku():
    for y in range(9):
        for x in range(9):
            number = arrayUser[y, x]
            text = font.render(str(number), True, (0, 0, 0))
            if arraySolved[y, x] == arrayUser[y, x] and arrayDef[y, x] == 0:
                pygame.draw.rect(screen, (226, 240, 210), (x * rectSize, y * rectSize, rectSize, rectSize))
                screen.blit(text, ((x * rectSize) + offsetX, (y * rectSize) + offsetY))
            elif arraySolved[y, x] != arrayUser[y, x] and arrayDef[y, x] == 0 and arrayUser[y, x] != 0:
                pygame.draw.rect(screen, (253, 170, 190), (x * rectSize, y * rectSize, rectSize, rectSize))
                screen.blit(text, ((x * rectSize) + offsetX, (y * rectSize) + offsetY))
    drawLine()

# Pygame window start parameters
pygame.init()
screen = pygame.display.set_mode((700, 500))
icon = pygame.image.load('duck.png')
pygame.display.set_caption('Sudoku')
pygame.display.set_icon(icon)
rectSize = 50
font = pygame.font.Font('freesansbold.ttf', 30)
font2 = pygame.font.SysFont('verdana', 20)
font3 = pygame.font.SysFont('verdana', 30)
running = True
selectSquare = False
numberPressed = False
isMenuSelected = False
isChecked = False
val = 0
x = -1
y = - 1
offsetX = 17
offsetY = 12
levEpositionX = 10
levMpositionX = 11
levHpositionX = 12
arrayDef = np.full((9,9),0)
arrayUser = np.full((9,9),0)
arraySolved = np.full((9,9),0)

# Window running
while running == True:
    screen.fill((230, 230, 230))
    drawMenu(x, isMenuSelected)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()
            print(mousePosition)
            x = getSelectedCell(mousePosition)[0]
            y = getSelectedCell(mousePosition)[1]
            selectSquare = True
            print(x)
            print(y)
        if event.type == pygame.KEYDOWN:
            print('Pressed button')
            if event.key == pygame.K_1:
                val = 1
            elif event.key == pygame.K_2:
                val = 2
            elif event.key == pygame.K_3:
                val = 3
            elif event.key == pygame.K_4:
                val = 4
            elif event.key == pygame.K_5:
                val = 5
            elif event.key == pygame.K_6:
                val = 6
            elif event.key == pygame.K_7:
                val = 7
            elif event.key == pygame.K_8:
                val = 8
            elif event.key == pygame.K_9:
                val = 9
            elif event.key == pygame.K_DELETE:
                val = 0
            elif event.key == pygame.K_LEFT:
                x = max(x - 1, 0)
            elif event.key == pygame.K_RIGHT:
                x = min(x + 1, 8)
            elif event.key == pygame.K_UP:
                y = max(y - 1, 0)
            elif event.key == pygame.K_DOWN:
                y = min(y + 1, 8)
            elif event.key == pygame.K_g:
                isChecked = False
                isMenuSelected = False
                numberPressed = False
                generateSudokuBoards(x)
                x = 0
                y = 0
            elif event.key == pygame.K_c:
                isChecked = True
            elif event.key == pygame.K_s:
                for i in range(9):
                    for j in range(9):
                        arrayUser[i, j] = arraySolved[i, j]
                isChecked = True
            else:
                val = -1
            if val >= 0 and val <= 9:
                numberPressed = True
            else:
                numberPressed = False

    drawBoard()
    drawLine()

    if selectSquare == True and x in (levEpositionX, levMpositionX, levHpositionX) and y == 1:
        isMenuSelected = True
    if selectSquare == True and x < 9 and y < 9:
        highlightCell(x, y)
        if numberPressed == True and arrayDef[y, x] == 0:
            arrayUser[y, x] = val
            print(arrayUser)
            print(arrayDef)
            print('User: ' + str(arrayUser[y, x]) + ' Def: ' + str(arrayDef[y, x]))
            numberPressed = False
        else:
            val = -1
            numberPressed = False

    if isChecked == True:
        selectSquare = False
        numberPressed = False
        checkSudoku()

    pygame.display.update()
