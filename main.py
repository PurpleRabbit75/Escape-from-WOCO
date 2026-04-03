from cmu_graphics import *
from sprites import *
from fluid_sim import Lava, Water, fluid_step
if True:
    import classes.ball
    import classes.collidable
    import classes.lava
    import classes.pin
    import classes.spawner
    import classes.wall
    import classes.water
    



# def onKeyPress(key):
#     if key == "up":
#         Sam.centerY -= 10
#     elif key == "down":
#         Sam.centerY += 10
#     elif key == "left":
#         Sam.centerX -= 10
#     elif key == "right":
#         Sam.centerX += 10

# g = 0.2
# vSam_0 = 0

# def onStep():

#     fluid_step()

#     global vSam_0
#     if not Sam.hitsShape(bucket):
#         Sam.centerY += vSam_0
#         vSam_0 += g
#     else:
#         vSam_0 = 0
  

a = Rect(0, 0, 400, 400, fill = "lightblue")
print(type(a).__bases__)
    
    
    




cmu_graphics.run()