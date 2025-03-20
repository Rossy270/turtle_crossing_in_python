from turtle import Turtle
from world_constants import SCREEN_HEIGHT

PLAYER_Y_SPAWN =  -(SCREEN_HEIGHT / 2) + 50

MOVE_SPEED = 20

class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.setheading(90)
        self.penup()
        self.respawn()


    def up(self):
        new_y = self.ycor() + MOVE_SPEED
        self.goto(self.xcor(), new_y)

    def respawn(self):
        self.goto(0, PLAYER_Y_SPAWN)