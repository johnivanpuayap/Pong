from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.penup()
        self.default_position = position
        self.goto(self.default_position)
        self.setheading(90)

    def move_up(self):
        self.forward(100)

    def move_down(self):
        self.backward(100)

    def reset(self):
        self.goto(self.default_position)
