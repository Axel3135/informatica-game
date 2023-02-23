'''main.py is de algemene regelcode die de interactie tussne gameManager.py en setGame.py regelt.
eventueel kunnen we dan later nog andere games toevogen, zoals uno door slechts een nieuwe unoGame.py te maken.
'''

#Libraries
import pygame
import numpy as np #Deze is waarschijnlijk wel nodig
import random

#pygame innit
pygame.init()

#main loop

running = True

while running:
    screen = pygame.display.set_mode((600,500))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
    







