from cmu_graphics import *

class Spawner():
    def __init__(self, x, y, fluidType):
        self.x = x
        self.y = y
        self.fluidType = fluidType
        self.children = []

    def step(self):
        if (self.fluidType == "water"):
            self.children.append(Circle(self.x, self.y, 2, fill = "blue"))
        else:
            self.children.append(Circle(self.x, self.y, 2, fill = "orange"))

            

        
