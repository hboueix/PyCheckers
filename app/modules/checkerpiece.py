import pygame


class Checkerpiece(pygame.sprite.Sprite):

    def __init__(self, color, pos):
        super().__init__()
        self.color = color
        try:
            self.image = pygame.image.load(f'app/assets/piece_{self.color}.png')
        except Exception:
            raise Exception(f"La couleur {self.color} n'existe pas.")
        self.image = pygame.transform.scale(self.image, (85, 85))
        self.original_img = self.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.hovered = self.is_selected = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def set_hovered(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False

    def set_selected(self):
        if self.hovered:
            self.image = pygame.image.load(f"app/assets/piece_{self.color}_selected.png")
            self.image = pygame.transform.scale(self.image, (85, 85))
            self.is_selected = True
        else:
            self.image = self.original_img
            self.is_selected = False
