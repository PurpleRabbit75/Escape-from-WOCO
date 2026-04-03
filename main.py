from cmu_graphics import *
from sprites import *
from fluid_sim import Lava, Water, fluid_step, bucket



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

    fluid_step()

    global vSam_0
    if not Sam.hitsShape(bucket):
        Sam.centerY += vSam_0
        vSam_0 += g
    else:
        vSam_0 = 0
  

    
    
    




cmu_graphics.run()