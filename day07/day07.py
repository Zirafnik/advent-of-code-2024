import os
import itertools

filepath = os.path.abspath("day07/input.txt")
file = open(filepath).read().splitlines()


def part1(data):
    total = 0
    for line in data:
        [result, numStr] = line.split(": ")
        numbers = [int(num) for num in numStr.split(" ")]

        possibleOperations = list(
            itertools.product(["*", "+"], repeat=(len(numbers) - 1))
        )

        for operations in possibleOperations:
            newResult = numbers[0]

            for i in range(1, len(numbers)):
                num = numbers[i]
                operation = operations[i - 1]

                if operation == "*":
                    newResult *= num
                else:
                    newResult += num

            if newResult == int(result):
                total += int(result)
                break

    return total


def part2(data):
    total = 0
    # lineNum = 1  # Used only for progress indicator
    # totalLines = 850  # Used only for progress indicator
    for line in data:
        # print(lineNum, totalLines, sep="/") # Used only for progress indicator
        [result, numStr] = line.split(": ")
        numbers = [int(num) for num in numStr.split(" ")]

        possibleOperations = list(
            itertools.product(["*", "+", "||"], repeat=(len(numbers) - 1))
        )

        for operations in possibleOperations:
            newResult = numbers[0]

            for i in range(1, len(numbers)):
                num = numbers[i]
                operation = operations[i - 1]

                if operation == "||":
                    newResult = int(str(newResult) + str(num))
                elif operation == "*":
                    newResult *= num
                else:
                    newResult += num

            if newResult == int(result):
                total += int(result)
                break
        # lineNum += 1 # Used only for progress indicator

    return total


print(part1(file))
print(part2(file))
