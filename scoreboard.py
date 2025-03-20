from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(-240,240)
        self.update_level(level)

    def update_level(self, level):
        self.clear()
        self.write(f"{level}", font=("Arial", 32, "bold"), align="center")