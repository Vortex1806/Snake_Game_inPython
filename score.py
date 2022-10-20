from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.reload()

    def reload(self):
        self.clear()
        self.write(arg=f" Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(arg  = "Game Over.", move=False, align=ALIGNMENT, font=FONT)