import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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
screen.listen()

# Create Ball
ball = Ball()

# Create Scoreboard
score = Scoreboard()

is_game_on = True

while is_game_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() == 300 or ball.ycor() == -300:
        ball.wall_bounce()

    # Detect collision with puddle
    if ball.distance(player_one) < 50 and ball.xcor() < -340 or (ball.distance(player_two) < 50 and ball.xcor() > 340):
        ball.paddle_bounce()

    # Detect if a user score
    if ball.xcor() >= 380:
        print("Player one scored")
        is_game_on = False

    if ball.xcor() <= -380:
        print("Player two scored")
        is_game_on = False

screen.exitonclick()