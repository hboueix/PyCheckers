import pygame
from modules.player import Player
from modules.checkerpiece import Checkerpiece


class Bot(Player):

    def __init__(self, color):
        super().__init__(2, color)
        start_pos = self.get_start_pos(self.tag_player)
        checkerpieces = [Checkerpiece(color, pos) for pos in start_pos]
        self.checkerpieces = pygame.sprite.Group()
        for piece in checkerpieces:
            self.checkerpieces.add(piece)