from turtle import Turtle

Y_SPEED = 100
X_SPEED = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.setheading(90)
        self.penup()
        self.respawn()

    def move_up(self):
        new_y = self.ycor() + Y_SPEED
        self.goto(self.xcor(), new_y)
        print(self.ycor())

    def move_down(self):
        new_y = self.ycor() - Y_SPEED
        self.goto(self.xcor(), new_y)

    def move_left(self):
        new_x = self.xcor() - X_SPEED
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + X_SPEED
        self.goto(new_x, self.ycor())

    def respawn(self):
        self.goto(0, -200)

    def arrive_finished_line(self):
        if self.ycor() >= 200:
            return True
        else:
            return False