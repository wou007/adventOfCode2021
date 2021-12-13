import os
import timeit

def part1(input):
    result = 0

    points = []
    folds = []
    maxX = 0
    maxY = 0

    for l in input:
        if 'fold along' in l:
            fold = l.split('=')
            folds.append((fold[0][-1],int(fold[1])))
        elif len(l) > 1:
            point = list(map(int,l.split(',')))
            points.append(point)
            maxX = max(maxX,point[0])
            maxY = max(maxY,point[1])

    paper = []

    for i in range(maxY+1):
        paper.append([0]*(maxX + 1))

    for p in points:
        paper[p[1]][p[0]] = 1

    if folds[0][0] == 'y':
        paper = foldY(paper,folds[0][1])
    else:
        paper = foldX(paper,folds[0][1])

    for a in paper:
        for b in a:
            if b > 0:
                result += 1

    return result

def foldY(paper,index):
    newPaper = []
    for i in range(index, 0, -1):
        line = []
        if len(paper) > index + i and index-i >= 0:
            for a,b in zip(paper[index+i],paper[index-i]):
                line.append(a + b)
        elif len(paper) > index + i:
            line = paper[index+i].copy()
        elif index-i >= 0:
            line = paper[index-i].copy()
        newPaper.append(line)
    return newPaper

def foldX(paper,index):
    newPaper = []
    for a in paper:
        line = []
        for i in range(index, 0, -1):
            if len(a) > index + i and index-i >= 0:
                line.append(a[index + i] + a[index - i])
            elif len(a) > index + i:
                line.append(a[index+i])
            elif index-i >= 0:
                line.append(a[index-i])
        newPaper.append(line)
    return newPaper

def part2(input):
    result = 0

    points = []
    folds = []
    maxX = 0
    maxY = 0

    for l in input:
        if 'fold along' in l:
            fold = l.split('=')
            folds.append((fold[0][-1],int(fold[1])))
        elif len(l) > 1:
            point = list(map(int,l.split(',')))
            points.append(point)
            maxX = max(maxX,point[0])
            maxY = max(maxY,point[1])

    paper = []

    for i in range(maxY+1):
        paper.append([0]*(maxX + 1))

    for p in points:
        paper[p[1]][p[0]] = 1

    for f in folds:
        if f[0] == 'y':
            paper = foldY(paper.copy(),f[1])
        else:
            paper = foldX(paper.copy(),f[1])

    for a in paper:
        line = ''
        for b in a:
            if b > 0:
                line+='#'
            else:
                line+=' '
        print(line)

    return 'UFRZKAUZ'

if __name__ == "__main__":
    f = open("Day13/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    