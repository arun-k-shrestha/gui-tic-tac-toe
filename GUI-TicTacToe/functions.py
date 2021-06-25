import pygame, sys
import numpy

pygame.init()

WIDTH = 660  
HEIGHT = 660
BG = (30, 160, 150 ) #background color
CIRCLE_COLOR = (240, 243, 244) # Circle(O) color
CROSS_COLOR = (112, 123, 124) # Cross(X) color

ROWS = 3
COLS = 3

LINE_COLOR = (20,140,130)
LINE_WIDTH = 15

CIRCLE_RADIUS = 55
CIRCLE_WIDTH = 15

CROSS_WIDTH = 20
CROSS_GAP = 60 # It makes a cross stay in the middle on the box without touching the boundries.

WINING_LINE_WIDTH = 10

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TicTacToe Game')
screen.fill( BG )

board = numpy.zeros((3,3))

def line():
    #horizontal lines
    pygame.draw.line(screen,LINE_COLOR, (0,220),(660,220), LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR, (0,440),(660,440), LINE_WIDTH)

    #vertical lines
    pygame.draw.line(screen,LINE_COLOR, (220,0),(220,660), LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR, (440,0),(440,660), LINE_WIDTH)

def drawing():
    for c in range(COLS):
        for r in range(ROWS):
            if board[c][r] == 1:
                pygame.draw.circle( screen , CIRCLE_COLOR , ( int(c*220 + 110), int(r*220 + 110) ), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[c][r] == 2:
                pygame.draw.line( screen, CROSS_COLOR, (c * 220 + CROSS_GAP , r * 220 + 220 - CROSS_GAP), (c * 220 + 220 - CROSS_GAP, r  * 220 + CROSS_GAP), CROSS_WIDTH )
                pygame.draw.line( screen, CROSS_COLOR, (c * 220 + CROSS_GAP, r * 220 + CROSS_GAP), (c * 220 + 220 - CROSS_GAP, r  * 220 + 220 - CROSS_GAP), CROSS_WIDTH )

def marking(row, col, mark):
    board[row][col] = mark

def availability (row, col):
    if board[row][col] == 0:
        return True
    else:
        return False


def is_full():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col]==0:
                return False
    return True

def winning_line():

    for col in range(3): # checking and marking horizontal lines

        if board[0][col]== board[1][col] == board[2][col] == 1:
            pygame.draw.line(screen,CIRCLE_COLOR, (20,110 * (col*2 + 1)),(640,110 * (col*2 + 1)), WINING_LINE_WIDTH)
            return True

        elif board[0][col] == board[1][col] == board[2][col] == 2:
            pygame.draw.line(screen,CROSS_COLOR, (20,110 * (col*2 + 1)),(640,110 * (col*2 + 1)), WINING_LINE_WIDTH)
            return True
    
    for row in range(3): # checking and marking vertical lines

        if board[row][0]== board[row][1] == board[row][2] == 1:
            pygame.draw.line(screen,CIRCLE_COLOR, (110 * (row*2 + 1), 20),(110 * (row*2 + 1), 640), WINING_LINE_WIDTH)
            return True

        elif board[row][0]== board[row][1] == board[row][2] ==  2:
            pygame.draw.line(screen,CROSS_COLOR, (110 * (row*2 + 1), 20),(110 * (row*2 + 1), 640), WINING_LINE_WIDTH)
            return True

def diagonal_lines():

    if board[0][0]== board[1][1] == board[2][2]== 1:
        pygame.draw.line(screen,CIRCLE_COLOR, (20,20),(640, 640), WINING_LINE_WIDTH)
        return True

    elif board[0][2]== board[1][1] == board[2][0]== 1:
        pygame.draw.line(screen,CIRCLE_COLOR, (20,640),(640, 20), WINING_LINE_WIDTH)
        return True

    elif board[0][0]== board[1][1] == board[2][2]== 2:
        pygame.draw.line(screen,CROSS_COLOR, (20,20),(640, 640), WINING_LINE_WIDTH)
        return True

    elif board[0][2]== board[1][1] == board[2][0]== 2:
        pygame.draw.line(screen,CROSS_COLOR, (20,640),(640, 20), WINING_LINE_WIDTH)
        return True