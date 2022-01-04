from typing import List
import re

"""
Day 5 - Advent of Code: Hydrothermal Venture
"""

def input_as_string(filename:str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")

def input_as_lines(filename:str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")

def input_as_ints(filename:str) -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))

def make_grid():
    gridLine = []
    grid = []

    for i in range(10):
        gridLine.append(0)
    
    for i in range(10):
        grid.append(list(gridLine))

    return grid

def print_grid(vents):
    for row in vents:  
        print(f"{row}\n")

def mark(x, y, diff, moveType, diagonal, toMark):
    if moveType == True: #vertical
        if y[1] > x[1]:
            iteratorStart = x[1]
            iteratorEnd = y[1]
        else:
            iteratorStart = y[1]
            iteratorEnd = x[1]
        
        for point in range(iteratorStart,iteratorEnd+1):
            toMark.append((x[0],point))
    elif moveType == False and diagonal == False:
        if y[0] > x[0]:
            iteratorStart = x[0]
            iteratorEnd = y[0]
        else:
            iteratorStart = y[0]
            iteratorEnd = x[0]
        
        for point in range(iteratorStart,iteratorEnd+1):
            toMark.append((point,y[1]))
    elif moveType == False and diagonal == True:
        print("figure it out")
        #top left - 
        #top right - 
        #bottom left - 
        #bottom right -

    return toMark

def find_points(vents):
    odd = []
    even = []

    for i in range (0,len(lines)):
        if i % 2 == 0:
            even.append(lines[i])
        else:
            odd.append(lines[i])

    print("----Z--I--P--P--I--N--G----")

    verticalMove = False
    diagonal = False
    for x,y, in zip(even, odd):
        print(f"1: {x} | {x[0]},{x[1]}")
        print(f"2: {y} | {y[0]},{y[1]}")
        x1 = x[0]
        x2 = x[1]

        y1 = y[0]
        y2 = y[1]

        #compare elements
        toMark = []
        #vertical check, X is the same
        if x[0] == y[0]:
            print("vertical move")
            verticalMove = True
            diff = abs(x[1]-y[1])
            toMark = mark(x, y, diff, verticalMove, diagonal, toMark)
            mark_points(toMark, vents)
        elif x[1] == y[1]:
            print("horizontal move")
            verticalMove = False
            diff = abs(x[0]-y[0])
            toMark = mark(x, y, diff, verticalMove, diagonal, toMark)
            mark_points(toMark, vents)
            #pass boolean flag to tell mark function if it's a horizontal or vertical move
        else:
            print("diagonal move")
            verticalMove = False
            diagonal = True
            toMark = mark(x, y, diff, verticalMove, diagonal, toMark)

        verticalMove = False
        diagonal = False

    return vents

def mark_points(toMark, vents):
    for x,y in toMark:
        vents[y][x] += 1
    
    return vents

def count_lines(vents):
    total = 0
    for i in range(0,len(vents)):
        for j in range(0,len(vents)):
            if vents[i][j] >= 2:
                total += 1

    return total

my_string = input_as_string(r'AoC-5.txt')
coords = re.findall(r'-?\d+\,?\d*', my_string)
vents = make_grid()

lines = []
for num in range(0,len(coords)):
    coords[num] = coords[num].split(',')
    lines.append([int(i) for i in list(coords[num])])

vents = find_points(vents)
totalLineOverlap = count_lines(vents)
print_grid(vents)
print(totalLineOverlap)
