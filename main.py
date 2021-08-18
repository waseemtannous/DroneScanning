from djitellopy import Tello
from time import sleep
from utils import *
from plot import *

import threading

ROTATE_ANGLE = 30
MAX_ANGLE = 360


def move(drone):
    drone.move_forward(20)
    drone.move_back(20)


def drone360():
    drone = Tello()
    drone.connect()

    print(drone.get_battery())

    drone.streamoff()
    drone.streamon()

    x = threading.Thread(target=runOrbSlam2)
    x.start()

    drone.takeoff()

    drone.move_up(80)

    angle = 0

    sleep(4)

    print('Starting ...')

    while angle <= MAX_ANGLE:
        drone.rotate_clockwise(10)
        # move(drone)
        angle += 10
        sleep(3)

    drone.end()
    x.join()


if __name__ == '__main__':
    # plot2D(x, z)
    # # plotConvexHull(x, y)
    # KMeansAlgo(x, z)
    # x1 = [2.87091167, 0.39248181, 1.67489614, 15.01441968]
    # y1 = [1.00472885, 1.02433301, -0.04094384, 0.6501901]
    # plot2D(x1, y1)
    # drone360()
    x, y, z = readCSV('PointData/pointDataSaloon.csv')
    # for i in range(len(x)):
    #     x[i] = x[i] * 100
    #
    # for i in range(len(y)):
    #     y[i] = y[i] * 100
    #
    # for i in range(len(z)):
    #     z[i] = z[i] * 100
    #
    plot2D(x, z)
    showCloud(x, y, z)
