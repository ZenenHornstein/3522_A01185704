from Labs.Lab2.asteroid import Asteroid
from random import randint
from math import pi
import datetime as dt
import time


def simulate(seconds):
    """
    Simulate asteroid movements for a predefined amount of time.

    :precondition: Seconds is > 0
    :postcondition: Run simulation of asteroids for [seconds] seconds.
    :param seconds: the number of seconds to run the simulation
    """

   #Grab the start time
    start_time = dt.datetime.now()

    # fill list with the start
    times_on_the_second = [start_time + dt.timedelta(seconds=x) for x in range(seconds + 1)]

    #end_time = start_time + dt.timedelta(seconds=seconds)

    end_time = times_on_the_second[-1]
    epochs = 0



    print(f"Simulation started at {start_time}")

    while dt.datetime.now() < end_time:

        while dt.datetime.now() < times_on_the_second[epochs]:
            pass

        for asteroid in Controller.currentAsteroids:
            asteroid.move()
            print(asteroid, F"time: {dt.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
        epochs += 1



      #  time.sleep(1)


class Controller:
    currentAsteroids = []

    def __init__(self):
        """
        Create an instance of controller.
        """
        for i in range(100):
            Controller.currentAsteroids.append(Asteroid.generate_random_asteroid())


def main():
    """
    Drives the program.

    :return:
    """
    c = Controller()
    cur_time = dt.datetime.now()
    start_time = cur_time.replace(microsecond=0, second=cur_time.second + 1 % 60)
    #start_time = cur_time.replace(microsecond=0, second=cur_time.seco % 60)

    print(f"Simulation should start at {start_time}")
    delta = start_time - cur_time
    time.sleep(delta.microseconds / 1000000)
    simulate(10)

if __name__ == '__main__':
    main()
