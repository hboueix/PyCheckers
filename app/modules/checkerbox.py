import pygame


class Checkerbox(pygame.sprite.Sprite):

    def __init__(self, size, color, coords):
        super().__init__()
        self.rect = pygame.Rect(coords[0], coords[1], size, size)
        self.color = color
        self.hovered = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def set_hovered(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False

