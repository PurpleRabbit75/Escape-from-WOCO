from cmu_graphics import *

class collidable(cmu_graphics.Shape):
    def __init__(self, x, y, width, height, fill):
        super().__init__(x, y, width, height, fill)