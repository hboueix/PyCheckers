import pygame


class OutputBox:

    def __init__(self, x, y, w, h, text='Bienvenue !'):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('lightskyblue3')
        self.text = text
        self.font = pygame.font.SysFont('Arial', 20)
        self.txt_surface = self.font.render(text, True, self.color)

    def blit_text(self, window, text):
        if self.text != text:
            text = self.text + '\n' + text
            self.text = text
        # 2D array where each row is a list of words.
        words = [word.split(' ') for word in text.splitlines()]
        space = self.font.size(' ')[0]  # The width of a space.
        max_width, max_height = self.rect.w, self.rect.h
        pos = x, y = (5, 5)
        text_heigth = 0
        for line in words:
            word0 = self.font.render(line[0], 0, self.color)
            text_heigth += word0.get_size()[1]
            if text_heigth > max_height:
                first_newline = text.index('\n')
                self.text = text = text[first_newline+1:]
                second_newline = text.index('\n')
                self.text = text = text[second_newline+1:]
            for word in line:
                word_surface = self.font.render(word, 0, self.color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                    text_heigth += word_height
                window.blit(word_surface, (x+self.rect.x, y+self.rect.y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    def draw(self, window):
        # Blit the rect.
        pygame.draw.rect(window, self.color, self.rect, 2)
