import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

num_of_entities = []
cars = []
count_of_times = 0
lower_range = 0
upper_range = random.randrange(1, 40)
for num_of_cars in range(lower_range, upper_range):
    num_of_entities.append(num_of_cars)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()

user = Player()

for car in num_of_entities:
    cars.append(CarManager())



screen.listen()
screen.onkey(user.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    for car in cars:
        if user.distance(car) < 25:
            scoreboard.game_over()
            screen.update()
            time.sleep(5)
            game_is_on = False
        elif user.ycor() > 280:
            user.reset()
            scoreboard.score_point()
            scoreboard.update_scoreboard()
            for car in cars:
                car.back_to_right()
                car.speed_up()
        elif car.xcor() < -400:
            car.back_to_right()
            count_of_times += 1
            if count_of_times % 6 == 0:
                cars.append((CarManager()))
        else:
            car.move()


    screen.update()
