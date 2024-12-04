import os
import re

filepath = os.path.abspath("day03/input.txt")
file = open(filepath)


def part1(data):
    sum = 0
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

    for line in data:
        occurrences = re.findall(pattern, line)

        for item in occurrences:
            [num1, num2] = item.replace("mul(", "").replace(")", "").split(",")

            multiplication = int(num1) * int(num2)
            sum += multiplication

    return sum


def part2(data):
    sum = 0
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")

    do = True
    for line in data:
        occurrences = re.findall(pattern, line)

        for item in occurrences:
            if item == "do()":
                do = True
                continue
            elif item == "don't()":
                do = False
                continue
            elif do:
                [num1, num2] = item.replace("mul(", "").replace(")", "").split(",")

                multiplication = int(num1) * int(num2)
                sum += multiplication

    return sum


# print(part1(file))
print(part2(file))
