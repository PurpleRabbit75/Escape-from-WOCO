from cmu_graphics import *
from classes.collidable import Collidable

class Wall(Collidable):
    def __init__(self, *args, **kwargs):
        self.box = Line(*args, **kwargs)
