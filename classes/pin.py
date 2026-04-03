from cmu_graphics import *
from classes.collidable import collidable

class pin(collidable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
