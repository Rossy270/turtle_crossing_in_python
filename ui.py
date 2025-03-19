from turtle import Turtle

class UI(Turtle):
    def __init__(self, level):
        super().__init__()
        self.penup()
        self.draw_scenario()
        self.level = level
        self.level_text = Turtle()
        self.show_level_text()
        self.hideturtle()

    def draw_scenario(self):
        self.color("white")
        self.goto(280, -200)
        self.pensize(5)
        self.setheading(90)
        self.forward(50)
        for i in range(4):
            self.setheading(180)
            self.pendown()
            self.forward(600)
            self.penup()
            self.setheading(90)
            self.forward(100)
            self.setheading(0)
            self.forward(600)
            print(self.position())

    def show_level_text(self):
        self.level_text.clear()
        self.level_text.goto(-280, 240)
        self.level_text.color("red")
        self.level_text.hideturtle()
        self.level_text.write(f"{self.level}", font = ("Arial", 32, "bold"), align = "center")

    def update_level(self, level):
        self.level = level
        self.show_level_text()

    def game_over(self):
        self.level_text.clear()
        self.clear()
        self.goto(0, 0)
        self.write(f"Você perdeu! Você foi até o level: {self.level}", font = ("Arial", 18, "bold"), align = "center")