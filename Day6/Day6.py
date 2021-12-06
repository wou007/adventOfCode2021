import os
import timeit

def part1(input):
    result = 0
    input = list(map(int,input[0].split(',')))

    fish = [0]*9

    for i in input:
        fish[i] += 1

    for i in range(80):
        temp = fish[0]
        for i in range(1,9):
            fish[i-1] = fish[i]
        fish[6] += temp
        fish[8] = temp

    result = sum(fish)
    
    return result

def part2(input):
    result = 0
    input = list(map(int,input[0].split(',')))

    fish = [0]*9

    for i in input:
        fish[i] += 1

    for i in range(256):
        temp = fish[0]
        for i in range(1,9):
            fish[i-1] = fish[i]
        fish[6] += temp
        fish[8] = temp

    result = sum(fish)
    
    return result

if __name__ == "__main__":
    f = open("Day6/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    