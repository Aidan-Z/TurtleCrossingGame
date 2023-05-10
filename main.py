from turtle import Screen
from cars import Car
from player import Player
from score import Score
import time


def main():

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    new_car = Car()
    player = Player()
    score = Score()

    screen.listen()
    screen.onkey(player.up, "Up")
    score.game_level()

    game_on = True
    while game_on:
        time.sleep(0.1)
        screen.update()
        new_car.gen_car()
        new_car.move()



        #new level:
        if player.distance(0, 280) <10:
            player.next_level()
            score.new_level()
            new_car.speed_up()



        #check distance of player from car
        for i in new_car.cars: #accessing class attribute (list of stored car objects)
            if player.distance(i) < 30:
                score.game_over()
                game_on = False


    screen.exitonclick()


if __name__ == '__main__':
    main()

