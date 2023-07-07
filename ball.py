from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_movement = 1
        self.y_movement = 1
        self.ball_speed = 0.005
        self.goto(0, 0)

        self.random_start()

    def random_start(self):
        self.x_movement *= random.choice([-1, 1])
        self.y_movement *= random.choice([-1, 1])

    def move(self):
        self.goto(self.xcor() + self.x_movement, self.ycor() + self.y_movement)

    def wall_bounce(self):
        self.y_movement *= -1

    def paddle_bounce(self):
        self.x_movement *= -1

    def reset(self):
        self.goto(0, 0)
        self.ball_speed = 0.005
        self.random_start()

    def increase_speed(self):
        self.ball_speed -= 0.001
