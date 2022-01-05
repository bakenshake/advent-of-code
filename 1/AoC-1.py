from typing import List
import re
import numpy as np
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
Advent of Code - Day 1: Sonar Sweep
By: Kati Bkaer
"""
def count_increase(output):
    counter = 0
    for i in range(0,len(output)-1):
        #print(output.count(i))
        if output[i] < output[i+1]:
            #print("increase")
            counter += 1

    print("The total increase amounts are: " + str(counter))

def measure_segments(output):
    segment_counter = 0
    segmentList = []
    for i in range(0,len(output)-1):
        if i != len(output)-2:
            segment = output[i] + output[i+1] + output[i+2]
            segmentList.append(segment)

    count_increase(segmentList)

    
#Day 1 AoC
filename = r'AoC-1.txt'
output = input_as_ints(filename)
count_increase(output)
measure_segments(output)