from .Square import *


class Box(Square):

    def __init__(self, size, color, coords):
        Square.__init__(self, size)
        self.color = color
        self.coords = coords
