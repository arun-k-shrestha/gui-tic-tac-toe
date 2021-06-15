import pygame, sys
import numpy

pygame.init()

WIDTH = 660  
HEIGHT = 660
BG = (30, 160, 150 ) #background color

ROWS = 3
COLS = 3

LINE_COLOR = (20,140,130)
LINE_WIDTH = 15

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TicTacToe Game')
screen.fill( BG )

board = numpy.zeros((3,3))
print(board)

def line():
    #horizontal lines
    pygame.draw.line(screen,LINE_COLOR, (0,220),(660,220), LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR, (0,440),(660,440), LINE_WIDTH)

    #vertical lines
    pygame.draw.line(screen,LINE_COLOR, (220,0),(220,660), LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR, (440,0),(440,660), LINE_WIDTH)

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

print(is_full())
line()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            click_onX = int(mouseX // 220)
            click_onY = int(mouseY // 220)

    pygame.display.update()
