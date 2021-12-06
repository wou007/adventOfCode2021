import os
import timeit

def part1(input):
    result = 0
    # input = list(map(int,input))

    counts = [0] * len(input[0])

    for l in input:
        for i in range(len(l)):
            if(l[i] == '1'):
                counts[i] += 1

    gamma = ''
    epsilon = ''

    for t in counts:
        if t < (len(input) / 2):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    gamma = int(gamma,2)
    epsilon = int(epsilon,2)
    
    return gamma * epsilon

def part2(input):
    result = 0
    
    temp = input
    temp2 = []
    run = 0
    while len(temp) > 1:
        counts = [0] * len(temp[0])
        for l in temp:
            for i in range(len(l)):
                if(l[i] == '1'):
                    counts[i] += 1

        mostValue = '0'
        if counts[run] >= (len(temp) / 2):
            mostValue = '1'

        for l in temp:
            if(l[run] == mostValue):
                temp2.append(l)

        run += 1
        temp = temp2.copy()
        temp2 = []
    
    oxygen = int(temp[0],2)

    temp = input
    temp2 = []
    run = 0
    while len(temp) > 1:
        counts = [0] * len(temp[0])
        for l in temp:
            for i in range(len(l)):
                if(l[i] == '1'):
                    counts[i] += 1

        mostValue = '0'
        if counts[run] < (len(temp) / 2):
            mostValue = '1'

        for l in temp:
            if(l[run] == mostValue):
                temp2.append(l)

        run += 1
        temp = temp2.copy()
        temp2 = []

    co2 = int(temp[0],2)
    
    return oxygen * co2

if __name__ == "__main__":
    f = open("Day3/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    