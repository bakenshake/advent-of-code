from typing import List
import re
from collections import Counter

"""
Helper functions to reuse for puzzles - thanks Danielle Lucek!
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

def make_grid(lines):
	tubes = []
	for row in lines:
		tube_row = [int(c) for c in row]
		tubes.append(tube_row)

	return tubes

def check_neighbors(x, y, tubes, lowCount):
    #Left: (-1, 0)
    #Right: (0, 1)
    #Top: (0, -1)
    #Down: (1, 0)
    adjacent = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    #stay in bounds
    for offset in adjacent:
        #print(f"Current element is: {tubes[y][x]}")
        ny = y + offset[0]
        nx = x + offset[1]
        if ny in range(0,len(tubes)) and nx in range(0,len(tubes[0])):
            if tubes[y][x] < tubes[ny][nx]:
                print(f"The current point: {tubes[y][x]} is less than {tubes[ny][nx]}")
                lowCount += 1

    return lowCount

def print_low_points(lowPoint):
    for i in range(0,len(lowPoint)):
        print(lowPoint[i])

f = r'C:\Users\kbaker19\Desktop\AoC-9.txt'
tubes = input_as_lines(f)
tubes = make_grid(tubes)
print(len(tubes)) #y value
cols = len(tubes)-1
rows = len(tubes[0])-1
print(tubes)

lowPoints = []
lowCount = 0
for y in range(0,len(tubes)):
    for x in range(0,len(tubes[0])):
        
        lowCount = check_neighbors(x,y,tubes,lowCount)

        if lowCount == 4: #center spaces
            lowPoints.append(tubes[y][x])
            print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
            lowCount = 0
        elif lowCount == 3: #edge cases
            if x == 0 or y == 0:
                print("edge case")
                print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
                lowPoints.append(tubes[y][x])
                lowCount = 0
            elif x == rows or y == cols:
                print("end edge case")
                print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
                lowPoints.append(tubes[y][x])
                lowCount = 0
        elif lowCount == 2: #corner cases
            if y == 0 and x == 0:
                print("top left corner")
                print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
                lowPoints.append(tubes[y][x])
                lowCount = 0
            elif y == 0 and x == rows:
                print("top right corner")
                print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
                lowPoints.append(tubes[y][x])
                lowCount = 0
            elif y == cols and x == 0:
                print("bottom left corner")
                print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
                lowPoints.append(tubes[y][x])
                lowCount = 0
            elif y == cols and x == rows:
                print("bottom right corner")
                print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
                lowPoints.append(tubes[y][x])
                lowCount = 0
        else:
            print(f"Ignore {tubes[y][x]}\n")
        lowCount = 0

print_low_points(lowPoints)

for i in range(0,len(lowPoints)):
    lowPoints[i] += 1

print(sum(lowPoints))