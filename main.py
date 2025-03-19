import time
import world_constants
from turtle import Screen, Turtle
from player import Player
from ui import UI
from manage_queue_car import ManageQueueCar

screen = Screen()
screen.setup(width = world_constants.SCREEN_WIDTH, height = world_constants.SCREEN_HEIGHT)
screen.title("Turtle Crossing")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()



player = Player()


screen.onkey(fun=player.move_up, key="w")
screen.onkey(fun=player.move_down, key="s")
screen.onkey(fun=player.move_left, key="a")
screen.onkey(fun=player.move_right, key="d")

game_is_on = True
current_level = 1
ui = UI(current_level)
queue_car = ManageQueueCar(current_level)

def game_over():
    queue_car.game_over()
    player.reset()
    ui.game_over()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    queue_car.move_cars()

    if queue_car.collide_with_player(player):
        game_is_on = False
        game_over()

    if player.arrive_finished_line():
        time.sleep(0.2)
        player.respawn()
        current_level += 1
        ui.update_level(current_level)
        queue_car.update_difficulty(current_level)



screen.exitonclick()