from typing import List
import re
from collections import Counter

"""
Day 4 - Advent of Code
By: Kati Baker
"""

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

def set_boards(output):
    #starting marker set 0-5
    markerPos = 5
    #pull out marked numbers
    markedNumbers = output[0]
    markedNumbers = markedNumbers.split(',')
    #print(markedNumbers)

    markers = markedNumbers[0:markerPos]
    #print(markers)

    #find number of boards based on line spaces
    numBoards = get_num_boards(output)
    print("Number of boards are: " + str(numBoards))

    #remove the marked numbers entry
    output.remove(output[0])

    #create a list for the boards 
    allBoards = []

    #strip the empties because 
    for c in output:
        if c == '':
            output.remove(c)
    #print(output)

    #craaaaazy stuff
    element = []
    for line in output: #go line by line
        #print(line)
        words = line.split(' ')
        #print(words)
        for strip in words: #strip the elements '' out
            if strip != '':
                words = strip.split(' ')
                words = strip.lstrip()
                #print(words) #EACH ELEMENT - HUZZAH
                #if str(words) in markers:   
                #    element.append('X')
                #if str(words) not in markers:
                element.append(words)            

    #for e in element:
        #print(e)

    #splice these elements into the boards
    board = []
    start = 0
    boardLength = 25
    boardCount = 0
    while boardCount != numBoards:
        board = element[start:boardLength]
        allBoards.append(board)
        start += 25
        boardLength += 25
        boardCount += 1

    #print(allBoards)
    #print("List of numbers: "+str(len(element)))
    
    #part 2 - make a list of boards to remove
    boardList = []
    winningList = []
    for count in (range(0,len(allBoards))):
        boardList.append(count)
        winningList.append(count)
    
    print(boardList)
    #check win conditions
    numBoardsRemoved = 0
    win = False
    while win != True:

        #mark boards again
        markerPos += 1
        markers = markedNumbers[0:markerPos]
        #print(markers)
        #mark ALL the boards
        mark_numbers(allBoards, markers)

        for checking in (range(0,len(winningList))):
            checking = winningList[checking]
            if checking in boardList:
                win = check_win_conditions(allBoards, boardList, checking)
                if win == True:
                    print("Number of Boards Removed: " + str(numBoardsRemoved))
                    if len(boardList) == 1:
                        win = True
                        break
                    else:
                        remove_board_number(boardList, checking, winningList)
                        print(allBoards[checking])
                        numBoardsRemoved += 1
                    win = False

        #print("Win state after checking conditions: " + str(win))

        if win == True and len(boardList) == 1:
            sum_unmarked_numbers(allBoards[boardList[0]], markers[-1])
            print("The last board is: " + str(boardList[0]))
            #print(boardList[0])
            print("Last marker: " + str(markers[-1]))
            print(allBoards[boardList[0]])
            print("--------------------------------------------------------------------------")
            print(markers)
            break
        
    win = False
    #print("Win state after loop: " + str(win))

def mark_numbers(allBoards, markers):
    boardCount = 0
    while boardCount != len(allBoards):
        element = allBoards[boardCount]
        for i in range(0,len(element)):
            if element[i] in markers:
                element[i] = 'X'
        boardCount += 1
    return element

def sum_unmarked_numbers(winningBoard, marker):
    intList = []
    for index in range(0,len(winningBoard)):
        #print(winningBoard[index])
        if winningBoard[index] != 'X':
            intList.append(int(winningBoard[index]))
            #print(intList)

    print("Sum is: ")
    print(sum(intList))

def remove_board_number(boardList, boardCount, winningList):
    for num in range(0,len(boardList)):
        if len(boardList) == 1:
            return
        if boardCount in boardList:
            if boardCount == boardList[num]:
                print("\n Removing board #: " + str(boardList[num]))
                #winningList.append(boardList[num])
                boardList.remove(boardList[num])

def check_win_conditions(allBoards, boardList, checking):
    #how many boards to go through
    boardToCheck = allBoards[checking]
    if checking in boardList:
        #print("\n Checking this board:")
        #print(boardToCheck)
        if  (boardToCheck[0] == 'X') and (boardToCheck[1] == 'X') and (boardToCheck[2] == 'X') and (boardToCheck[3] == 'X') and (boardToCheck[4] == 'X'):
            print("Vertical win, row 1")
            #sum numbers here
            #sum_unmarked_numbers(allBoards[boardCount])
            return True
        elif (boardToCheck[5] == 'X') and (boardToCheck[6] == 'X') and (boardToCheck[7] == 'X') and (boardToCheck[8] == 'X') and (boardToCheck[9] == 'X'):
            print("Vertical win, row 2")
            #sum_unmarked_numbers(allBoards[boardCount])
            return True
        elif (boardToCheck[10] == 'X') and (boardToCheck[11] == 'X') and (boardToCheck[12] == 'X') and (boardToCheck[13] == 'X') and (boardToCheck[14] == 'X'):
            print("Vertical win, row 3")
            #sum_unmarked_numbers(allBoards[boardCount])    
            return True
        elif (boardToCheck[15] == 'X') and (boardToCheck[16] == 'X') and (boardToCheck[17] == 'X') and (boardToCheck[18] == 'X') and (boardToCheck[19] == 'X'):
            print("Vertical win, row 4")
            #sum_unmarked_numbers(allBoards[boardCount])
            return True
        elif (boardToCheck[20] == 'X') and (boardToCheck[21] == 'X') and (boardToCheck[22] == 'X') and (boardToCheck[23] == 'X') and (boardToCheck[24] == 'X'):
            print("Vertical win, row 5")

            #sum_unmarked_numbers(allBoards[boardCount])
            return True
        elif (boardToCheck[0] == 'X') and (boardToCheck[5] == 'X') and (boardToCheck[10] == 'X') and (boardToCheck[15] == 'X') and (boardToCheck[20] == 'X'):
            print("Horizontal win, column 1")
            #sum_unmarked_numbers(allBoards[boardCount])
            return True
        elif (boardToCheck[1] == 'X') and (boardToCheck[6] == 'X') and (boardToCheck[11] == 'X') and (boardToCheck[16] == 'X') and (boardToCheck[21] == 'X'):
            print("Horizontal win, column 2")
            #sum_unmarked_numbers(allBoards[boardCount])
            return True
        elif (boardToCheck[2] == 'X') and (boardToCheck[7] == 'X') and (boardToCheck[12] == 'X') and (boardToCheck[17] == 'X') and (boardToCheck[22] == 'X'):
            print("Horizontal win, column 3")
            #sum_unmarked_numbers(allBoards[boardCount])
            return True
        elif (boardToCheck[3] == 'X') and (boardToCheck[8] == 'X') and (boardToCheck[13] == 'X') and (boardToCheck[18] == 'X') and (boardToCheck[23] == 'X'):
            print("Horizontal win, column 4")
            #sum_unmarked_numbers(allBoards[boardCount])
            return True
        elif (boardToCheck[4] == 'X') and (boardToCheck[9] == 'X') and (boardToCheck[14] == 'X') and (boardToCheck[19] == 'X') and (boardToCheck[24] == 'X'):
            print("Horizontal win, column 5")
            #sum_unmarked_numbers(allBoards[boardCount])
            return True

def get_num_boards(output):
    num = 0
    for i in (range(1,len(output))):
        if output[i] == '':
            num += 1

    return num
    
filename = r'AoC-4-Test.txt'
output = input_as_lines(filename)
set_boards(output)
