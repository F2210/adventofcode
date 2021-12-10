from collections import deque

pointdict = {")": 3, "]": 57, "}": 1197, ">": 25137}
pointdict2 = {")": 1, "]": 2, "}": 3, ">": 4}
matchdict = {"(": ")", "[": "]", "{": "}", "<": ">"}
charset = ["()", "[]", "{}", "<>"]

def removeset(newline):

    for set in charset:
        newline = newline.replace(set, "")

    for set in charset:
        if set in newline:
            newline = removeset(newline)

    return newline

with open('input/10.txt', 'r') as file:

    lines = file.readlines()
    newline = ""
    goodlines = []

    score = 0
    for lineid in range(len(lines)):
        line = lines[lineid]
        notfound = True
        result = removeset(line)
        for char in result:
            if char in pointdict.keys() and notfound:
                score += pointdict[char]
                notfound = False

        if notfound:
            goodlines.append(result.strip())

    print(score)

    scores = []
    for line in goodlines[-1:]:
        score = 0
        for char in line[::-1]:
            score *= 5
            score += pointdict2[matchdict[char]]
        scores.append(score)

    print(sorted(scores)[len(scores) // 2])

