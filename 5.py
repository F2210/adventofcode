import numpy as np
import math

with open('input/5.txt', 'r') as file:

    lines = file.readlines()

    array = np.array([[0 for i in range(999)] for x in range(999)])

    for line in lines:

        coordinates = line.strip().split(" -> ")

        x1 = int(coordinates[0].split(",")[0])
        y1 = int(coordinates[0].split(",")[1])
        x2 = int(coordinates[1].split(",")[0])
        y2 = int(coordinates[1].split(",")[1])

        if x1 == x2:
            for i in range(int(math.fabs(y2 - y1))+1):
                array[x1, i+min(y2, y1)] += 1

        elif y1 == y2:
            for i in range(int(math.fabs(x2 - x1)+1)):
                array[i+min(x2, x1), y1] += 1

        elif int(math.fabs(x2 - x1)) == int(math.fabs(y2 - y1)):

            xdir = 1
            ydir = 1
            if y2 < y1:
                ydir = -1
            if x2 < x1:
                xdir = -1

            for i in range(int(math.fabs(x2 - x1))+1):
                xi = i * xdir
                yi = i * ydir

                array[xi+x1, yi+y1] += 1


    array = np.where(array < 2, 0, array)

    print(np.count_nonzero(array))

