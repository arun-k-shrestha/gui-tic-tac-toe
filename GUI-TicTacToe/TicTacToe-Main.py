import pygame, sys
import numpy

pygame.init()

WIDTH = 660  
HEIGHT = 660
BG = (30, 160, 150 ) #background color
C1 = (255, 0, 0)
C2 = (123, 30, 120)

ROWS = 3
COLS = 3

LINE_COLOR = (20,140,130)
LINE_WIDTH = 15

CIRCLE_RADIUS = 55
CIRCLE_WIDTH = 15

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
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 1:
                pygame.draw.circle( screen , C1 , ( int(r*220 + 110), int(c*220 + 110) ), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[r][c] == 2:
                pygame.draw.circle( screen , C2 , ( int(r*220 + 110), int(c*220 + 110) ), CIRCLE_RADIUS, CIRCLE_WIDTH)

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

line()

player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            click_onX = int(mouseX // 220)
            click_onY = int(mouseY // 220)
        
            if availability( click_onX, click_onY):
                if player == 1:
                    marking(click_onX,click_onY,1)
                    player = 2
                elif player == 2:
                    marking(click_onX,click_onY,2)
                    player = 1

                drawing()

    pygame.display.update()
