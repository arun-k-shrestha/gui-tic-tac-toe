import pygame, sys

pygame.init()

WIDTH = 638  
HEIGHT = 638
screen = pygame.display.set_mode((WIDTH,HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
