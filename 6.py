with open('input/6.txt', 'r') as file:

    initialstate = [int(i) for i in file.readlines()[0].strip().split(",")]

    initialstate = sorted(initialstate)

    countdict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
    }

    for key in countdict.keys():
        countdict[key] = initialstate.count(key)

    for i in range(1, 257):
        for key in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            if key == 0:
                producevalue = countdict[key]
                countdict[key] = 0
            elif key == 7:
                countdict[key-1] = producevalue + countdict[key]
            elif key == 8:
                countdict[key-1] = countdict[key]
                countdict[key] = producevalue
            else:
                countdict[key-1] = countdict[key]
                countdict[key] = 0

    print(countdict)

    totalfishies = 0
    for key in countdict.keys():
        totalfishies += countdict[key]

    print(totalfishies)