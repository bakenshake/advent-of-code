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

def age_fish(lanternFish):
    for fish in range(0,len(lanternFish)):
        #decrement all fish each step
        lanternFish[fish] -= 1

    return lanternFish

def breed_fish(lanternFish, newFish):
    for fish in range(0,len(lanternFish)):
        if lanternFish[fish] < 0:
            #add it so it is not reduced
            #create a new on at end of list
            newFish += 1

    return lanternFish, newFish

def add_fish(lanternFish, newFish):
    while newFish != 0:
        lanternFish.append(8)
        newFish -= 1

    return lanternFish

def reset_fish(lanternFish):
    for fish in range(0,len(lanternFish)):
        if lanternFish[fish] < 0:
            lanternFish[fish] = 6
    return lanternFish

#read in input
f = r'AoC-6.txt'
input = input_as_string(f)

#split on the ,
input = input.split(',')

#setup the numbers and convert to ints
lanternFish = []
for num in input:
    lanternFish.append(int(num))

days = 1
newFish = 0
while days != 81:
    lanternFish = age_fish(lanternFish)
    #print(f"After aging: {lanternFish}")

    lanternFish, newFish = breed_fish(lanternFish, newFish)
    #print(f"New fish: {newFish}")

    lanternFish = add_fish(lanternFish, newFish)

    lanternFish = reset_fish(lanternFish)
    #print(f"After reset: {lanternFish}")

    #print("----------------------------------")
    #print(f"After Day: {days} | {lanternFish}")
    #print("----------------------------------\n\n")

    newFish = 0
    days += 1

    #lanternFish = 
print(len(lanternFish))
