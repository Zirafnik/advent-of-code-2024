import os

filepath = os.path.abspath("day01/input.txt")
file = open(filepath)
data = file.read().splitlines()

def part1(data):
    # Split into two lists
    list1 = []
    list2 = []
    for line in data:
        [num1, num2] = line.split()

        list1.append(int(num1))
        list2.append(int(num2))

    # Sort each list
    list1.sort()
    list2.sort()

    # Get distance for each item & add them to sum
    sum = 0
    for i in range(len(list1)):
        distance = abs(list1[i] - list2[i])
        sum += distance
    
    return sum

def part2(data):
    # Create a frequency dict for right nums + list for left nums
    listL = []
    dictR = {}
    for line in data:
        [num1, num2] = line.split()
        listL.append(int(num1))
        dictR[int(num2)] = dictR.get(int(num2), 0) + 1
    
    # Loop over left list & calculate similarity score based on right freqs
    total = 0
    for num in listL:
        similarityScore = num * dictR.get(num, 0)
        total += similarityScore

    return total


print(part1(data))
print(part2(data))