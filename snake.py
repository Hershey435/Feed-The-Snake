from turtle import Turtle

STARTING_POSITIONS = {(-40, 0), (-20, 0), (0, 0)}
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)

        self.segments.append(t)

    def create_snake(self):

        for i in STARTING_POSITIONS:
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(i)

            self.segments.append(t)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            nx = self.segments[seg - 1].xcor()
            ny = self.segments[seg - 1].ycor()
            self.segments[seg].goto(nx, ny)
        self.head.forward(MOVE_DIS)

    # def can_snake_move(self):
    #     if self.head.xcor() !=
