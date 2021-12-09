import os
import timeit

def part1(input):
    result = 0
    
    heightMap = []

    for l in input:
        heightMap.append(list(map(int,l)))

    for y in range(len(heightMap)):
        for x in range(len(heightMap[0])):
            smallest = True
            for i in range(-1,2):
                for j in range(-1,2):
                    try:
                        if y+i >= 0 and x+j >= 0 and i != 0 or j != 0:
                            if heightMap[y+i][x+j] <= heightMap[y][x]:
                                smallest = False
                    except IndexError:
                        # Does not excist
                        pass
            if smallest:
                result += 1 + heightMap[y][x]

    return result

def part2(input):
    result = 0
    
    heightMap = []
    lowPoints = []

    for l in input:
        heightMap.append(list(map(int,l)))

    for y in range(len(heightMap)):
        for x in range(len(heightMap[0])):
            smallest = True
            for i in range(-1,2):
                for j in range(-1,2):
                    try:
                        if y+i >= 0 and x+j >= 0 and i != 0 or j != 0:
                            if heightMap[y+i][x+j] <= heightMap[y][x]:
                                smallest = False
                    except IndexError:
                        # Does not excist
                        pass
            if smallest:
                lowPoints.append((y,x))

    basinNumber = 100

    for l in lowPoints:
        todo = [l]
        while len(todo) > 0:
            point = todo.pop()
            heightMap[point[0]][point[1]] = basinNumber

            if point[0]+1 < len(heightMap) and heightMap[point[0]+1][point[1]] < 9:
                todo.append((point[0]+1,point[1]))

            if point[0]-1 >= 0 and heightMap[point[0]-1][point[1]] < 9:
                todo.append((point[0]-1,point[1]))

            if point[1]+1 < len(heightMap[point[0]]) and heightMap[point[0]][point[1]+1] < 9:
                todo.append((point[0],point[1]+1))
                
            if point[1]-1 >= 0 and heightMap[point[0]][point[1]-1] < 9:
                todo.append((point[0],point[1]-1))
        
        basinNumber += 1

    basinSizes = []
    for i in range(100, basinNumber):
        basinSizes.append(sum(x.count(i) for x in heightMap))

    basinSizes = sorted(basinSizes)

    return basinSizes[-1] * basinSizes[-2] * basinSizes[-3]

if __name__ == "__main__":
    f = open("Day9/input.txt","r")
    input = f.read().split("\n")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

    runs = 1

    t1 = timeit.timeit(lambda: part1(input), number=runs)
    t2 = timeit.timeit(lambda: part2(input), number=runs)

    print(f"\nRuntime Part 1 {t1/runs}s, Part 2 {t2/runs}s")
    