import pygame
import sys
import os
from Class.Window import *
from Class.Checkerboard import *
from Class.InputBox import *
from Class.OutputBox import *

# Get real path and real directory
realpath = os.path.realpath(__file__)
realdir = os.path.dirname(realpath)

pygame.init()

clock = pygame.time.Clock()

# Init objects
win = Window(880, 60 * 8).open()

checkerboard = Checkerboard(0, 0, 60 * 8)

inputbox = InputBox(60 * 8, 440, 400, 40)

outputbox = OutputBox(60 * 8, 0, 400, 440)

# Set title and icon
pygame.display.set_caption("PyCheckers")
image = pygame.image.load(realdir + "/img/icon.png").convert()
pygame.display.set_icon(image)

# Game loop
CONTINUE = True
try:
    while CONTINUE:
        # Handle event
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                CONTINUE = False

            input_text = inputbox.handle_event(event)

        # Update objects
        win.fill((30, 30, 30))

        checkerboard.load(win)
        inputbox.draw(win)

        outputbox.draw(win)
        if input_text != '':
            outputbox.blit_text(win, 'user> ' + input_text)
        else:
            outputbox.blit_text(win, outputbox.text)
        input_text = ''

        # Update display
        pygame.display.flip()
        clock.tick(30)


except KeyboardInterrupt:
    print('\nExit application...')

pygame.quit()
