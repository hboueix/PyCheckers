from modules.checkerboard import Checkerboard
from modules.inputbox import InputBox
from modules.outputbox import OutputBox


class Game:

    def __init__(self):
        self.checkerboard = Checkerboard()
        self.outputbox = OutputBox(self.checkerboard.rect.w, 0, 400, 680)
        self.inputbox = InputBox(self.checkerboard.rect.w, self.outputbox.rect.h, 400, 40)


