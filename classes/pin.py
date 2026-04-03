from cmu_graphics import *
from classes.collidable import Collidable

class Pin(Collidable):
    def __init__(self, *args, **kwargs):
        pin = Group(
            Rect(107.5, 100, 5, 50, fill = gradient("gold", "yellow")),
            Circle(110, 90, 10, fill = None, border = gradient("gold", "yellow"), borderWidth = 5),
            Rect(110-10, 100, 20, 5, fill = gradient("gold", "yellow"))
        )
