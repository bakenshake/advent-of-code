"""
Advent of Code - Day 1: Sonar Sweep
Helper functions to reuse for puzzles - thanks Danielle Lucek!
"""
from typing import List

def input_as_string(filename:str) -> str:
    """returns the content of the input file as a string"""
    with open(filename,'r', encoding="utf8") as file_to_open:
        return file_to_open.read().rstrip("\n")
def input_as_lines(filename:str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")
def input_as_ints(filename:str) -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))
def count_increase(output):
    """Increases each item if it's less than the one in front of it"""
    counter = 0
    for i in range(0,len(output)-1):
        if output[i] < output[i+1]:
            counter += 1

    return counter
def measure_segments(segments):
    """Chunks it out"""
    segment_list = []
    for i in range(0,len(segments)-1):
        if i != len(segments)-2:
            segment = segments[i] + segments[i+1] + segments[i+2]
            segment_list.append(segment)

    return count_increase(segment_list)
FILENAME = 'AoC-1.txt'
file_input = input_as_ints(FILENAME)
PARTONE = count_increase(file_input)
PARTTWO = measure_segments(file_input)
print(f"Part 1 answer is: {PARTONE}\nPart 2 answer is: {PARTTWO}")
