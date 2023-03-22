import pygame
from .constants import *

class Board:
    def __init__(self):
        self.board = []
        self.selected_card = None
        self.total_cards = 81
        self.cards_left = 81
        

    def draw_board(self, win):
        win.fill(GREEN)
        #maak tafel waarop de kaarten komen te liggen
        pygame.draw.rect(win, BROWN, (100,100,600,600))
        
    def create_board(self, win, color, pos1, pos2):
        pygame.draw.rect(win, color, (pos1,pos2))

'''
 def start_screen(self, win):
        win.fill(WHITE)


        #set.constants.set_rect.move(50,400)
        #set.constants.logo2_rect.move(WIDTH - 258, 400)
        '''

