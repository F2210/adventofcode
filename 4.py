import numpy as np

def Bingo(board):
    for x in range(5):
        row_bingo = np.count_nonzero(board[x:, ])
        column_bingo = np.count_nonzero(board[:, x])
        if not row_bingo or not column_bingo:
            print(board)
            print(np.sum(board))
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
    for number in drawnumbers:
        bingolist = []
        counter = 0
        for board in boards:
            boards[counter] = np.where(boards[counter] == number, 0, boards[counter])

            if Bingo(boards[counter]):
                print(len(boards))
                boards.pop(counter)
                print(number)
                print(len(boards))
            else:
                counter += 1
