import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.num_cars = random.randrange(0, 20)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.generate_car()
        self.move()

    def generate_car(self):
        self.shape("square")
        self.color(COLORS[random.randrange(0, 6)])
        self.shapesize(stretch_wid=1.2, stretch_len=2)
        self.penup()
        self.goto(random.randint(200, 900), random.randint(-250, 300))

    def move(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def back_to_right(self):
        new_x = self.xcor() + 800
        new_y = random.randint(-250, 300)
        self.goto(new_x, new_y)

    def speed_up(self):
        self.move_speed *= .8

    def stop(self):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x, new_y)
