'''main.py is de algemene regelcode die de interactie tussne gameManager.py en setGame.py regelt.
eventueel kunnen we dan later nog andere games toevogen, zoals uno door slechts een nieuwe unoGame.py te maken.
'''

#Libraries
import pygame
import numpy as np #Deze is waarschijnlijk wel nodig
import random
from set.constants import *
from set.board import Board
from set.button import *

FPS = 60
#pygame init
pygame.init()
board = Board()
start_game = False
#Pepijn was here

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Set!")

SET_LOGO = pygame.image.load('assets/set_logo.png')
LOGO = pygame.image.load('assets/4_rij_logo.png')
LOGO2 = pygame.transform.scale(LOGO, (158, 158))

set_rect = SET_LOGO.get_rect()
logo2_rect = LOGO2.get_rect()

set_rect.center = 250, 400
logo2_rect.center = 642, 400



def intro():
    WIN.fill(WHITE)
    WIN.blit(SET_LOGO, set_rect)
    WIN.blit(LOGO2, logo2_rect)
    
    
def main():
    run = True
    clock = pygame.time.Clock()
    starting = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                print(pos)
                if set_rect.collidepoint(pos):
                    print("Set! clicked!")
                    starting = False
                    set_rect.center = -100,-100
                    logo2_rect.center = -100,-100
                elif logo2_rect.collidepoint(pos):
                    print("4 in a row clicked!")
                    starting = False
                    set_rect.center = -100,-100
                    logo2_rect.center = -100,-100
        if starting == True:
            intro()
        else:
            board.draw_board(WIN)
        
            
        pygame.display.update()

    pygame.quit()

main()