from cmu_graphics import *
from set import bucket

Lava = []
for i in range(100):
    Lava.append(Circle(2*i, 2*i, 5, fill = "red", border = "orange", borderWidth = 2))

Water = []
for i in range(100):
    Water.append(Circle(2*i, 400-2*i, 5, fill = "blue", border = "cyan", borderWidth = 2))


def fluid_step():
    for dot in Lava + Water:
        if not dot.hitsShape(bucket):
            dot.centerY += 2
   
            


if __name__ == "__main__":
    cmu_graphics.run()

    def onStep():
        fluid_step()