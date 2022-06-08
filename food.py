from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.goto(random.randint(-280, 280), random.randint(-280, 250))

    def move(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 250))
