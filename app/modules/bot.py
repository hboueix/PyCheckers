from modules.player import Player
from modules.checkerpiece import Checkerpiece


class Bot(Player):

    def __init__(self, color):
        self.color = color
        start_pos = []
        for j in range(0, 3):
            for i in range(8):
                if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                    start_pos.append((i * 85, 40 + j * 85))
        self.checkerpieces = [Checkerpiece(color, pos) for pos in start_pos]