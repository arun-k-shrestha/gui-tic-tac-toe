import pygame, sys

pygame.init()

WIDTH = 660  
HEIGHT = 660
BG = (30, 160, 150 ) #background color

LINE_COLOR = (20,140,130)
LINE_WIDTH = 15

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TicTacToe Game')
screen.fill( BG )

def line():
    #horizontal lines
    pygame.draw.line(screen,LINE_COLOR, (0,220),(660,220), LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR, (0,440),(660,440), LINE_WIDTH)

    #vertical lines
    pygame.draw.line(screen,LINE_COLOR, (220,0),(220,660), LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR, (440,0),(440,660), LINE_WIDTH)

line()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
