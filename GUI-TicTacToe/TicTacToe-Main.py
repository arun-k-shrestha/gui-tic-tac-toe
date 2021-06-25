import pygame, sys
import numpy
import functions

functions.line()
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
        
            if functions.availability( click_onX, click_onY):
                if player == 1:
                    functions.marking(click_onX,click_onY,1)
                    player = 2
                elif player == 2:
                    functions.marking(click_onX,click_onY,2)
                    player = 1
                
                functions.drawing()
                functions.diagonal_lines()
                functions.winning_line()
    
    pygame.display.update()

