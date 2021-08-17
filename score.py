from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_score()
        self.hideturtle()
        self.goto(0, 270)

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=("Courier", 20, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))
