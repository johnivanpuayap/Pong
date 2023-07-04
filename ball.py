from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.y_direction = 1
        self.x_direction = 1
        self.goto(0, 0)

        self.random_start()

    def random_start(self):
        self.x_direction = random.choice([-1, 1])
        self.y_direction = random.choice([-1, 1])

    def move(self):
        self.goto(self.xcor() + (5*self.x_direction), self.ycor() + (5*self.y_direction))

    def bounce(self):
        self.y_direction *= -1

