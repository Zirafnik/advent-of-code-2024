import os

filepath = os.path.abspath("day02/input.txt")
file = open(filepath)


def part1(data):
    safeReportsCount = 0

    for report in data:
        [isSafe, _] = checkReportSafety(report)

        if isSafe:
            safeReportsCount += 1

    return safeReportsCount


def part2(data):
    safeReportsCount = 0

    for report in data:
        [isSafe, problematicIndex] = checkReportSafety(report)

        if isSafe:
            safeReportsCount += 1
        else:
            # Check safety by removing i, i-1, i-2
            for index in [problematicIndex, problematicIndex - 1, problematicIndex - 2]:
                [isSafeWithout, _] = checkReportSafety(report, index)

                if isSafeWithout:
                    safeReportsCount += 1
                    break

    return safeReportsCount


def checkReportSafety(report, idxToIgnore=None):
    if idxToIgnore is not None and idxToIgnore < 0:
        return (False, None)

    isIncreasing = None
    prevLvl = None

    levels = report.split()

    for i in range(len(levels)):
        if i == idxToIgnore:
            continue

        level = levels[i]

        # First level
        if prevLvl is None:
            prevLvl = int(level)
            continue

        diff = prevLvl - int(level)

        # Difference min = 1 and max = 3
        if abs(diff) < 1 or abs(diff) > 3:
            # Return problematic index
            return (False, i)

        # Second level
        if isIncreasing is None:
            if diff < 0:
                isIncreasing = True
            else:
                isIncreasing = False

        # After levels (if decreasing, when previously increasing)
        if diff > 0 and isIncreasing:
            # Return problematic index
            return (False, i)

        # (if increasing, when previously decreasing)
        elif diff < 0 and not isIncreasing:
            # Return problematic index
            return (False, i)

        prevLvl = int(level)

    return (True, None)


# print(part1(file))
print(part2(file))  # Test: 7 (added custom test cases)
