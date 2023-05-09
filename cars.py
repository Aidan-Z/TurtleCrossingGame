from turtle import Turtle
import random
COLORS = ['orange', 'green', 'blue', 'red', 'pink', 'yellow', ]
Y_RANGE = range(-295, 260)


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color(random.choice(COLORS))
        self.start = self.goto(290, random.choice(Y_RANGE))


    def move(self):
        self.backward(5)



