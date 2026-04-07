from cmu_graphics import *
from time import sleep
import threading
import random

class Walls():
    def __init__(self):
        self.walls = []

    def add_wall(self, wall):
        self.walls.append(wall)

class Spawner():
    def __init__(self, x, y, num_balls, fluid_type, walls):
        self.balls = []
        self.x = x
        self.y = y
        self.num_balls = num_balls
        self.num_balls_spawned = 0
        self.walls = walls
        self.fluid_type = fluid_type

    def spawn_balls(self):
        radius = 5

        for i in range(self.num_balls):
            if self.fluid_type == "water":
                fill="blue"    
            elif self.fluid_type == "lava":
                fill="orange"

            self.balls.append(Circle(self.x + random.uniform(-10, 10), self.y + random.uniform(-10, 10), radius, fill=fill))


            self.num_balls_spawned += 1

    def sign(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    def move_balls_by_gravity(self):
        for ball in self.balls:
            ball.centerY += 4

    def move_balls_by_ball_collision(self):
        balls_want_to_move_like_this = [[0, 0] for i in range(self.num_balls_spawned)]
        collisions = [0 for i in range(self.num_balls_spawned)]

        repulsion_damper = 32
        for i in range(self.num_balls_spawned):
            for j in range(self.num_balls_spawned):
                if i == j:
                    pass

                b1 = self.balls[i]
                b2 = self.balls[j]

                diffX = b1.centerX - b2.centerX
                diffY = b1.centerY - b2.centerY

                if b1.hitsShape(b2) and abs(diffX) + abs(diffY) < (6*b1.radius)/4:
                    
                    # only check this many times per ball, otherwise it gets really laggy
                    collisions[i] += 1
                    if collisions[i] > 2:
                        break;
                    
                    # if this ball is being pushed up by another ball, undo the effects of gravity
                    if diffY < 0:
                        b1.centerY -= 4
                    
                    move_X_by = (2*(b1.radius + abs(diffX) + abs(diffX)))*self.sign(diffX) / repulsion_damper
                    move_Y_by = (2*(b1.radius + abs(diffY) + abs(diffY)))*self.sign(diffY) / repulsion_damper

                    balls_want_to_move_like_this[i][0] += move_X_by
                    balls_want_to_move_like_this[i][1] += move_Y_by
                    
        for i in range(self.num_balls_spawned):
            if collisions[i] > 0:
                balls_want_to_move_like_this[i][0] /= collisions[i]
                balls_want_to_move_like_this[i][1] /= collisions[i]

                if balls_want_to_move_like_this[i][0] != 0:
                    self.balls[i].centerX += balls_want_to_move_like_this[i][0]
                if balls_want_to_move_like_this[i][1] != 0:
                    self.balls[i].centerY += balls_want_to_move_like_this[i][1]


    def move_balls_by_wall_collision(self):
        for ball in self.balls:
            if ball.centerX - ball.radius < 0:
                ball.centerX = ball.radius
            elif ball.centerX + ball.radius > 400:
                ball.centerX = 400 - ball.radius

            if ball.centerY - ball.radius < 0:
                ball.centerY = ball.radius
            elif ball.centerY + ball.radius > 400:
                ball.centerY = 400 - ball.radius

            for wall in self.walls.walls:
                if ball.hitsShape(wall):
                    if wall.rotateAngle == 0:
                        ball.centerY -= ball.radius/1.5
                    if wall.rotateAngle < 0:
                        ball.centerX -= ball.radius/1.5
                        ball.centerY -= ball.radius/1.5
                    if wall.rotateAngle > 0:
                        ball.centerX += ball.radius/1.5
                        ball.centerY -= ball.radius/1.5


    def move_balls(self):
        self.move_balls_by_gravity()
        self.move_balls_by_ball_collision()
        self.move_balls_by_wall_collision()

    def step(self):
        self.move_balls()

walls = Walls()
walls.add_wall(Rect(125, 200, 100, 20, rotateAngle=20, fill="black", align="center"))
walls.add_wall(Rect(275, 200, 100, 20, rotateAngle=-20, fill="black", align="center"))

lava_spawner = Spawner(125, 100, 50, "lava", walls)
lava_spawner.spawn_balls()

water_spawner = Spawner(275, 100, 50, "water", walls)
water_spawner.spawn_balls()

sleep(0.5)

def onStep():
    lava_spawner.step()
    water_spawner.step()

cmu_graphics.run()