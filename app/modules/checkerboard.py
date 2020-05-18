import pygame
from modules.checkerbox import Checkerbox


class Checkerboard(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 40, 680, 680)
        self.squaresize = self.rect.w / 8
        self.squarecolor = {'white': [200, 200, 200], 'black': [100, 100, 100]}
        self.boxes = [[i for i in range(8)] for _ in range(8)]
        for x in range(1, 9):
            for y in range(1, 9):
                coords = [
                    self.rect.x + self.squaresize * (x - 1),
                    self.rect.y + self.squaresize * (y - 1)
                ]
                if x % 2 != 0:
                    if y % 2 != 0:
                        box = Checkerbox(
                            self.squaresize, self.squarecolor['white'], coords
                        )
                    else:
                        box = Checkerbox(
                            self.squaresize, self.squarecolor['black'], coords
                        )
                else:
                    if y % 2 != 0:
                        box = Checkerbox(
                            self.squaresize, self.squarecolor['black'], coords
                        )
                    else:
                        box = Checkerbox(
                            self.squaresize, self.squarecolor['white'], coords
                        )
                self.boxes[x-1][y-1] = box

    def draw(self, screen):
        for line in self.boxes:
            for box in line:
                box.set_hovered()
                box.draw(screen)

    def get_hovered(self):
        for line in self.boxes:
            for box in line:
                if box.hovered:
                    return box.rect.x, box.rect.y

    def get_all_box_xy(self):
        all_pos = []
        for line in self.boxes:
            for box in line:
                all_pos.append((box.rect.x, box.rect.y))
        return all_pos

