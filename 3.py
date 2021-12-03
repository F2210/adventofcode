with open('input/3.txt', 'r') as file:
    bins = file.readlines()
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
        10: 0,
        11: 0,
    }

    gfilterdict = {}
    efilterdict = {}

    oxyrating = {}
    co2rating = {}

    newbins = []
    for bin in bins:
        newbins.append(bin.strip())
    bins = newbins

    for bin in bins:
        for value in range(0, len(bin)):
            countdict[value] += int(bin[value])

    totallines = len(bins)

    e = "0b"
    g = "0b"
    for key, value in countdict.items():
        if key == 12:
            pass
        else:
            if value >= (totallines/2):
                e += "0"
                g += "1"
            else:
                e += "1"
                g += "0"

    gbinary = g[2:]
    ebinary = e[2:]

    # the most common one is added to gamma
    # the least common one is added to epsilon

    # first coscrubber
    # when least common is 1: add all numbers with one in that place to the list
    # when equal amount of 1 and 0: add ones with 0 in that place to list

    ebinarydict = {}
    gbinarydict = {}
    oxyfilterlist = bins
    co2filterlist = bins

    co2string = ""
    for deterindex in range(0, len(ebinary)):

        co2rating[deterindex] = []
        co2binsum = 0
        for bin in co2filterlist:
            co2binsum += int(bin[deterindex])
        positive = co2binsum < (len(co2filterlist) / 2)
        co2matchingvalue = str(int(positive))
        co2string += co2matchingvalue
        for bin in co2filterlist:
            if bin[deterindex] == co2matchingvalue:
                co2rating[deterindex].append(bin)

        co2filterlist = co2rating[deterindex]

    # second oxy
    # when most common is 1: add all numbers with one in that place to the list
    # when equal amount of 1 and 0: add ones with 1 in that place to the list
    oxystring = ""
    for deterindex in range(0, len(ebinary)):

        oxyrating[deterindex] = []
        oxybinsum = 0
        for bin in oxyfilterlist:
            oxybinsum += int(bin[deterindex])
        positive = oxybinsum >= (len(oxyfilterlist) / 2)
        oxymatchingvalue = str(int(positive))
        oxystring += oxymatchingvalue
        for bin in oxyfilterlist:
            if bin[deterindex] == oxymatchingvalue:
                oxyrating[deterindex].append(bin)

        oxyfilterlist = oxyrating[deterindex]

    count = {}
    for key, list in oxyrating.items():
        count[key] = len(list)
        if len(list) == 1:
            oxyresult = list[0]

    count = {}
    for key, list in co2rating.items():
        count[key] = len(list)
        if len(list) == 1:
            co2result = list[0]

    print("result _ first exercise", int(e, 2) * int(g, 2))
    print("result _ second exercise", int("0b" + str(co2result), 2) * int("0b" + str(oxyresult), 2))