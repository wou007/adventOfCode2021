import os
import timeit

def part1(input):
    result = 0
    
    for line in input:
        parts = line.split('|')
        for letters in parts[1].split(' '):
            if len(letters) == 2:
                result += 1
            if len(letters) == 3:
                result += 1
            if len(letters) == 4:
                result += 1
            if len(letters) == 7:
                result += 1

    return result

def part2(input):
    total = 0
    
    for line in input:
        parts = line.split('|')
        examples = list(filter(None, parts[0].split(' ')))

        results = ['']*10

        for e in examples:
            if len(e) == 2:
                results[1] = e
            if len(e) == 3:
                results[7] = e
            if len(e) == 4:
                results[4] = e
            if len(e) == 7:
                results[8] = e

        examples.remove(results[1])
        examples.remove(results[7])
        examples.remove(results[4])
        examples.remove(results[8])

        # 6
        for e in examples:
            if len(e) == 6:
                equalFrom1 = 0
                for l in results[1]:
                    if l in e:
                        equalFrom1 += 1
                if equalFrom1 == 1:
                    results[6] = e
        examples.remove(results[6])

        # 9
        for e in examples:
            if len(e) == 6:
                equalFrom4 = 0
                for l in results[4]:
                    if l in e:
                        equalFrom4 += 1
                if equalFrom4 == 4:
                    results[9] = e
        examples.remove(results[9])

        # 0
        for e in examples:
            if len(e) == 6:
                results[0] = e
        examples.remove(results[0])

        # 3
        for e in examples:
            if len(e) == 5:
                equalFrom1 = 0
                for l in results[1]:
                    if l in e:
                        equalFrom1 += 1
                if equalFrom1 == 2:
                    results[3] = e
        examples.remove(results[3])

        # 5
        for e in examples:
            if len(e) == 5:
                equalFrom4 = 0
                for l in results[4]:
                    if l in e:
                        equalFrom4 += 1
                if equalFrom4 == 3:
                    results[5] = e
        examples.remove(results[5])

        #2
        results[2] = examples[0]

        text = ''

        for letters in parts[1].split(' '):
            for i in range(10):
                if sorted(letters) == sorted(results[i]):
                    text += str(i)
        total += int(text)

    return total

if __name__ == "__main__":
    f = open("Day8/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    