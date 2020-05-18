import pygame


class Checkerpiece(pygame.sprite.Sprite):

    def __init__(self, color, pos):
        self.color = color
        if self.color == 'black':
            self.image = pygame.image.load('app/assets/piece_black.png')
        elif self.color == 'white':
            self.image = pygame.image.load('app/assets/piece_white.png')
        else:
            raise Exception(f"La couleur {self.color} n'existe pas.")
        self.image = pygame.transform.scale(self.image, (85, 85))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
