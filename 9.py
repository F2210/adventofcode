import numpy as np


def isSafe(i, j, visited):
    return (i >= 0 and i < len(rows) and j >= 0 and j < len(rows[0]) and not visited[i][j] and coordinates[i][j])

def DFS(i, j, visited):
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

    visited[i][j] = True

    for k in range(8):
        if isSafe(i + rowNbr[k], j + colNbr[k], visited):
            DFS(i + rowNbr[k], j + colNbr[k], visited)

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

    coordinates = np.where(coordinates == 9, 0, coordinates)

    visited = coordinates < -1

    count = 0
    for i in range(len(row)):
        for j in range(len(row[0])):
            if visited[i][j] == False and coordinates[i][j] == 1:
                DFS(i, j, visited)
                count += 1

    print(count)

    print(lowcount)