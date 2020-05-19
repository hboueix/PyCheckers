import pygame
from modules.checkerpiece import Checkerpiece

class Player:

    def __init__(self, tag_player, color):
        self.tag_player = tag_player
        self.color = color
        start_pos = self.get_start_pos(self.tag_player)
        checkerpieces = [Checkerpiece(color, pos) for pos in start_pos]
        self.checkerpieces = pygame.sprite.Group()
        for piece in checkerpieces:
            self.checkerpieces.add(piece)

    def get_start_pos(self, tag_player):
        if tag_player == 1:
            n, m = 5, 8
        elif tag_player == 2:
            n, m = 0, 3
        else:
            raise Exception("L'argument tag_player doit être un entier 1 ou 2")
        start_pos = []
        for j in range(n, m):
            for i in range(8):
                if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                    start_pos.append((i * 85, 40 + j * 85))
        return start_pos

    def get_all_piece_xy(self):
        all_pos = []
        for piece in self.checkerpieces:
            all_pos.append((piece.rect.x, piece.rect.y))
        return all_pos

