import pygame
from modules.checkerpiece import Checkerpiece

class Player:

    def __init__(self, color, current_user=False):
        self.current_user = current_user
        self.color = color
        self.tag_player = 1 if color == 'white' else 2
        start_pos = self.get_start_pos()
        checkerpieces = [Checkerpiece(color, pos) for pos in start_pos]
        self.checkerpieces = pygame.sprite.Group()
        for piece in checkerpieces:
            self.checkerpieces.add(piece)
        self.his_turn = True if self.tag_player == 1 else False

    def lose_piece(self, pos):
        for piece in self.checkerpieces:
            if (piece.rect.x, piece.rect.y) == pos:
                self.checkerpieces.remove(piece)
                print(f"remove piece at pos {pos}")

    def get_start_pos(self):
        if self.current_user:
            n, m = 5, 8
        else:
            n, m = 0, 3
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

