from car import Car
from world_constants import SCREEN_WIDTH

DIFFICULT_LIST = [3, 4, 5, 6, 7]
WIDTH_LIMIT_PADDING = 80
THRESHOLD_COLLISION = 38

class ManageQueueCar:
    def __init__(self, level):
        self.cars = []
        self.current_level = level
        self.create_car_list()
        self.width_limit = (SCREEN_WIDTH / 2) + WIDTH_LIMIT_PADDING

    def create_car_list(self):
        existent_pos = []
        for _ in range(DIFFICULT_LIST[self.current_level - 1]):
            new_car = Car()

            if not new_car.pos() in existent_pos:
                existent_pos.append(new_car.pos())
            else:
                while new_car.pos() in existent_pos:
                    new_car.initial_pos()

            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.move()
            self.cars_in_bound(car)

        if len(self.cars) < 1:
            self.create_car_list()


    def cars_in_bound(self, car):
        if car.xcor() < - self.width_limit:
            self.cars.remove(car)
        elif car.xcor() > self.width_limit:
            self.cars.remove(car)

    def collide_with_player(self, player):
        if len(self.cars) > 1:
            for car in self.cars:
                if car.distance(player) < THRESHOLD_COLLISION:
                    return True

            return False
        else:
            return False

    def update_difficulty(self, level):
        if level <= len(DIFFICULT_LIST):
            self.current_level = level

        for car in self.cars:
            car.remove()

        self.cars = []

    def game_over(self):
        for car in self.cars:
            car.reset()

