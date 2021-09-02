from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)

snake = Snake()
food = Food()
score = Score()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")
# sc.onkey(sc.exitonclick, "space")


is_game_on = True
while is_game_on:
    sc.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        score.add_score()
        snake.extend()
        food.refresh()

    # Collision with wall
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x > 270 or x < -270 or y > 270 or y < -270:
        score.reset_score()
        snake.reset()

    # Collision with tail
    for segment in range(0, len(snake.segments) - 1):
        if snake.segments[segment] == snake.head:
            # print("1")
            pass
        elif snake.head.distance(snake.segments[segment]) < 5:
            # print("2")
            score.reset_score()
            snake.reset()

sc.exitonclick()
