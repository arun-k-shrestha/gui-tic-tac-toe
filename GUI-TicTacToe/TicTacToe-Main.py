import pygame, sys
import functions


functions.line()
start = 1
game_over = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and game_over == True:

            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            click_onX = int(mouseX // 220)
            click_onY = int(mouseY // 220)
        
            if functions.availability( click_onX, click_onY):
                if start == 1:
                    functions.marking(click_onX,click_onY,1)
                    start = 2
                elif start == 2:
                    functions.marking(click_onX,click_onY,2)
                    start = 1
                
                functions.drawing()
                functions.diagonal_lines()
                functions.winning_line()

                if functions.winning_line()== True or functions.diagonal_lines() == True or functions.is_full():
                    game_over = False
                    pygame.display.update()
                    pygame.time.delay(500)
                    functions.restart_screen()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                functions.restart()
                game_over = True
            
    pygame.display.update()


