#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from .Rectangle import *
from .CheckerBox import *


class Checkerboard(Rectangle):

    def __init__(self, x, y, size):
        Rectangle.__init__(self, size, size)
        self.x = x
        self.y = y
        self.squaresize = self.size / 8
        self.squarecolor = {'white': [200, 200, 200], 'black': [100, 100, 100]}
        self.boxes = [[i for i in range(8)] for _ in range(8)]

    def load(self, window):
        for x in range(1, 9):

            for y in range(1, 9):

                box = self.boxes[x-1][y-1]
                coords = [
                    self.x + self.squaresize * (x - 1),
                    self.y + self.squaresize * (y - 1),
                    self.x + self.squaresize,
                    self.y + self.squaresize
                ]

                if x % 2 != 0:
                    if y % 2 != 0:
                        box = CheckerBox(self.squaresize,
                                         self.squarecolor['white'],
                                         coords
                                         )
                        pygame.draw.rect(
                            window, box.color, box.coords
                        )
                    else:
                        box = CheckerBox(self.squaresize,
                                         self.squarecolor['black'],
                                         coords
                                         )
                        pygame.draw.rect(
                            window, box.color, box.coords
                        )
                else:
                    if y % 2 != 0:
                        box = CheckerBox(self.squaresize,
                                         self.squarecolor['black'],
                                         coords
                                         )
                        pygame.draw.rect(
                            window, box.color, box.coords
                        )
                    else:
                        box = CheckerBox(self.squaresize,
                                         self.squarecolor['white'],
                                         coords
                                         )
                        pygame.draw.rect(
                            window, box.color, box.coords
                        )
                self.boxes[x-1][y-1] = box
