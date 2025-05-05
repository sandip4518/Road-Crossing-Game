import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move_player,"Up")

cars= CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    scoreboard.scoreboard()

    #detect the collision with the car.
    for car in cars.car_list:
        if car.distance(player) < 30 :
            scoreboard.game_over()
            game_is_on = False

    #detect player cross the road.
    if player.ycor() > player.finish_line :
        scoreboard.increase_level()
        player.reset_position()
        cars.increase_speed()


screen.exitonclick()