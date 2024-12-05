import os

filepath = os.path.abspath("day05/input.txt")
file = open(filepath).read().splitlines()


def part1(data):
    sumMedians = 0
    [rules, lineIndex] = parseRules(data)

    for i in range(lineIndex + 1, len(data)):
        line = data[i]

        pages = line.split(",")

        incorrect = False
        for j in range(len(pages)):
            page = pages[j]
            for k in range(j + 1, len(pages)):
                afterPage = pages[k]
                if afterPage in rules.get(page, {}):
                    continue
                else:
                    incorrect = True
                    break

            # Completely skip rest of pages if line is wrong
            if incorrect:
                break

        if not incorrect:
            sumMedians += getMedian(pages)

    return sumMedians


def parseRules(data):
    rules = {}

    for i in range(len(data)):
        line = data[i]
        if line == "":
            return (rules, i)

        [num1, num2] = line.split("|")

        rules.setdefault(num1, set()).add(num2)


def getMedian(list):
    medianIdx = len(list) // 2

    return int(list[medianIdx])


print(part1(file))
