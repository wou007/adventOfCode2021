import os
import timeit

def part1(input):
    depth = 0
    forward = 0
    
    for i in input:
        a = i.split(' ')
        if a[0] == 'up':
            depth -= int(a[1])
        if a[0] == 'down':
            depth += int(a[1])
        if a[0] == 'forward':
            forward += + int(a[1])
    
    return depth * forward

def part2(input):
    depth = 0
    forward = 0
    aim = 0
    
    for i in input:
        a = i.split(' ')
        if a[0] == 'up':
            aim -= int(a[1])
        if a[0] == 'down':
            aim += int(a[1])
        if a[0] == 'forward':
            forward += int(a[1])
            depth += (aim * int(a[1]))
    
    return depth * forward

if __name__ == "__main__":
    f = open("Day2/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    