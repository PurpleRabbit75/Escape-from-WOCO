from cmu_graphics import *
from classes.collidable import collidable

class wall(collidable):
    def __init__(self, *args, **kwargs):
        box = Line(*args, **kwargs)
