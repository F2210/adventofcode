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

        elif x2 == y1 and x1 == y2:
            diagdelta = int(math.fabs(y2 - y1)) + 1

            (xstart, ystart) = (x1, y1) if x1 < x2 else (x2, y2)

            for i in range(diagdelta):
                array[xstart + i, ystart + i] += 1

        elif x1 == y1 and x2 == y2:
            diagdelta = int(math.fabs(x1 - x2)) + 1

            (ystart, xstart) = (y1, x1) if y1 < y2 else (y2, x2)

            for i in range(diagdelta):
                array[xstart + i, ystart + i] += 1

    array = np.where(array < 2, 0, array)

    print(np.count_nonzero(array))
