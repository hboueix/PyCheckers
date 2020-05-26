import pygame
# import os
from modules.helpers import *
from modules.menu import Menu
from modules.game import Game
from modules.user import User


pygame.init()

# Get real path and real directory
# realpath = os.path.realpath(__file__)
# realdir = os.path.dirname(realpath)

# Set title and init game window with icon
pygame.display.set_caption("PyCheckers")

screen = pygame.display.set_mode((1080, 720))

icon = pygame.image.load("app/assets/icon.png").convert()
pygame.display.set_icon(icon)

# Create main menu
menu = Menu()
menu.main()

# Create a game
game = Game()

# Not playing so main page

# Game loop
running = True
input_text = ''
while running:

    if game.is_playing:
        # Update game screen
        game.update(screen, input_text)
        input_text = ''
    else:
        menu.update(screen)

    # Update screen
    pygame.display.flip()

    for event in pygame.event.get():
        # Catch input
        input_text = game.inputbox.handle_event(event)
        for inputbox in menu.inputboxes:
            inputbox.handle_event(event)
        # Start new game event
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If button clic on main menu
            if not game.is_playing:
                for option in menu.options:
                    if option.hovered:
                        if option.text == "BACK":
                            menu.main()
                        elif option.text == "White" or option.text == "Black":
                            menu.selected = option
                        elif option.text == "PLAY":
                            game.set_players(menu.selected.text.lower())
                            game.is_playing = True
                        elif option.text == "OFFLINE GAME":
                            menu.offline_mode()
                        elif option.text == "Player vs Player":
                            game.with_bot = False
                            menu.offline_color()
                        elif option.text == "Player vs AI":
                            game.with_bot = True
                            menu.offline_color()
                        elif option.text == "ONLINE GAME":
                            menu.login_register()
                        elif option.text == "Login":
                            if check_login(menu.input_username.text, menu.input_password.text):
                                game.user = User(menu.input_username.text)
                            game.set_players('white')
                            game.is_playing = True
                        elif option.text == "Register":
                            if check_register(menu.input_username.text):
                                register(menu.input_username.text, menu.input_password.text)
                                game.user = User(menu.input_username.text)
                            game.set_players('white')
                            game.is_playing = True
            # User trying to move piece
            elif game.player1.his_turn:
                for piece in game.player1.checkerpieces:
                    if piece.is_selected:
                        target = game.checkerboard.get_hovered()
                        valid_moves = get_valid_moves(piece, game.player1, game.player2, game.checkerboard)
                        if target in valid_moves:
                            piece.move(target)
                            if game.with_bot:
                                game.player1.his_turn = False
                                game.player2.his_turn = True
                                for piece_bot in game.player2.checkerpieces:
                                    piece_bot.valid_moves = get_valid_moves(piece_bot,
                                                                            game.player1,
                                                                            game.player2,
                                                                            game.checkerboard)
                                game.player2.random_move()
                                game.player1.his_turn = True
                                game.player2.his_turn = False
                            else:
                                game.player1.his_turn = False
                                game.player2.his_turn = True
                    piece.set_selected()
                    if piece.is_selected:
                        valid_moves = get_valid_moves(piece, game.player1, game.player2, game.checkerboard)
                        piece.valid_moves = valid_moves
            elif game.player2.his_turn:
                for piece in game.player2.checkerpieces:
                    if piece.is_selected:
                        target = game.checkerboard.get_hovered()
                        valid_moves = get_valid_moves(piece, game.player1, game.player2, game.checkerboard)
                        if target in valid_moves:
                            piece.move(target)
                            game.player1.his_turn = True
                            game.player2.his_turn = False
                    piece.set_selected()
                    if piece.is_selected:
                        valid_moves = get_valid_moves(piece, game.player1, game.player2, game.checkerboard)
                        piece.valid_moves = get_valid_moves(piece, game.player1, game.player2, game.checkerboard)


        '''
        # If return is pressed on main menu
        if event.type == pygame.KEYDOWN and not game.is_playing:
            if event.key == pygame.K_RETURN:
                game.is_playing = True
        '''

        # Close window event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
