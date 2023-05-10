from turtle import Screen
from cars import Car
from player import Player
from score import Score
import time
import threading


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

new_car = Car()
player = Player()
score = Score()


cars = []


screen.listen()
screen.onkey(player.up, "Up")


def main():
    score.game_level()

    game_on = True
    while game_on:
        time.sleep(0.1)
        screen.update()
        new_car.gen_car()
        # cars.append(new_car)
        new_car.move()



        #new level:
        if player.distance(0, 280) <10:
            player.next_level()
            score.new_level()


        #check distance of player from car
        for i in new_car.cars: #accessing class attribute (list of stored car objects)
            if player.distance(i) < 35:
                game_on = False
                print("end")




    screen.exitonclick()


if __name__ == '__main__':
    main()

# timer = threading.Timer(0.1, gen_cars()) #generating too fast and too many
