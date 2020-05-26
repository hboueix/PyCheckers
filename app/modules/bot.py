import pygame
import random
from modules.helpers import get_valid_moves
from modules.player import Player
from modules.checkerpiece import Checkerpiece


class Bot(Player):

    def __init__(self, color):
        super().__init__(color)
        start_pos = self.get_start_pos()
        checkerpieces = [Checkerpiece(color, pos) for pos in start_pos]
        self.checkerpieces = pygame.sprite.Group()
        for piece in checkerpieces:
            self.checkerpieces.add(piece)

    def random_move(self):
        checkerpieces = list(self.checkerpieces)
        random.shuffle(checkerpieces)
        for piece in checkerpieces:
            if piece.valid_moves:
                print(piece.valid_moves)
                for move in random.sample(piece.valid_moves, len(piece.valid_moves)):
                    piece.move(move)
                    return
