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
Day 3 of Advent of Code
"""
def gamma_rate(output):
    gammaRate = []
    epsilonRate = []

    grc1 = []
    grc2 = []
    grc3 = []
    grc4 = []
    grc5 = []
    grc6 = []
    grc7 = []
    grc8 = []
    grc9 = []
    grc10 = []
    grc11 = []
    grc12 = []

    allLines = []

    for i in (range(0,len(output))):
        print(output[i])
        result = list(output[i])
        #print("---------------")
        #print(result)
        allLines.append(result)

        for j in (range(0,len(result))):
            #print(result[j])
            if j == 0:
                grc1.append(result[j])
            if j == 1:
                grc2.append(result[j])
            if j == 2:
                grc3.append(result[j])
            if j == 3:
                grc4.append(result[j])
            if j == 4:
                grc5.append(result[j])
            if j == 5:
                grc6.append(result[j])
            if j == 6:
                grc7.append(result[j])
            if j == 7:
                grc8.append(result[j])
            if j == 8:
                grc9.append(result[j])
            if j == 9:
                grc10.append(result[j])
            if j == 10:
                grc11.append(result[j])
            if j == 11:
                grc12.append(result[j])

    count_array(grc1, gammaRate, epsilonRate)
    count_array(grc2, gammaRate, epsilonRate)
    count_array(grc3, gammaRate, epsilonRate)
    count_array(grc4, gammaRate, epsilonRate)
    count_array(grc5, gammaRate, epsilonRate)
    count_array(grc6, gammaRate, epsilonRate)
    count_array(grc7, gammaRate, epsilonRate)
    count_array(grc8, gammaRate, epsilonRate)
    count_array(grc9, gammaRate, epsilonRate)
    count_array(grc10, gammaRate, epsilonRate)
    count_array(grc11, gammaRate, epsilonRate)
    count_array(grc12, gammaRate, epsilonRate)

    print("Gamma Rate is: " + str(gammaRate))
    print("Epsilon Rate is: " + str(epsilonRate))

    stringGammaRate = ''.join(map(str, gammaRate))
    stringEpsilonRate = ''.join(map(str, epsilonRate))

    print("Binary Gamma Rate is: " + str(stringGammaRate))
    print("Binary Epsilon Rate is: " + str(stringEpsilonRate))

    stringGammaRate = int(stringGammaRate,2)
    stringEpsilonRate = int(stringEpsilonRate,2)

    print("Decimal Gamma Rate is: " + str(stringGammaRate))
    print("Decimal Epsilon Rate is: " + str(stringEpsilonRate))

    powerConsumption = stringGammaRate * stringEpsilonRate
    print("Power Consumption: " + str(powerConsumption))

    #-----------PART 2-----------#

    parsedLines = []
    clean_input(allLines, parsedLines)

    bitTracker = 0
    reading = parsedLines.copy()
    numToCheck = '1'
    print("\nFILTERING OXYGEN")
    oxygenRating = filter(gammaRate, bitTracker, reading, numToCheck)
    numToCheck = '0'
    reading = parsedLines.copy()
    print("\nFILTERING CARBON")
    carbonRating = filter(epsilonRate, bitTracker, reading, numToCheck)

    print(f"Binary --- Oxygen is: {oxygenRating}, Carbon is: {carbonRating}")

def filter(rateToCheck, bitTracker, reading, numToCheck):
    while bitTracker != len(rateToCheck):
        if len(reading) == 1:
            return reading

        currPosition = rateToCheck[bitTracker]
        print("POSITION IS: " + str(bitTracker))

        ones = 0
        zeroes = 0

        for k in (range(0,len(reading))):
            if k <= len(reading):
                entry = reading[k]
                for l in entry[bitTracker]:
                    if l == '0':
                        zeroes += 1
                    elif l == '1':
                        ones += 1

        #tracking most count
        if zeroes > ones and numToCheck == '1':
            numToKeep = '0'
        elif ones > zeroes and numToCheck == '1':
            numToKeep = '1'
        elif zeroes == ones and numToCheck == '1':
            numToKeep = '1'
        
        #tracking least count
        if zeroes > ones and numToCheck == '0':
            numToKeep = '1'
        elif ones > zeroes and numToCheck == '0':
            numToKeep = '0'
        elif zeroes == ones and numToCheck == '0':
            numToKeep = '0'

        print(f"Num to keep is: {numToKeep}")

        for m in range(0,len(reading)):
            if m < len(reading):
                if len(reading) == 1:
                    return

                entry = reading[m]

                if zeroes != ones:
                    reading = clear_nums(numToKeep, numToCheck, reading, bitTracker)
                elif numToCheck == '1' and zeroes == ones:
                    print("keep the one")
                    reading = clear_nums(numToKeep, numToCheck, reading, bitTracker)
                elif numToCheck == '0' and zeroes == ones:
                    print("keep the zero")
                    reading = clear_nums(numToKeep, numToCheck, reading, bitTracker)

        print("Remaining set is: ")
        for index in range(0,len(reading)):
            print(reading[index])

        bitTracker += 1

    print(reading)
    return reading

def clear_nums(numToKeep, numToCheck, reading, bitTracker):
    remove = []
    for i in range(0,len(reading)):
        entry = reading[i]
        #print(f'Reviewing entry: {entry}')
        if entry[bitTracker] != numToKeep:
            remove.append(entry)

    for x in remove:
        print(f"Removing: {x}")
        reading.remove(x)
    
    return reading

def count_array(grc, gammaRate, epsilonRate):
    zeroCounter = 0
    oneCounter = 0

    for i in (range(0,len(grc))):
        if grc[i] == '0':
            zeroCounter += 1
        if grc[i] == '1':
            oneCounter += 1

    if zeroCounter > oneCounter:
        gammaRate.append(0)
        epsilonRate.append(1)
    else:
        gammaRate.append(1)
        epsilonRate.append(0)

def clean_input(allLines, parsedLines):
    for i in (range(0,len(allLines))):
        element = str(list(map(int, re.findall(r'\d+', str(allLines[i])))))
        element = element.replace(',','')
        element = element.replace(' ','')
        element = element.replace('[','')
        element = element.replace(']','')
        parsedLines.append(element)

#Day 3 AoC
filename3 = 'AoC-3.txt'
output3 = input_as_lines(filename3)
gamma_rate(output3)