import pygame
from modules.button import Button
from modules.inputbox import InputBox


class Menu:

    def __init__(self):
        # Create background
        self.background = pygame.image.load("app/assets/background.png")
        self.background = pygame.transform.scale(self.background, (1080, 1080))
        # Logo
        self.logo = pygame.image.load("app/assets/logo.png")
        self.selected = None
        self.inputboxes = pygame.sprite.Group()

    def update(self, screen):
        # Apply background & logo
        screen.blit(self.background, (0, -110))
        screen.blit(self.logo, (540 - (self.logo.get_rect().w / 2), 60))
        # Draw buttons
        for option in self.options:
            option.set_hovered()
            if self.selected == option:
                option.draw(screen, (0, 255, 0))
            else:
                option.draw(screen)
        for inputbox in self.inputboxes:
            inputbox.draw(screen)

    def main(self):
        self.options = [Button("OFFLINE GAME", (540, 360)), Button("ONLINE GAME", (540, 450))]
        self.selected = None
        self.inputboxes = pygame.sprite.Group()

    def login_register(self):
        self.inputboxes = pygame.sprite.Group()
        self.options = [Button("Login", (270, 500)), Button("Register", (810, 500)), Button("BACK", (100, 650))]
        self.input_username = InputBox(440, 300, 200, 40, 'Username')
        self.input_password = InputBox(440, 380, 200, 40, 'Password')
        self.inputboxes.add(self.input_username, self.input_password)

    def online(self):
        self.options = [Button("Find a player", (540, 400)), Button("BACK", (100, 650))]
        self.selected = None

    def offline_mode(self):
        self.options = [Button("Player vs Player", (420, 340)),
                        Button("Player vs AI", (660, 340)),
                        Button("BACK", (100, 650))]
        self.selected = None

    def offline_color(self):
        self.options = [Button("White", (460, 340)),
                        Button("Black", (620, 340)),
                        Button("PLAY", (540, 450)),
                        Button("BACK", (100, 650))]
        self.selected = self.options[0]
