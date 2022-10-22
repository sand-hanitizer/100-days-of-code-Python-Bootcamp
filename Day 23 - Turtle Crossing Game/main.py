import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

TOP_EDGE = 270
game_is_on = True
count = 1
NUM = 8
sleep = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
screen.onkey(fun=turtle.move_up, key="Up")

manager = CarManager()

scoreboard = Scoreboard()

while game_is_on:
    time.sleep(sleep)
    screen.update()
    count += 1
    if count % NUM == 0:
        car = manager.create_car()
        count = 0

    for car in manager.all_cars:
        manager.move_across(car)
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.ycor() > TOP_EDGE:
        turtle.return_turtle()
        manager.speed_up()

        sleep *= 0.9
        if NUM != 1: NUM -= 1

        scoreboard.level += 1
        scoreboard.clear()
        scoreboard.level_update()


screen.exitonclick()
