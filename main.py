from cmu_graphics import *
from objects import *



def onKeyPress(key):
    if key == "up":
        Sam.centerY -= 10
    elif key == "down":
        Sam.centerY += 10
    elif key == "left":
        Sam.centerX -= 10
    elif key == "right":
        Sam.centerX += 10

g = 0.2
vSam_0 = 0

def onStep():
    global vSam_0
    if Sam.hitsShape(pin):
        pin.fill = "red"
    else:
        pin.fill = gradient("gold", "yellow")
    
    Sam.centerY += vSam_0
    vSam_0 += g
    




cmu_graphics.run()