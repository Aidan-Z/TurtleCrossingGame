from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-260, 270)
        self.color('black')
        self.hideturtle()
        self.speed(0)

    def game_level(self):
        self.write(f"level: {self.level}", align='center', font=('Helvetica', 20, 'normal'))

    def new_level(self):
        self.clear()
        self.level += 1
        self.game_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Helvetica', 20, 'normal'))






