import random
import time, world_constants
from turtle import Screen, Turtle
from player import Player
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width= world_constants.SCREEN_WIDTH, height= world_constants.SCREEN_HEIGHT)
screen.title("Crossing street")
screen.listen(False)
screen.bgcolor("white")
screen.tracer(0)

player = Player()


screen.onkey(fun=player.up, key= "w")

cars = []
level = 1
game_is_on = True

scoreboard = Scoreboard(level)

def create_car():
    if len(cars) < 20:
        new_car = Car(level)
        cars.append(new_car)

while game_is_on:
    screen.update()
    time.sleep(0.1)

    create_car()

    #Faz o carro se mover
    for car in cars:
        car.move()

        if car.xcor() < -world_constants.SCREEN_WIDTH / 2:
            cars.remove(car)
            car.die()

    #Checando a collisão
    for car in cars:
        if car.distance(player) < 20:
            game_is_on = False

    #Checando se o player chegou na linha de chegada
    if player.ycor() > 240:
        player.respawn()
        level += 1
        scoreboard.update_level(level)
        for car in cars:
            car.update_speed(level)


screen.exitonclick()