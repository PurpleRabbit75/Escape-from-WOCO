from cmu_graphics import *
from classes.ball import Ball

class Spawner():
    def __init__(self, x, y, fluidType):
        self.x = x
        self.y = y
        self.fluidType = fluidType
        self.children = []

    def step(self):
        if (self.fluidType == "water"):
            self.children.append(Ball(self.x, self.y, 2, fill = "blue"))
        else:
            self.children.append(Ball(self.x, self.y, 2, fill = "orange"))
        
        for particle in self.children:
            particle.centerY += 1

            

        
