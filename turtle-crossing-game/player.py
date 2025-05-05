

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1.5)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.finish_line = FINISH_LINE_Y

    def move_player(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)
