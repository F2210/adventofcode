import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

def canlook(i, j, visited):
    return (i >= 0 and i < len(rows) and j >= 0 and j < len(rows[0]) and not visited[i][j] and coordinates[i][j])

def dfs(i, j, visited):
    row_nbr = [-1, 0, 0, 1]
    col_nbr = [0, 1, -1, 0]

    visited[i][j] = True
    if coordinates[i][j] > 0:
        basin[i][j] = True

    checkarray[i][j] = basin[i][j]

    for k in range(4):
        if canlook(i + row_nbr[k], j + col_nbr[k], visited):
            dfs(i + row_nbr[k], j + col_nbr[k], visited)

with open('input/9.txt', 'r') as file:

    rows = file.readlines()

    xcounter = 0
    ycounter = 0

    lowcount = 0
    lowlist = []

    newrows = []
    for row in rows:
        newrows.append(row.strip())
    rows = newrows

    coordinates = np.array([[int(x) for x in row] for row in rows])

    for row in rows:

        xcounter = 0

        for column in row:
            column = int(column)

            checklist = [
                (column < int(row[xcounter-1]) if xcounter != 0 else ""),
                (column < int(row[xcounter+1]) if xcounter != len(row)-1 else ""),
                (column < int(rows[ycounter-1][xcounter]) if ycounter != 0 else ""),
                (column < int(rows[ycounter+1][xcounter]) if ycounter != 99 else "")
            ]

            lowest = True

            for check in checklist:
                if not check and check != "":
                    lowest = False

            if lowest:
                lowlist.append((xcounter, ycounter))
                lowcount += column + 1

            xcounter += 1

        ycounter += 1

    basincount = []

    coordinates = coordinates + 1
    coordinates = np.where(coordinates == 10, 0, coordinates)
    checkarray = coordinates
    countlist = []
    checkarray = np.array([[0 for x in row] for row in rows])
    for ylow, xlow in lowlist:
        visited = coordinates < -1
        basin = coordinates < -1
        dfs(xlow, ylow, visited)
        np.set_printoptions(linewidth=750)
        countlist.append(np.count_nonzero(basin))

    print(np.product(sorted(countlist)[-3:]))
    print(lowcount)