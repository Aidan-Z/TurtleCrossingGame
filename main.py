from turtle import Screen
from cars import Car
from player import Player
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
cars = []
player = Player()

screen.listen()
screen.onkey(player.up, "Up")



def main():
    for i in range(15): #need to creat timer so they generate every x seconds, random range number
        new_car = Car()
        cars.append(new_car)

    game_on = True
    while game_on:
        time.sleep(0.1)
        screen.update()

        for i in cars[:]:
            i.move()
            if player.distance(i) < 40:
                game_on = False











    screen.exitonclick()


if __name__ == '__main__':
    main()
