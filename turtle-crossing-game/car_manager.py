COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from  turtle import Turtle
import random
import time
class CarManager:
    def __init__(self):
        self.car_list = []
        self.starting_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:

            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250,250)
            new_car.goto(300,new_y)
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.starting_distance)

    def increase_speed(self):
        self.starting_distance += MOVE_INCREMENT
        self.move_cars()
