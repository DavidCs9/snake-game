from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
x_coordinates = [0, -20 , -40]


#  snake creation
segments = []
for x in range(len(x_coordinates)):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(x_coordinates[x], 0)
    segments.append(snake)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # move the snake
    for seg_num in range(len(segments)-1 ,0 ,-1 ):
        segments[seg_num].goto(segments[seg_num-1].xcor(), segments[seg_num-1].ycor())
    segments[0].forward(20)







screen.exitonclick()
