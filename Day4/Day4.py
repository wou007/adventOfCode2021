import os
import timeit

def part1(input):
    result = 0
    draws = input[0].split(',')
    draws = list(map(int,draws))

    card = []
    cards = []
    for line in input[2:]:
        if len(line) > 0:
            line = line.split(' ')
            line = filter(None, line)
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
                    for b in a:
                        if(b != 1337):
                            result += b
        if result != 0:
            result *= d
            break
    
    return result

def part2(input):
    result = 0
    draws = input[0].split(',')
    draws = list(map(int,draws))

    card = []
    cards = []
    for line in input[2:]:
        if len(line) > 0:
            line = line.split(' ')
            line = filter(None, line)
            card.append(list(map(int,line)))
        else:
            cards.append(card.copy())
            card = []
    cards.append(card.copy())

    for d in draws:
        countLeftOver = 0
        countFinished = 0
        result = 0
        for c in cards:
            if not checkHorizontal(c) and not checkVertical(c):
                performDraw(c,d)
                if checkHorizontal(c) or checkVertical(c):
                    countFinished += 1
                    if countFinished == 1:
                        for a in c:
                            for b in a:
                                if b != 1337:
                                    result += b
                else:
                    countLeftOver += 1
                
        if countLeftOver == 0:
            result *= d
            break
    
    return result

def checkHorizontal(card):
    result = False
    for x in card:
        complete = True
        for y in x:
            if y != 1337:
                complete = False
        if complete:
            result = complete
    
    return result

def checkVertical(card):
    result = False
    for i in range(len(card[0])):
        complete = True
        for x in card:
            if x[i] != 1337:
                complete = False
        if complete:
            result = complete
    
    return result

def performDraw(card, draw):
    for x in card:
        for i, n in enumerate(x):
            if(n == draw):
                x[i] = 1337

if __name__ == "__main__":
    f = open("Day4/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    