import random
from turtle import Turtle, colormode

LEVEL_SPEED = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

colormode(255)

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0 ,255)
    b = random.randint(0, 255)

    return r,g,b

class Car(Turtle):
    def __init__(self, level):
        super().__init__(shape="square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(generate_random_color())
        self.move_speed = LEVEL_SPEED[level - 1]
        self.goto(random.randint(350, 800), random.randint(-250, 250))

    def move(self):
        new_x = self.xcor() - self.move_speed
        self.goto(new_x, self.ycor())

    def die(self):
        self.reset()
        self.hideturtle()

    def update_speed(self, level):
        if level > len(LEVEL_SPEED):
            return

        self.move_speed = LEVEL_SPEED[level - 1]
