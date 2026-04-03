from cmu_graphics import *
from classes.ball import ball

class lava(ball):
    def __init__(self, *args, **kwargs):
        dot =Circle(*args, **kwargs)
