import os
import timeit

def part1(input):
    result = 0
    field = {}

    for l in input:
        parts = l.split(' -> ')
        a = list(map(int,parts[0].split(',')))
        b = list(map(int,parts[1].split(',')))

        if a[0] == b[0]:
            for i in range(min(a[1],b[1]),max(a[1],b[1]) + 1):
                if f"{a[0]},{i}" in field:
                    field[f"{a[0]},{i}"] += 1
                else:
                    field[f"{a[0]},{i}"] = 1

        if a[1] == b[1]:
            for i in range(min(a[0],b[0]),max(a[0],b[0]) + 1):
                if f"{i},{a[1]}" in field:
                    field[f"{i},{a[1]}"] += 1
                else:
                    field[f"{i},{a[1]}"] = 1

    for key in field:
        if field[key] > 1:
            result += 1

    return result

def part2(input):
    result = 0
    field = {}

    for l in input:
        parts = l.split(' -> ')
        a = list(map(int,parts[0].split(',')))
        b = list(map(int,parts[1].split(',')))

        if a[0] == b[0]:
            for i in range(min(a[1],b[1]),max(a[1],b[1]) + 1):
                if f"{a[0]},{i}" in field:
                    field[f"{a[0]},{i}"] += 1
                else:
                    field[f"{a[0]},{i}"] = 1
        elif a[1] == b[1]:
            for i in range(min(a[0],b[0]),max(a[0],b[0]) + 1):
                if f"{i},{a[1]}" in field:
                    field[f"{i},{a[1]}"] += 1
                else:
                    field[f"{i},{a[1]}"] = 1
        else:
            for i in range(abs(a[0]-b[0]) + 1):
                x = 0
                y = 0
                if a[0] < b[0]:
                    x = a[0] + i
                else:
                    x = a[0] - i

                if a[1] < b[1]:
                    y = a[1] + i
                else:
                    y = a[1] - i
                
                if f"{x},{y}" in field:
                    field[f"{x},{y}"] += 1
                else:
                    field[f"{x},{y}"] = 1

    for value in field.values():
        if value > 1:
            result += 1

    return result

if __name__ == "__main__":
    f = open("Day5/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 5

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    