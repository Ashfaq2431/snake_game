from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"SCORE:{self.score} HIGH SCORE:{self.high_score}",align='center',font=("courier",24,"normal"))

    def add(self):
        self.clear()
        self.write(f"SCORE:{self.score} HIGH SCORE:{self.high_score}",align='center',font=("courier",24,"normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt','w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.add()

    def increase(self):
        self.score += 1
        self.add()



