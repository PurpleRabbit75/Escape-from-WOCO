from cmu_graphics import *
from classes.wall import wall
from sprites import *
if True:
    import classes.ball
    import classes.collidable
    import classes.lava
    import classes.pin
    import classes.spawner
    import classes.wall
    import classes.water
    

def generate_set():
    wall(0, 0, 150, 80, lineWidth = 20)
    wall(400, 0, 250, 80, lineWidth = 20)

generate_set()


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
  

    

    
    




cmu_graphics.run()