from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        # default 20 by 20 we are making as 20 by 100 using stretch
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x_cor, y_cor)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

