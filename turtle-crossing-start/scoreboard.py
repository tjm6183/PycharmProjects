from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-175, 198)
        self.write(self.level, align="center", font=((FONT)))
        self.goto(-300, 200)
        self.text = self.write("Level: ", align="left", font=(FONT))


    def score_point(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=((FONT)))
