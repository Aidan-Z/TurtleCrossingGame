from turtle import Turtle
import random
COLORS = ['orange', 'green', 'blue', 'red', 'pink']

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color(random.choice(COLORS))
