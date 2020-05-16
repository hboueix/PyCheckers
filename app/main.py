import pygame
#import os
from modules.menu import Menu
from modules.game import Game

pygame.init()

# Get real path and real directory
#realpath = os.path.realpath(__file__)
#realdir = os.path.dirname(realpath)

# Set title and init game window with icon
pygame.display.set_caption("PyCheckers")

screen = pygame.display.set_mode((1080, 720))

icon = pygame.image.load("app/assets/icon.png").convert()
pygame.display.set_icon(icon)

# Create main menu
main_menu = Menu()

# Create a game
game = Game()

# Not playing so main page
is_playing = False

# Game loop
running = True
input_text = ''
while running:

    if is_playing:
        # Apply background color
        screen.fill((30, 30, 30))

        # Draw checkerboard
        game.checkerboard.draw(screen)

        # Draw chat
        game.inputbox.draw(screen)
        game.outputbox.draw(screen)
        if input_text != '':
            game.outputbox.blit_text(screen, 'user> ' + input_text)
            input_text = ''
        else:
            game.outputbox.blit_text(screen, game.outputbox.text)
    else:
        # Apply background & logo
        screen.blit(main_menu.background, (0, -110))
        screen.blit(main_menu.logo, (540 - (main_menu.logo.get_rect().w / 2), 60))
        # Draw buttons
        for option in main_menu.options:
            option.set_hovered()
            option.draw(screen)

    # Update screen
    pygame.display.flip()

    for event in pygame.event.get():
        # Catch input
        input_text = game.inputbox.handle_event(event)
        # Start new game event
        if event.type == pygame.MOUSEBUTTONDOWN:
            for option in main_menu.options:
                if option.hovered and option.text == "NEW GAME":
                    is_playing = True
        # Close window event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
