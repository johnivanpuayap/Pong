from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(xcor, ycor)
        self.setheading(90)

    def move_up(self):
        print("Moving Up")
        self.forward(100)

    def move_down(self):
        print("Moving Down")
        self.backward(100)
