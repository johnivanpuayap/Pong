from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create Paddle
player_one = Paddle((-350, 0))
player_two = Paddle((350, 0))

# Player One Controls
screen.onkey(player_one.move_up, "W")
screen.onkey(player_one.move_up, "w")
screen.onkey(player_one.move_down, "S")
screen.onkey(player_one.move_down, "s")

# Player Two Controls
screen.onkey(player_two.move_up, "Up")
screen.onkey(player_two.move_down, "Down")

# Create Ball
ball = Ball()

is_game_on = True

while is_game_on:
    screen.update()
    screen.listen()
    screen.tracer(1)

    ball.move()

    if ball.ycor() == 300 or ball.ycor() == -300:
        ball.bounce()


screen.exitonclick()