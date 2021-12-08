import re

with open('input/8.txt', 'r') as file:

    lines = file.readlines()

    patternsbase = {
        7: 8,
        3: 7,
        4: 4,
        2: 1,
    }

    segmentcount = 0

    for line in lines:
        line = line.strip().split(" | ")
        linenumberdict = {}
        for length, number in patternsbase.items():
            for segment in line[0].split(" "):
                if length == len(segment):
                    linenumberdict[number] = r"".join(f"[{i}]" for i in segment)

        print(linenumberdict)

        for segment in line[0].strip().split(" "):
            if len(segment) == 6:
                print(bool(re.search(linenumberdict[4], segment)))
                print(bool(re.search(linenumberdict[1], segment)))
            if len(segment) == 6 and bool(re.search(linenumberdict[4], segment)) and bool(re.search(linenumberdict[1], segment)):
                print("found 9")
                linenumberdict[9] = r"".join(f"[{i}]" for i in segment)
            elif len(segment) == 6 and not bool(re.search(linenumberdict[4], segment)) and bool(re.search(linenumberdict[1], segment)):
                print("found 0")
                linenumberdict[0] = r"".join(f"[{i}]" for i in segment)
            elif len(segment) == 6 and not bool(re.search(linenumberdict[4], segment)) and not bool(re.search(linenumberdict[1], segment)):
                print("found 6")
                linenumberdict[6] = r"".join(f"[{i}]" for i in segment)

        print(linenumberdict)

        for letter in linenumberdict[9]:
            intwo = linenumberdict[6].replace(letter, "")

        for segment in line[0].split(" "):
            if len(segment) == 5 and not bool(re.search(str(r"".join(f"[{i}]" for i in linenumberdict[1])), segment)):
                if intwo in segment:
                    linenumberdict[2] = segment
                else:
                    linenumberdict[5] = segment
            elif len(segment) == 5:
                linenumberdict[3] = segment

        print(linenumberdict)
