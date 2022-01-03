from typing import List
import re
import numpy as np
from collections import Counter
import time

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
	chitons = []
	for row in lines:
		chiton_row = [int(c) for c in row]
		chitons.append(chiton_row)

	return chitons

#part 1 only - needs to account for moving up and backwards as well, not just to the right and down
#implement Dijkstra!!
def calc_cost(grid, rows, cols):
    cost = [[0 for x in range(rows+1)] for x in range(cols+1)]
    
    #set starting pt to cost pt since it doesn't count in the risk
    cost[0][0] = grid[0][0]

    #init col
    for i in range(1, rows+1):
        cost[i][0] = cost[i-1][0] + grid[i][0]

    #init row
    for j in range(1, cols+1):
        cost[0][j] = cost[0][j-1] + grid[0][j]

    #fill out the rest
    adjacent = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j]
    
    cost[rows][cols] = cost[rows][cols] - grid[rows][cols]

    #print(cost[rows][cols])

    return cost

def inside_grid(i, j, rows, cols):
    if i >= 0 and i <= rows and j >= 0 and j <= cols:
        print("In bounds")
        return True
    else:
        return False

start_time2 = time.time()
f = r'C:\Users\kbaker19\Desktop\AoC-15-Input.txt'
grid = input_as_lines(f)
grid = make_grid(grid)
#print(grid)
#print("-------------------------------------------")

rows = len(grid)-1
cols = len(grid)-1
cost = []
cost = calc_cost(grid, rows, cols)

stop_time2 = time.time()

print(f"Final answer: {cost[rows][cols]}, found in {(stop_time2 - start_time2) * 1000} milliseconds")