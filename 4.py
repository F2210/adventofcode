import numpy as np

def Bingo(board):
    for x in range(5):
        for row in np.count_nonzero(board == -1, axis=1):
            if row == 5:
                return True
        for row in np.count_nonzero(board == -1, axis=0):
            if row == 5:
                return True

with open('input/4.txt', 'r') as file:

    lines = file.readlines()

    drawnumbers = [int(i) for i in lines[0].strip().split(",")]

    boards = []
    board = []
    for line in lines[2:]:
        if line.strip() == "":
            boards.append(np.array(board))
            board = []
        else:
            row = [int(line[0:2]), int(line[3:5]), int(line[6:8]), int(line[9:11]), int(line[12:15])]
            board.append(row)

    nobingo = True
    stop = False
    wonboards = []
    for number in drawnumbers:
        bingolist = []
        counter = 0
        for board in boards:
            boards[counter] = np.where(boards[counter] == number, -1, boards[counter])

            if Bingo(boards[counter]):
                wonboards.append(counter)
                if len(wonboards) == 99:
                    lastboard = boards[counter]
                    lastnumber = number
                    stop = True
                # boards.pop(counter)
            counter += 1

            if stop:
                break
        if stop:
            break

    print(lastboard)
    print(np.sum(lastboard))
    print(lastnumber)
