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

        self.update_score()

    def update_score(self):
        self.goto(-20, 260)
        self.write(f"{self.player_one_score}", True, align="center", font=("Courier", 24, "normal"))

        self.goto(20, 260)
        self.write(f"{self.player_two_score}", True, align="center", font=("Courier", 24, "normal"))
        self.hideturtle()

    def add_score(self, player):
        self.clear()
        self.goto(0, 0)

        if player == '1':
            self.write(f"Player One Scored!", True, align="center", font=("Courier", 24, "normal"))
            self.player_one_score += 1
        else:
            self.write(f"Player Two Scored!", True, align="center", font=("Courier", 24, "normal"))
            self.player_two_score += 1

        self.goto(0, -20)
        self.write("Press 'c' or 'C' to continue playing again!", True, align="center", font=("Courier", 12, "normal"))
        self.goto(0, -40)
        self.write("Press 'r' or 'R' to restart the game!", True, align="center", font=("Courier", 12, "normal"))

    def continue_score(self):
        self.clear()
        self.draw_board()

    def reset_score(self):
        self.clear()
        self.player_one_score = 0
        self.player_two_score = 0
        self.draw_board()
