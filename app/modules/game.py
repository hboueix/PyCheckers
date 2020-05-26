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
        self.with_bot = False

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
            piece.set_hovered()
            piece.draw(screen)
            if piece.is_selected:
                for move in piece.valid_moves:
                    pygame.draw.rect(screen, [0, 255, 0], (move[0] + 10, move[1] + 10, 65, 65), 5)

        header = 'user> '
        if hasattr(self, "user"):
            self.user.run_connection(input_text)
            if self.user.recv_text != '':
                input_text = self.user.recv_text + input_text
            elif input_text != '':
                input_text = f"{self.user.username}> {input_text}"
            self.user.recv_text = ''

        if input_text != '':
            if not hasattr(self, "user"):
                input_text = header + input_text
            self.outputbox.blit_text(screen, input_text)
        else:
            self.outputbox.blit_text(screen, self.outputbox.text)

    def set_players(self, color_current_user):
        self.player1 = Player(color_current_user, True)
        color_player2 = 'white' if color_current_user == 'black' else 'black'
        if not self.with_bot:
            self.player2 = Player(color_player2)
        else:
            self.player2 = Bot(color_player2)
