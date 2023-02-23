import pygame
from .constants import GREEN, BROWN

class Board:
    def __init__(self):
        self.board = []
        self.selected_card = None
        self.total_cards = 81
        self.cards_left = 81

    def draw_board(self, win):
        win.fill(GREEN)
        #maak tafel waarop de kaarten komen te liggen

    def create_board(self, win, color, pos1, pos2):
        pygame.draw.rect(win, color, (pos1,pos2))
