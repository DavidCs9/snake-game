from turtle import Turtle, Screen


class Snake():
    def __init__(self):
        self.x_coordinates = [0, -20 , -40]
        self.segments = []
        for x in range(len(self.x_coordinates)):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(self.x_coordinates[x], 0)
            self.segments.append(snake) 

    def move(self):
        for seg_num in range(len(self.segments)-1 ,0 ,-1 ):
            self.segments[seg_num].goto(self.segments[seg_num-1].xcor(), self.segments[seg_num-1].ycor())
        self.segments[0].forward(20)