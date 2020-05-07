import pygame
import sys
import os
from Class.Window import *
from Class.Checkerboard import *

realpath = os.path.realpath(__file__)
realdir = os.path.dirname(realpath)

pygame.init()

win = Window(60 * 8, 60 * 8).open()

checkerboard = Checkerboard(60 * 8)
checkerboard.load(win)

pygame.display.set_caption("PyCheckers")

image = pygame.image.load(realdir + "/img/icon.png").convert()
pygame.display.set_icon(image)

CONTINUE = True
try:
    while CONTINUE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CONTINUE = False
        pygame.display.flip()

except KeyboardInterrupt:
    print('\nExit application...')
