from  turtle import Turtle

FONT = ("Courier", 25, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()

    def scoreboard(self):
        self.clear()
        self.goto(-195,260)
        self.write(f"Game Level {self.level}", align="center", font=("Courier", 20, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.",align="center",font=FONT)

    def increase_level(self):
        self.level += 1
        self.scoreboard()
