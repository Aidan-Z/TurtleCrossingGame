from turtle import Turtle
import random
COLORS = ['orange', 'green', 'blue', 'red', 'pink', 'yellow', ]
Y_RANGE = range(-240, 260)
X_RANGE = range(-295, 260)


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape('square')
        self.shapesize(stretch_wid=1.2, stretch_len=2)
        self.color(random.choice(COLORS))
        self.start = self.goto(270, random.choice(Y_RANGE))


    def move(self):
        self.backward(5)

    def first_cars(self):
        self.goto(random.choice(X_RANGE), random.choice(Y_RANGE))



