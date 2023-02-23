import pygame
from .constants import GREEN

class Board:
    def __init__(self):
        self.board = []
        self.selected_card = None
        self.total_cards = 81
        self.cards_left = 81

    def draw_board(self, win):
        win.fill(GREEN)
