'''main.py is de algemene regelcode die de interactie tussne gameManager.py en setGame.py regelt.
eventueel kunnen we dan later nog andere games toevogen, zoals uno door slechts een nieuwe unoGame.py te maken.
'''

#Libraries
import pygame
import numpy as np #Deze is waarschijnlijk wel nodig
import random
from time import sleep
from set.constants import *
from set.board import Board
from set.button import *
from setGame import *

FPS = 60
#pygame init
pygame.init()
board = Board()
start_game = False

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Set!")

SET_LOGO = pygame.image.load('assets/set_logo.png')
LOGO = pygame.image.load('assets/4_rij_logo.png')
LOGO2 = pygame.transform.scale(LOGO, (158, 158))
kaartdemo = pygame.image.load('assets/individuele_kaarten/GDE1.jpg')
kaart = pygame.transform.scale(kaartdemo, (70,120)) #standaardmaten kaarten

set_rect = SET_LOGO.get_rect()
logo2_rect = LOGO2.get_rect()
kaart_rect = kaart.get_rect()

set_rect.center = 250, 400
logo2_rect.center = 642, 400
kaart_rect.center = 200, 200

selected = None

def load_cards():
    pass

def intro():
    WIN.fill(WHITE)
    WIN.blit(SET_LOGO, set_rect)
    WIN.blit(LOGO2, logo2_rect)

def init_set():
    '''functie die het setspel beheert.
    deze wordt aangeroepen door de mainloop.'''
    widthx, heighty = 70, 120
    startx, starty = 200, 200
    margin = 10
    #firstCard(200, 200)
    board.draw_board(WIN)
    SetBoard = SetGame()
    cardIndex = 0
    SetBoard.active_cards[0].image
    for i in range(4):  # eens per ronde
        for j in range(3):
            # index --> i*3+j
            set_demo_kaart = SetBoard.active_cards[(i*3+j)].image
            set_kaart = pygame.transform.scale(set_demo_kaart, (70,120))
            set_kaart_rect = set_kaart.get_rect()
            set_kaart_rect.center = [startx+i*(widthx+margin), starty+j*(heighty+margin)]  # set center img
            WIN.blit(set_kaart, set_kaart_rect)
    sleep(1)
    # zet active cards in goede rooster
    
    #clickedCards = []
    #while len(clickedCards) <= 2:
        

    # import setgame
    # maak een setboard object CHECK
    # zet de list actieve kaarten om naar plaatjes op het scherm CHECK
    # zorg dat drie kaarten geselecteeerd kunnen worden en geasigned aan een player (geef de geselecteerde kaarten aan) BEZIG
    # check of drie kaarten een set is
    # als set punten speler += 1
    # overige game logic (kaarten aanvullen, end detect, geen set detect)
    

    
def main():
    run = True
    clock = pygame.time.Clock()
    starting = True
    load_cards()
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
                    selected = 'set_init'
                elif logo2_rect.collidepoint(pos):
                    print("4 in a row clicked!")
                    starting = False
                    set_rect.center = -100,-100
                    logo2_rect.center = -100,-100
                    selected = '4row'
        if starting == True:
            intro()
        else:
            if selected == 'set_init':
                init_set()
                selected = set
            elif selected == 'set':
                pass
            elif selected == '4row':
                pass
        
            
        pygame.display.update()

    pygame.quit()

main()