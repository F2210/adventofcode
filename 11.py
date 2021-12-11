import numpy as np

with open('input/11.txt', 'r') as file:

    lines = file.readlines()

    newlines = []
    for line in lines:
        newlines.append(line.strip())
    lines = newlines

    array = np.array([[int(i) for i in line] for line in lines])

    rownr = [-1, -1, -1,  0, 1,  1, 0, 1]
    colnr = [ 0, -1,  1, -1, 1, -1, 1, 0]

    stepcounter = 0
    flashcounter = 0
    notfinished = True
    while notfinished:
        array = array + 1
        flashed = array < -1
        notallflashed = True
        while notallflashed:
            results = np.where(array > 9)
            array = np.where(array > 9, 0, array)
            if len(results[0]) == 0:
                for i in range(len(results[0])):
                    if flashed[results[0][i], results[1][i]]:
                        array[results[0][i], results[1][i]] = 0
                notallflashed = False
                flashed = array < -1
            else:
                for i in range(len(results[0])):
                    flashcounter += 1
                    if not flashed[results[0][i], results[1][i]]:
                        # print(array)
                        for j in range(len(rownr)):
                            xcoor = results[0][i]+colnr[j]
                            ycoor = results[1][i]+rownr[j]
                            if -1 < xcoor < 10 and -1 < ycoor < 10:
                                array[xcoor, ycoor] += 1
                            else:
                                pass
                        # print(array)
                    array[results[0][i], results[1][i]] = 0
                    flashed[results[0][i], results[1][i]] = True

        if stepcounter == 100:
            print(flashcounter)
            notfinished = False
        else:
            stepcounter += 1
        if np.count_nonzero(flashed) == 100:
            print(stepcounter)

    #  WAT GAAT ER FOUT?

    print(flashcounter)


