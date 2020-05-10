from .Rectangle import *


class CheckerBox(Rectangle):

    def __init__(self, size, color, coords):
        Rectangle.__init__(self, size, size)
        self.color = color
        self.coords = coords
