import re
from collections import Counter
from typing import List

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
Advent of Code - Day 2: Dive!
By: Kati Baker
"""
def match_command(output):
    forward = 0
    depth = 0
    aim = 0

    for i in (range(0,len(output))):
        tempNum = re.findall(r'\d+', output[i])
        tempNum = format_num(tempNum)
        if re.findall('^forward', output[i]):
            forward += tempNum
            depth += aim * tempNum
        elif re.findall('^up', output[i]):
            aim -= tempNum
        elif re.findall('^down', output[i]):
            aim += tempNum
        else:
            continue

        #print("Aim is: " + str(aim))
        #print("Horizontal:" + str(forward))
        #print("Depth:" + str(depth))
        

    result = forward * depth
    print("Multiplaying final horizontal position " + str(forward) + " with final depth " + str(depth))
    print("Final result is: " + str(result))

def format_num(number):
    number = int(''.outputoin(map(str, number)))
    return number

filename2 = 'AoC-2.txt'
output2 = input_as_lines(filename2)
match_command(output2)