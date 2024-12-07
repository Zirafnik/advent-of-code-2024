import os

filepath = os.path.abspath("day06/input.txt")
file = open(filepath).read().splitlines()


def part1(data):
    spinDirection = {"UP": "RIGHT", "RIGHT": "DOWN", "DOWN": "LEFT", "LEFT": "UP"}

    positions = set()

    [guard, direction] = findGuardAndStartDirection(data)

    prevPosition = None
    currentPosition = guard
    while not isOutOfBounds(currentPosition, data):
        # If obstacle: turn right, retract step, re-do prev loop
        if data[currentPosition[0]][currentPosition[1]] == "#":
            direction = spinDirection[direction]
            currentPosition = prevPosition
        else:
            # Increase position count
            positions.add(currentPosition)

        # Save previous position in case of obstacles
        prevPosition = currentPosition

        # Take step forward
        if direction == "UP":
            currentPosition = (currentPosition[0] - 1, currentPosition[1])
        elif direction == "DOWN":
            currentPosition = (currentPosition[0] + 1, currentPosition[1])
        elif direction == "RIGHT":
            currentPosition = (currentPosition[0], currentPosition[1] + 1)
        elif direction == "LEFT":
            currentPosition = (currentPosition[0], currentPosition[1] - 1)

    return len(positions)  # return count of unique positions (coordinates)


def findGuardAndStartDirection(data):
    directions = {"^": "UP", "v": "DOWN", ">": "RIGHT", "<": "LEFT"}

    for y in range(len(data)):
        for x in range(len(data[y])):
            char = data[y][x]
            if char in {"^", "v", ">", "<"}:
                return ((y, x), directions[char])


def isOutOfBounds(coord, data):
    [y, x] = coord

    # Check if indexes are "Out of bounds"
    if y < 0 or x < 0 or y > len(data) - 1 or x > len(data[y]) - 1:
        return True

    return False


print(part1(file))
