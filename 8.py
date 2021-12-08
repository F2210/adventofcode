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
        segmentdict = {}
        for length, number in patternsbase.items():
            for segment in line[0].split(" "):
                if length == len(segment):
                    linenumberdict[number] = r"^".join(f"(?=.*{i})" for i in segment)
                    segmentdict[number] = len(segment)

        for segment in line[0].strip().split(" "):
            if len(segment) == 6 and bool(re.search(linenumberdict[4], segment)) and bool(re.search(linenumberdict[1], segment)):
                segment9 = segment
                linenumberdict[9] = r"^".join(f"(?=.*{i})" for i in segment)
                segmentdict[9] = len(segment)
            elif len(segment) == 6 and not bool(re.search(linenumberdict[4], segment)) and bool(re.search(linenumberdict[1], segment)):
                linenumberdict[0] = r"^".join(f"(?=.*{i})" for i in segment)
                segmentdict[0] = len(segment)
            elif len(segment) == 6 and not bool(re.search(linenumberdict[4], segment)) and not bool(re.search(linenumberdict[1], segment)):
                intwo = segment
                linenumberdict[6] = r"^".join(f"(?=.*{i})" for i in segment)
                segmentdict[6] = len(segment)

        for letter in segment9:
            intwo = intwo.replace(letter, "")

        for segment in line[0].split(" "):
            if len(segment) == 5 and not bool(re.search(linenumberdict[1], segment)):
                if intwo in segment:
                    linenumberdict[2] = r"^".join(f"(?=.*{i})" for i in segment)
                    segmentdict[2] = len(segment)
                else:
                    linenumberdict[5] = r"^".join(f"(?=.*{i})" for i in segment)
                    segmentdict[5] = len(segment)
            elif len(segment) == 5:
                linenumberdict[3] = r"^".join(f"(?=.*{i})" for i in segment)
                segmentdict[3] = len(segment)

        linevalue = ""
        for segment in line[1].split(" "):
            for key, value in segmentdict.items():
                if len(segment) == value and bool(re.search(linenumberdict[key], segment)):
                    linevalue += str(key)

        segmentcount += int(linevalue)

    print(segmentcount)
