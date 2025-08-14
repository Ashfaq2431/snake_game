from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score=0
        self.goto(0,270)
        self.write(f"score:{self.score}", align="center", font=('Arial', 15, "normal"))

    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"score:{self.score}", align="center", font=('Arial', 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=('Arial', 15, "normal"))

