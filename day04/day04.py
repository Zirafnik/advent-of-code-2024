import os

filepath = os.path.abspath("day04/input.txt")
file = open(filepath)
puzzle = file.read().splitlines()


def part1(data):
    count = 0
    word = "XMAS"

    coordVectorFactors = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for i in range(len(data)):
        line = data[i]

        for j in range(len(line)):
            char = line[j]

            # Find 'X'
            if char != word[0]:
                continue

            # Check all vectors around it for necessary next characters
            for vectorFactors in coordVectorFactors:
                [f1, f2] = vectorFactors

                # Check the path along this vector (as long as characters match)
                for k in range(1, len(word)):
                    [y, x] = [i + f1 * k, j + f2 * k]

                    # Check if new indexes are "Out of bounds"
                    if y < 0 or x < 0 or y > len(data) - 1 or x > len(line) - 1:
                        break

                    newChar = data[y][x]

                    # Check if characters match, else break out
                    if newChar == word[k]:
                        # If last character, add to total count
                        if newChar == word[-1]:
                            count += 1
                    else:
                        break

    return count


def part2(data):
    count = 0
    diagonalCoordinates = [
        ((-1, -1), (1, 1)),
        ((1, -1), (-1, 1)),
    ]
    opposites = {"S": "M", "M": "S"}

    for i in range(len(data)):
        line = data[i]

        for j in range(len(line)):
            char = line[j]

            # Find 'A'
            if char != "A":
                continue

            # Check both diagonals
            for k in range(2):
                diagonal = diagonalCoordinates[k]
                [coord1, coord2] = diagonal

                # First Coordinate
                [y, x] = [i + coord1[0], j + coord1[1]]

                # Check if new indexes are "Out of bounds"
                if y < 0 or x < 0 or y > len(data) - 1 or x > len(line) - 1:
                    break

                firstChar = data[y][x]

                if firstChar not in {"S", "M"}:  # set has O(1) lookup
                    break

                # Second coordinate
                [y, x] = [i + coord2[0], j + coord2[1]]

                # Check if new indexes are "Out of bounds"
                if y < 0 or x < 0 or y > len(data) - 1 or x > len(line) - 1:
                    break

                secondChar = data[y][x]

                # If second character is not the opposite of first, break out
                if secondChar == opposites[firstChar]:
                    if k == 1:
                        count += 1
                else:
                    break

    return count


print(part1(puzzle))  # 2613
print(part2(puzzle))  # 1905
