from cmu_graphics import *

bucket = Rect(20, 350, 200, 50, fill = "brown", border = "saddlebrown", borderWidth = 5)

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