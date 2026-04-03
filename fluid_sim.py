from cmu_graphics import *

Lava = []

for i in range(100):
    Lava.append(Circle(2*i, 2*i, 5, fill = "red", border = "orange", borderWidth = 2))

Water = []
for i in range(100):
    Water.append(Circle(2*i, 400-2*i, 5, fill = "blue", border = "cyan", borderWidth = 2))


def fluid_step():
    for lava in Lava:
        lava.centerY += 1
    for water in Water:
        water.centerY -= 1


if __name__ == "__main__":
    cmu_graphics.run()