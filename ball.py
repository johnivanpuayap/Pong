from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_movement = 1
        self.y_movement = 0
        self.goto(0, 0)

        self.random_start()

    def random_start(self):
        pass

    def move(self):
        self.goto(self.xcor() + self.x_movement, self.ycor() + self.y_movement)

    def wall_bounce(self):
        self.y_movement *= -1

    def paddle_bounce(self):
        self.x_movement *= -1
