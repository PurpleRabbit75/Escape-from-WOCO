from cmu_graphics import *
from classes.collidable import collidable

class wall(collidable):
    def __init__(self, x, y, width, height, fill):
        super().__init__(x, y, width, height, fill)
