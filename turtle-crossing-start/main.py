import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

cars = []
cars_2 = []
lower_range = 0
upper_range = random.randrange(1, 21)
for num_of_cars in range(lower_range, upper_range):
    cars.append(num_of_cars)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

user = Player()

for car in cars:
    cars_2.append(CarManager())



screen.listen()
screen.onkey(user.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    for car in cars_2:
        car.move()
        if car.xcor() < -400:
            car.back_to_right()
    screen.update()
