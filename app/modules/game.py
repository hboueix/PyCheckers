import pygame
from modules.checkerboard import Checkerboard
from modules.inputbox import InputBox
from modules.outputbox import OutputBox
from modules.player import Player
from modules.bot import Bot


class Game:

    def __init__(self):
        # Game has begun ?
        self.is_playing = False
        # Components
        self.checkerboard = Checkerboard()
        self.outputbox = OutputBox(self.checkerboard.rect.w, 0, 400, 680)
        self.inputbox = InputBox(self.checkerboard.rect.w, self.outputbox.rect.h, 400, 40)
        self.player1 = Player('white', True)
        self.player2 = Bot('black')

    def update(self, screen, input_text):
        # Apply background color
        screen.fill((30, 30, 30))

        # Draw checkerboard
        self.checkerboard.draw(screen)

        # Draw chat
        self.inputbox.draw(screen)
        self.outputbox.draw(screen)

        # Draw player1 pieces
        for piece in self.player1.checkerpieces:
            piece.set_hovered()
            piece.draw(screen)
            if piece.is_selected:
                for move in piece.valid_moves:
                    pygame.draw.rect(screen, [0, 255, 0], (move[0] + 10, move[1] + 10, 65, 65), 5)
        # Draw player 2 pieces
        for piece in self.player2.checkerpieces:
            piece.draw(screen)

        if input_text != '':
            self.outputbox.blit_text(screen, 'user> ' + input_text)
        else:
            self.outputbox.blit_text(screen, self.outputbox.text)


