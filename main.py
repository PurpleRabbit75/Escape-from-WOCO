from cmu_graphics import *
from classes.wall import Wall
from classes.spawner import Spawner
from classes.pin import Pin
from classes.ball import Ball
from sprites import *

def generate_set():
    app.background = "cornflowerBlue"

    # Upper slanty Walls
    us1 = Wall(0, 0, 150, 90, lineWidth = 20)
    us2 = Wall(400, 0, 250, 90, lineWidth = 20)

    # Upper Little vertical Walls
    uv1 = Wall(us1.box.x2, us1.box.y2 + 7, 150, 0, lineWidth = 20)
    uv2 = Wall(us2.box.x2, us2.box.y2 + 7, 250, 0, lineWidth = 20)

    # Lower slanty Walls
    spacing = 70
    ls1 = Wall(us1.box.x1, spacing, us1.box.x2, us1.box.y2 + spacing, lineWidth = 20)
    ls2 = Wall(us2.box.x1, spacing, us2.box.x2, us2.box.y2 + spacing, lineWidth = 20)

    # Lower vertical Walls
    lv1 = Wall(150, 250, ls1.box.x2, ls1.box.y2 - 7, lineWidth = 20)
    lv2 = Wall(250, 250, ls2.box.x2, ls2.box.y2 - 7, lineWidth = 20)

generate_set()


TEST_SPAWNER = Spawner(200, 200, "water")

def onStep():
    TEST_SPAWNER.step()

cmu_graphics.run()