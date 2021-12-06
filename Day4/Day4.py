import os
import timeit

def part1(input):
    result = 0
    draws = list(map(int,input[0].split(',')))

    card = []
    cards = []
    for line in input[2:]:
        if len(line) > 0:
            line = filter(None, line.split(' '))
            card.append(list(map(int,line)))
        else:
            cards.append(card.copy())
            card = []
    cards.append(card.copy())

    for d in draws:
        for c in cards:
            performDraw(c,d)
            if checkHorizontal(c) or checkVertical(c):
                for a in c:
                    result += sum(a)
        
        if result != 0:
            result %= 1337
            result *= d
            break
    
    return result

def part2(input):
    result = 0
    draws = list(map(int,input[0].split(',')))

    card = []
    cards = []
    for line in input[2:]:
        if len(line) > 0:
            line = filter(None, line.split(' '))
            card.append(list(map(int,line)))
        else:
            cards.append(card.copy())
            card = []
    cards.append(card.copy())

    for d in draws:
        countLeftOver = 0
        result = 0
        for c in cards:
            if not checkHorizontal(c) and not checkVertical(c):
                performDraw(c,d)
                if countLeftOver == 0 and (checkHorizontal(c) or checkVertical(c)):
                    if result == 0:
                        for a in c:
                            result += sum(a)
                else:
                    countLeftOver += 1
                
        if countLeftOver == 0:
            result %= 1337
            result *= d
            break
    
    return result

def checkHorizontal(card):
    result = False
    for x in card:
        if x.count(1337) == len(x):
            result = True
    
    return result

def checkVertical(card):
    result = False
    for i in range(len(card[0])):
        complete = True
        for x in card:
            if x[i] != 1337:
                complete = False
                break
        if complete:
            result = complete
            break
    
    return result

def performDraw(card, draw):
    for x in card:
        if draw in x:
            x[x.index(draw)] = 1337
            break

if __name__ == "__main__":
    f = open("Day4/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    