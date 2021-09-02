from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.high = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_score()
        self.hideturtle()
        self.goto(0, 270)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high}", align="center", font=("Courier", 16, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over.", align="center", font=("Courier", 20, "normal"))

    def reset_score(self):
        if self.score > self.high:
            with open("data.txt", mode="w") as f:
                self.high = self.score
                f.write(f"{self.high}")
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()
