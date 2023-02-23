'''main.py is de algemene regelcode die de interactie tussne gameManager.py en setGame.py regelt.
eventueel kunnen we dan later nog andere games toevogen, zoals uno door slechts een nieuwe unoGame.py te maken.
'''

#Libraries
import pygame
import numpy as np #Deze is waarschijnlijk wel nodig
import random
from set.constants import WIDTH, HEIGHT
from set.board import Board

FPS = 60
#pygame init
pygame.init()

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Set!")

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_board(WIN)
        pygame.display.update()

    pygame.quit()

main()