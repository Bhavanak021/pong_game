from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
# tracer is used to hide the animation
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    # to update the screen and show the turtle which got hidded with tracer
    screen.update()
    ball.move()

    # detect collision  with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.turn_y()

    #  collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.turn_x()
    if ball.xcor() > 250 or ball.xcor() < -250:
        ball.speed(0.01)
    # start in opposite direction if ball misses the paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
