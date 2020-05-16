import pygame
from modules.button import Button


class Menu:

    def __init__(self):
        self.title = 'Menu'
        self.options = [Button("NEW GAME", (465, 360))]
        # Create background
        self.background = pygame.image.load("app/assets/background.png")
        self.background = pygame.transform.scale(self.background, (1080, 1080))
        # Logo
        self.logo = pygame.image.load("app/assets/logo.png")