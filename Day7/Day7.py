import os
import timeit

def part1(input):
    result = 99999999999999999
    input = list(map(int,input[0].split(',')))

    for i in range(min(input),max(input)):
        fuel = 0
        for c in input:
            fuel += abs(c-i)
        result = min(fuel,result)
    
    return result

def part2(input):
    result = 99999999999999999
    input = list(map(int,input[0].split(',')))

    for i in range(min(input),max(input)):
        fuel = 0
        for c in input:
            fuel += sum(range(1,abs(c-i)+1))
        result = min(fuel,result)
    
    return result

if __name__ == "__main__":
    f = open("Day7/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    