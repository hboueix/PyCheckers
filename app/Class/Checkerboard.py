#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from .Square import *
from .Box import *


class Checkerboard(Square):

    def __init__(self, size):
        Square.__init__(self, size)
        self.squaresize = self.size / 8
        self.squarecolor = {'white': [200, 200, 200], 'black': [100, 100, 100]}
        self.boxes = [[i for i in range(8)] for _ in range(8)]

    def load(self, window):
        for x in range(1, 9):

            for y in range(1, 9):

                box = self.boxes[x-1][y-1]
                coords = [
                    self.squaresize * (x - 1),
                    self.squaresize * (y - 1),
                    self.squaresize,
                    self.squaresize
                ]

                if x % 2 != 0:
                    if y % 2 != 0:
                        box = Box(self.squaresize,
                                  self.squarecolor['white'],
                                  coords
                                  )
                        pygame.draw.rect(
                            window, box.color, box.coords
                        )
                    else:
                        box = Box(self.squaresize,
                                  self.squarecolor['black'],
                                  coords
                                  )
                        pygame.draw.rect(
                            window, box.color, box.coords
                        )
                else:
                    if y % 2 != 0:
                        box = Box(self.squaresize,
                                  self.squarecolor['black'],
                                  coords
                                  )
                        pygame.draw.rect(
                            window, box.color, box.coords
                        )
                    else:
                        box = Box(self.squaresize,
                                  self.squarecolor['white'],
                                  coords
                                  )
                        pygame.draw.rect(
                            window, box.color, box.coords
                        )
                self.boxes[x-1][y-1] = box


'''
pygame.init()

squaresize = 60

squarecolor_wht = [200, 200, 200]
squarecolor_blk = [100, 100, 100]

botbar = 150
botbarcolor = squarecolor_blk

notpressedcolor = squarecolor_wht
pressedcolor = squarecolor_blk

game_w = (squaresize * 8)
game_h = (squaresize * 8)

win_w = game_w
win_h = game_h

win = pygame.display.set_mode([win_w, win_h])


def main():
    for x in range(1, 9):
        for y in range(1, 9):
            if x % 2 != 0:
                if y % 2 != 0:
                    pygame.draw.rect(win, squarecolor_wht, [squaresize * (x - 1), squaresize * (y - 1),
                                                            squaresize, squaresize])
                else:
                    pygame.draw.rect(win, squarecolor_blk, [squaresize * (x - 1), squaresize * (y - 1),
                                                            squaresize, squaresize])
            else:
                if y % 2 != 0:
                    pygame.draw.rect(win, squarecolor_blk, [squaresize * (x - 1), squaresize * (y - 1),
                                                            squaresize, squaresize])
                else:
                    pygame.draw.rect(win, squarecolor_wht, [squaresize * (x - 1), squaresize * (y - 1),
                                                            squaresize, squaresize])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
'''
