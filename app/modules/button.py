import pygame


class Button(pygame.sprite.Sprite):
    hovered = False

    def __init__(self, text, pos):
        super().__init__()
        self.text = text
        self.pos = pos
        self.menu_font = pygame.font.Font(None, 40)
        self.set_rect()
        #self.draw()

    def draw(self, screen, bg=(255, 255, 255)):
        self.set_rend()
        pygame.draw.rect(screen, bg,
                         (self.rect.x - 20, self.rect.y - 20, self.rect.w + 40, self.rect.h + 35)
                        )
        screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = self.menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return (8, 59, 102)
        else:
            return (0, 0, 0)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.centerx = self.pos[0]
        self.rect.y = self.pos[1]

    def set_hovered(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False
