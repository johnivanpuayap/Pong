import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from menu import Menu


def start_game():
    global is_on_menu
    is_on_menu = False
    menu.clear()
    score.draw_board()
    is_game_on = True

    while is_game_on:
        screen.update()
        time.sleep(ball.ball_speed)
        ball.move()

        # Detect collision with wall
        if ball.ycor() == 290 or ball.ycor() == -290:
            ball.wall_bounce()

        # Detect collision with puddle
        if ball.distance(player_one) < 50 and ball.xcor() < -340 or (
                ball.distance(player_two) < 50 and ball.xcor() > 340):
            ball.paddle_bounce()
            ball.increase_speed()

        # Detect if a user score
        if ball.xcor() >= 380:
            score.add_score('1')
            score.update_score()
            screen.update()
            is_game_on = False

        if ball.xcor() <= -380:
            score.add_score('2')
            score.update_score()
            screen.update()
            is_game_on = False

    screen.exitonclick()


def play_game():
    if is_on_menu:
        start_game()


def continue_game():
    player_one.reset()
    player_two.reset()
    ball.reset()
    score.continue_score()
    start_game()


def restart_game():
    player_one.reset()
    player_two.reset()
    ball.reset()
    score.reset_score()
    start_game()


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

# Game Controls
screen.onkey(continue_game, "C")
screen.onkey(continue_game, "c")
screen.onkey(restart_game, "R")
screen.onkey(restart_game, "r")
screen.onkey(play_game, "P")
screen.onkey(play_game, "p")
screen.listen()

# Create Ball
ball = Ball()

# Create Scoreboard
score = Scoreboard()

is_on_menu = True
menu = Menu()

screen.exitonclick()
