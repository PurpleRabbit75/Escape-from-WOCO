from cmu_graphics import *
from classes.collidable import collidable

class Wall(collidable):
    def __init__(self, *args, **kwargs):
        self.box = Line(*args, **kwargs)
