#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, sys

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
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()