import pygame


class Checkerbox(pygame.sprite.Sprite):

    def __init__(self, size, color, coords):
        super().__init__()
        self.rect = pygame.Rect(coords[0], coords[1], size, size)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
