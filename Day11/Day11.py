import os
import timeit

def part1(input):
    result = 0

    octopuses = []

    for l in input:
        row = []
        for o in l:
            row.append(int(o))
        octopuses.append(row)

    for i in range(100):
        for r in range(len(octopuses)):
                for o in range(len(octopuses[r])):
                    octopuses[r][o] += 1
        
        doagain = True
        while(doagain):
            doagain = False
            for r in range(len(octopuses)):
                for o in range(len(octopuses[r])):
                    if octopuses[r][o] > 9:
                        octopuses[r][o] = -1000
                        for i in range(-1,2):
                            for j in range(-1,2):
                                if r+i >= 0 and o+j >= 0 and r+i < len(octopuses) and o+j < len(octopuses[r]):
                                    octopuses[r+i][o+j] += 1
                                    if octopuses[r+i][o+j] > 9:
                                        doagain = True


        for r in range(len(octopuses)):
            for o in range(len(octopuses[r])):
                if octopuses[r][o] < 0:
                    octopuses[r][o] = 0
                    result += 1

    return result

def part2(input):
    result = 0

    octopuses = []

    for l in input:
        row = []
        for o in l:
            row.append(int(o))
        octopuses.append(row)

    while True:
        result += 1
        for r in range(len(octopuses)):
                for o in range(len(octopuses[r])):
                    octopuses[r][o] += 1
        
        doagain = True
        while(doagain):
            doagain = False
            for r in range(len(octopuses)):
                for o in range(len(octopuses[r])):
                    if octopuses[r][o] > 9:
                        octopuses[r][o] = -1000
                        for i in range(-1,2):
                            for j in range(-1,2):
                                if r+i >= 0 and o+j >= 0 and r+i < len(octopuses) and o+j < len(octopuses[r]):
                                    octopuses[r+i][o+j] += 1
                                    if octopuses[r+i][o+j] > 9:
                                        doagain = True

        count = 0
        for r in range(len(octopuses)):
            for o in range(len(octopuses[r])):
                if octopuses[r][o] < 0:
                    octopuses[r][o] = 0
                    count += 1
        if count == 100:
            break

    return result

if __name__ == "__main__":
    f = open("Day11/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    