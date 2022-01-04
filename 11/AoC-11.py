from typing import List
import re
#import numpy as np
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

"""
Day 11 of Advent of Code
"""
def do_step(octupi):
    steps = 0
    flashes = list()
    while steps != 100:
        flashList = list()

        #increase all the octopus
        increase_energy(octupi)

        #check for flashes
        check_levels(octupi, flashes, flashList)

        steps += 1
        print("Number of flashes: "+str(len(flashes)))

        for fx, fy in flashList:
            octupi[fy][fx] = 0
        # print situation
        print(f'after {steps+1} steps:')

    if (steps >= 100):
        #part1 = f'Part 1: {flashes} Flashes'
        #print(part1)
        print(len(flashes))

def increase_energy(octupi):
    print("Increasing energy...")
    for y in range(len(octupi)):
        for x in range(0,len(octupi[0])):
            #print("Moving from energy level: " + str(octupi[y][x]))
            octupi[y][x] += 1
            #print("To this energy level: " + str(octupi[y][x]))

def check_levels(octupi, flashes, flashList):
    for y in range(0,len(octupi)):
        for x in range(0,len(octupi[0])):
            if octupi[y][x] == 10:
                flashes.append(1)
                flashList.append((x,y))
                #print("Octopus flashing at: " + str(y) + "," + str(x))
                flash(x, y, octupi)

def flash(x, y, octupi):
    adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] 
    for ny, nx in adjacent:
        octupi[ny][nx] += 1 
    octupi[y][x] = 0
    
def print_octupi(octopuses):
    for y in range(len(octopuses)):
        for x in range(len(octopuses[0])):
            print(octopuses[y][x],end='')
        print()
    print()

octupi = []
for d in open(r'AoC-11.txt','r').read().split('\n')[:-1]:
    octupi.append([int(i) for i in list(d)])
print(octupi) 
do_step(octupi)
