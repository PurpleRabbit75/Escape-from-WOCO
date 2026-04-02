from cmu_graphics import *

Rect(0, 0, 20, 20, fill = "blue")


Sam = Group(
    Rect(40, 40, 20, 40, fill = "black"),
    Circle(50, 30, 10, fill = "black")
)

pin = Group(
    Rect(107.5, 100, 5, 50, fill = gradient("gold", "yellow")),
    Circle(110, 90, 10, fill = None, border = gradient("gold", "yellow"), borderWidth = 5),
    Rect(110-10, 100, 20, 5, fill = gradient("gold", "yellow"))
)

def onKeyPress(key):
    if key == "up":
        Sam.centerY -= 10
    elif key == "down":
        Sam.centerY += 10
    elif key == "left":
        Sam.centerX -= 10
    elif key == "right":
        Sam.centerX += 10



cmu_graphics.run()