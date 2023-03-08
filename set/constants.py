#Aparte file in de package met alle constanten zodat we meer overzicht hebben. + packages zijn cool.
import pygame


WIDTH, HEIGHT = 800, 750
ROWS, COLS = 5, 5
AREA_SIZE = 100

RED = (255, 0 ,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 64, 0)
LIGHT_GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BROWN = (70,22,22)

SET_LOGO = pygame.image.load('assets/set_logo.png')
LOGO = pygame.image.load('assets/4_rij_logo.png')
LOGO2 = pygame.transform.scale(LOGO, (158, 158))

set_rect = SET_LOGO.get_rect()
logo2_rect = LOGO2.get_rect()
