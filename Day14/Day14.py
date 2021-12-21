import os
import timeit

def part1(input):
    result = 0
    inserts = {}

    polymer = input[0]

    for l in input[2:]:
        parts = l.split(' -> ')
        inserts[parts[0]] = parts[1]

    for x in range(10):
        newPolymer = ''
        for i in range(len(polymer)-1):
            newPolymer += polymer[i]
            newPolymer += inserts[polymer[i]+polymer[i+1]]
        newPolymer += polymer[-1]
        polymer = newPolymer
    
    ma = 0
    mi = 99999999999999999

    for l in inserts.values():
        ma = max(polymer.count(l),ma)
        mi = min(polymer.count(l),mi)

    result = ma - mi

    return result

def part2(input):
    result = 0
    inserts = {}
    pairCounts = {}
    polymer = input[0]

    for l in input[2:]:
        parts = l.split(' -> ')
        inserts[parts[0]] = parts[1]
        pairCounts[parts[0]] = 0

    
    for a,b in zip(polymer,polymer[1:]):
        pairCounts[f"{a}{b}"] += 1

    for x in range(40):
        tempPairCounts = {}
        for i in inserts:
            tempPairCounts[i] = 0
        for p in pairCounts:
            count = pairCounts[p]
            if count > 0:
                extraLetter = inserts[p]
                tempPairCounts[f"{p[0]}{extraLetter}"] += count
                tempPairCounts[f"{extraLetter}{p[1]}"] += count
        pairCounts = tempPairCounts

    
    ma = 0
    mi = 99999999999999999

    letterCount = {}
    for l in inserts.values():
        letterCount[l] = 0

    for p in pairCounts:
        letterCount[p[0]] += pairCounts[p]

    letterCount[polymer[-1]] += 1

    for l in letterCount.values():
        ma = max(l,ma)
        mi = min(l,mi)

    result = ma - mi

    return result

if __name__ == "__main__":
    f = open("Day14/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    