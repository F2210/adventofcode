
with open('input/1.txt', 'r') as file:
    numbers = file.readlines()
    lcount = 0
    hcount = 3
    larger = -1
    oldnumber = 0
    for number in numbers[1:]:
        print([int(i) for i in numbers[lcount : hcount]])
        number = sum([int(i) for i in numbers[lcount : hcount]])
        print(number)
        if oldnumber < number:
            larger += 1
        lcount += 1
        hcount += 1
        oldnumber = number

    print(larger)