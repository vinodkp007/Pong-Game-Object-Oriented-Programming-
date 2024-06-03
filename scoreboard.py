from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        self.x = 0
        self.y = 0

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=self.r_score, align="center", font=("Arial", 80, "normal"))
    def l_point(self):
        self.l_score += 1
        self.update_score()
    def r_point(self):
        self.r_score += 1
        self.update_score()