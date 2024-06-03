from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        # setting the ball properties as all we need
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.04
    def move(self):
        # we are increasing x and y so that the ball moves to the right of the screen
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # the y co-ordinate is decreasing if it was increasing when the ball was hitting the wall(top wall)
        # the y co-ordinate is increasing if it was decreasing when the ball was hitting the bottom wall
        self.y_move = self.y_move * -1

    def bounce_x(self):
        # same as it does to bounce_y but here the variations are on x co-ordinate
        self.x_move = self.x_move * -1

        # added at the end of creating game to increase the speed of the ball once it touches the paddle
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        # imp reverses the direction of x
        self.bounce_x()

        # resetting speed of ball to it's original value
        self.move_speed = 0.07

