from turtle import Screen
from cars import Car
from player import Player
from score import Score
import time
import threading


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
s = Score()
cars = []

screen.listen()
screen.onkey(player.up, "Up")

def gen_cars():
    """creates new car objects from class Car()"""
    new_car = Car()
    cars.append(new_car)

def first_cars():
    """generates first 20 car objects from class Car()"""
    for i in range(20):
        new_car = Car()
        new_car.first_cars()
        cars.append(new_car)

def main():
    s.game_level()
    first_cars()


    game_on = True
    while game_on:
        time.sleep(0.1)
        screen.update()
        #need to generate cars but not too many of them and not too fast










        #new level:
        if player.distance(0, 270) <10:
            player.next_level()
            s.new_level()


        #move cars across screen:
        for i in cars:
            i.move()
            if player.distance(i) < 34:
                game_on = False
                print("end")



    screen.exitonclick()


if __name__ == '__main__':
    main()

# timer = threading.Timer(0.1, gen_cars()) #generating too fast and too many
