import os
import timeit

def part1(input):
    result = 0

    connections = []

    for l in input:
        connections.append(l.split('-'))

    result = walkPaths(connections, ['start'])

    return result

def walkPaths(connections, visitedLocations):
    result = 0
    for c in connections:
        nextPos = None
        if c[0] == visitedLocations[-1]:
            nextPos = c[1]
        elif c[1] == visitedLocations[-1]:
            nextPos = c[0]

        if nextPos != None:
            if nextPos == 'end':
                result += 1
            elif nextPos not in visitedLocations or nextPos.isupper():
                newVisitedLocations = visitedLocations.copy()
                newVisitedLocations.append(nextPos)
                result += walkPaths(connections, newVisitedLocations)
    return result


def part2(input):
    result = 0

    connections = []

    for l in input:
        connections.append(l.split('-'))

    result = walkPaths2(connections, ['start'])

    return result

def walkPaths2(connections, visitedLocations):
    result = 0
    for c in connections:
        nextPos = None
        if c[0] == visitedLocations[-1]:
            nextPos = c[1]
        elif c[1] == visitedLocations[-1]:
            nextPos = c[0]

        if nextPos != None:
            if nextPos == 'end':
                result += 1
            elif allowedToVisitLocation(visitedLocations, nextPos):
                newVisitedLocations = visitedLocations.copy()
                newVisitedLocations.append(nextPos)
                result += walkPaths2(connections, newVisitedLocations)
    return result

def allowedToVisitLocation(visitedLocations, location):
    if location == 'start':
        return False
    if location == 'end':
        raise Exception
    if location.isupper():
        return True
    if location not in visitedLocations:
        return True

    for l in visitedLocations:
        if l.islower():
            if visitedLocations.count(l) > 1:
                return False
    return True

if __name__ == "__main__":
    f = open("Day12/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    