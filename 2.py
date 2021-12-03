with open('input/2.txt', 'r') as file:
    movements = file.readlines()
    y = 0
    x = 0
    z = 0
    for move in movements:
        move = move.split(" ")
        direction = move[0]
        amount = int(move[1])
        if direction == "forward":
            x += amount
            y += (z * amount)
        elif direction == "up":
            # y -= amount
            z -= amount
        elif direction == "down":
            # y += amount
            z += amount

    result = x * y

print(result)