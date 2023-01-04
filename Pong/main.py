from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

first_ball = Ball((0, 0))
first_ball.move()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(first_ball.move_speed)
    screen.update()
    first_ball.move()

    if first_ball.ycor() > 280 or first_ball.ycor() < -280:
        first_ball.bounce_y()
    elif first_ball.distance(r_paddle) < 50 and first_ball.xcor() > 320 or first_ball.distance(l_paddle) < 50 and first_ball.xcor() < -320:
        first_ball.bounce_x()
    elif first_ball.xcor() > 400:
        first_ball.reset_position()
        scoreboard.l_point()
    elif first_ball.xcor() < -400:
        first_ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()