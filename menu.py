from turtle import Turtle


class Menu(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.draw_menu()

    def draw_menu(self):
        self.goto(0, 200)
        self.write(f"Pong", True, align="center", font=("Courier", 60, "normal"))

        self.goto(0, -200)
        self.write(f"Press 'p' or 'P' to start Playing", True, align="center", font=("Courier", 12, "normal"))
        self.hideturtle()
