from turtle import Turtle
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
DIRECTION=[0,90,180,270]
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)
    def add_segment(self,i):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(i)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.segments[0].heading() != DIRECTION[3]:
           self.segments[0].seth(90)
    def down(self):
        if self.segments[0].heading() != DIRECTION[1]:
           self.segments[0].seth(270)
    def left(self):
        if self.segments[0].heading() != DIRECTION[0]:
           self.segments[0].seth(180)
    def right(self):
        if self.segments[0].heading() != DIRECTION[2]:
           self.segments[0].seth(0)

