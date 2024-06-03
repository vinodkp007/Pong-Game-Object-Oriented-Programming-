from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("PONG GAME")
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
#     detect collision with the paddle
#     see since the distance method is calculated from the center of paddle object u can't use < 20
#     hence < 50 distance b/w paddle and ball is perfect and also calculating the x cor makes it perfect combination
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect if R-paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    # detect if L-paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
screen.exitonclick()