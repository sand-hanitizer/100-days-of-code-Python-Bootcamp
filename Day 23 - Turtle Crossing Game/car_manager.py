from random import choice, randint
from turtle import Turtle

game_is_on = True
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.all_cars = []
        self.MOVE_DISTANCE = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.goto(x=300, y=randint(-250, 250))
        self.all_cars.append(new_car)

    def move_across(self, car):
        new_x = car.xcor() - self.MOVE_DISTANCE
        new_y = car.ycor()
        car.goto(new_x, new_y)

    def speed_up(self):
        self.MOVE_DISTANCE = STARTING_MOVE_DISTANCE + MOVE_INCREMENT
