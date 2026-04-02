from cmu_graphics import *

Rect(0, 0, 20, 20, fill = "blue")


Sam = Group(
    Rect(40, 40, 20, 40, fill = "black"),
    Circle(50, 30, 10, fill = "black")
)


cmu_graphics.run()