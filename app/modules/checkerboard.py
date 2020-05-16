import pygame
from modules.checkerbox import Checkerbox


class Checkerboard(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 40, 680, 680)
        self.squaresize = self.rect.w / 8
        self.squarecolor = {'white': [200, 200, 200], 'black': [100, 100, 100]}
        self.boxes = [[i for i in range(8)] for _ in range(8)]

    def draw(self, screen):
        for x in range(1, 9):
            for y in range(1, 9):
                box = self.boxes[x-1][y-1]
                coords = [
                    self.rect.x + self.squaresize * (x - 1),
                    self.rect.y + self.squaresize * (y - 1)
                ]
                if x % 2 != 0:
                    if y % 2 != 0:
                        box = Checkerbox(
                            self.squaresize, self.squarecolor['white'], coords
                        )
                        box.draw(screen)
                    else:
                        box = Checkerbox(
                            self.squaresize, self.squarecolor['black'], coords
                        )
                        box.draw(screen)
                else:
                    if y % 2 != 0:
                        box = Checkerbox(
                            self.squaresize, self.squarecolor['black'], coords
                        )
                        box.draw(screen)
                    else:
                        box = Checkerbox(
                            self.squaresize, self.squarecolor['white'], coords
                        )
                        box.draw(screen)
                self.boxes[x-1][y-1] = box
