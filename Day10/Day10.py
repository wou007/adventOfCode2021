import os
import timeit
import math

openingBrackets = ['(','[','{','<']
closingBrackets = [')',']','}','>']
inverts = [('(',')',3),('[',']',57),('{','}',1197),('<','>',25137)]
scoring = [('(',1),('[',2),('{',3),('<',4)]

def part1(input):
    result = 0
    
    for l in input:
        latestOpening = []
        found = False
        for b in l:
            if b in openingBrackets:
                latestOpening.append(b)
            if b in closingBrackets:
                for i in inverts:
                    if i[1] == b:
                        if i[0] == latestOpening[-1]:
                            latestOpening.pop()
                        else:
                            found = True
                            result += i[2]
                            break
                    if found:
                        break
            if found:
                break

    return result

def part2(input):
    result = 0
    
    scores = []

    for l in input:
        latestOpening = []
        found = False
        for b in l:
            if b in openingBrackets:
                latestOpening.append(b)
            if b in closingBrackets:
                for i in inverts:
                    if i[1] == b:
                        if i[0] == latestOpening[-1]:
                            latestOpening.pop()
                        else:
                            found = True
                            break
        if not found and len(latestOpening) > 0:
            score = 0
            latestOpening.reverse()
            for r in latestOpening:
                for s in scoring:
                    if r == s[0]:
                        score *= 5
                        score += s[1]
            scores.append(score)

    scores.sort()

    result = scores[math.floor(len(scores)/2)]

    return result

if __name__ == "__main__":
    f = open("Day10/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    