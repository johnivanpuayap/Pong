from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.player_one_score = 0
        self.player_two_score = 0
        self.draw_board()

    def draw_board(self):
        self.goto(0, -300)
        self.setheading(90)
        self.penup()

        while self.ycor() <= 300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

        self.goto(-20, 280)
        self.pendown()
        self.write(f"{self.player_one_score}")
        self.penup()

        self.goto(20, 280)
        self.pendown()
        self.write(f"{self.player_two_score}")
        self.penup()
        self.hideturtle()