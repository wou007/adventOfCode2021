import os
import timeit

def part1(input):
    result = 0
    input = list(map(int,input))

    prev = None
    for i in input:
        if prev != None and prev < i:
            result = result + 1
        prev = i
    
    return result

def part2(input):
    result = 0
    input = list(map(int,input))

    for i in range(3,len(input)):
        if input[i-3] < input[i]:
            result = result + 1
    
    return result

if __name__ == "__main__":
    f = open("Day1/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    