from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
x_coordinates = [0, -20, -40]


#  snake and food creation
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    score.create_scoreboard()
    screen.update()
    time.sleep(0.1)

    # move the snake
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        snake.eat(food)
        food.move()
        time.sleep(0.1)
        score.score_up()

    # detect collision with itself
    for x in range(1, len(snake.segments)):
        if snake.head.distance(snake.segments[x]) < 15:
            game_is_on = False

    # detect collision with the border
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 250
        or snake.head.ycor() < -290
    ):
        game_is_on = False


screen.exitonclick()
