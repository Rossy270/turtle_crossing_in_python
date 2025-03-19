import random
from turtle import Turtle, colormode

X_POSITION = [-300, 300]
Y_POSITION = [-100, 0, 100]

colormode(255)

def generate_random_color():
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

    return color

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid = 1, stretch_len = random.randint(2, 4))
        self.color(generate_random_color())
        self.shape("square")
        random_x = random.randint(5, 15)
        self.x_speed = random.choice([-random_x, random_x])
        self.penup()
        self.initial_pos()

    def move(self):
        new_x = self.xcor() + self.x_speed
        self.goto(new_x, self.ycor())

    def initial_pos(self):
        new_x, new_y = (0, 0)
        if self.x_speed > 0:
            new_x = X_POSITION[0]
        else:
            new_x = X_POSITION[1]

        new_y = random.choice(Y_POSITION)

        self.goto(new_x, new_y)

    def remove(self):
        self.goto(800,800)
