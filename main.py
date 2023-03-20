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


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                print(pos)
                if board.set_box.collidepoint(pos):
                    print("Set! clicked!")
                elif board.four_box.collidepoint(pos):
                    print("4 in a row clicked!")
        board.draw_board(WIN)
        board.start_screen(WIN)
        
            
        pygame.display.update()

    pygame.quit()

main()