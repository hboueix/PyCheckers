import pygame
from modules.checkerpiece import Checkerpiece

class Player:

    def __init__(self, color):
        self.color = color
        start_pos = []
        for j in range(5, 8):
            for i in range(8):
                if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                    start_pos.append((i * 85, 40 + j * 85))
        self.checkerpieces = [Checkerpiece(color, pos) for pos in start_pos]

    def get_all_piece_xy(self):
        all_pos = []
        for piece in self.checkerpieces:
            all_pos.append((piece.rect.x, piece.rect.y))
        return all_pos

