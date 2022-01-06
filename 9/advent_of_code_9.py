#Advent of Code - Day 9: Smoke Basin
from typing import List

"""
Helper functions to reuse for puzzles - thanks Danielle Lucek!
"""
def input_as_string(filename:str) -> str:
    """returns the content of the input file as a string"""
    with open(filename,'r',encoding="utf8") as file_to_open:
        return file_to_open.read().rstrip("\n")

def input_as_lines(filename:str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")

def input_as_ints(filename:str) -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))

def make_grid(lines):
    #Creates the grid of tubes
    tubes = []
    for row in lines:
        tube_row = [int(c) for c in row]
        tubes.append(tube_row)

    return tubes

def check_neighbors(x, y, tubes, count):
    """Checks 4 neighbors for each tube and inc count if adjacents higher"""
    #Left: (-1, 0)
    #Right: (0, 1)
    #Top: (0, -1)
    #Down: (1, 0)
    adjacent = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    for offset in adjacent:
        #print(f"Current element is: {tubes[y][x]}")
        neighbor_y = y + offset[0]
        neighbor_x = x + offset[1]
        if neighbor_y in range(0,len(tubes)) and neighbor_x in range(0,len(tubes[0])):
            if tubes[y][x] < tubes[neighbor_y][neighbor_x]:
                #print(f"The current point: {tubes[y][x]} is less than {tubes[neighbor_y][neighbor_x]}")
                count += 1
    return count

def print_low_points(lowPoint):
    """Prints the low points - may not need"""
    for i in range(0,len(lowPoint)):
        print(lowPoint[i])

def find_low_points(lowPoints):
    """"""
    points_loc = []
    low_count = 0
    basins = [] #length of each basin list
    for y in range(0,len(tubes)):
        for x in range(0,len(tubes[0])):
            basin_size = [] #list of each basin
            low_count = check_neighbors(x,y,tubes,low_count)

            if low_count == 4: #center spaces
                lowPoints.append(tubes[y][x])
                points_loc.append((y,x))
                print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
                basin_size.append((x,y)) #append the low point
                basin_size = find_basins(x, y, tubes, basin_size) #find the rest of the basin
                basins.append(len(basin_size)) #append the size of that list
                #print(f"Basin size is: {basin_size}")
            elif low_count == 3: #edge cases
                if x == 0 or y == 0:
                    #print("edge case")
                    print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
                    lowPoints.append(tubes[y][x])
                    points_loc.append((y,x))
                    basin_size.append((x,y)) #append the low point
                    basin_size = find_basins(x, y, tubes, basin_size) #find the rest of the basin
                    basins.append(len(basin_size)) #append the size of that list
                    #print(f"Basin size is: {basin_size}")
                elif x == rows or y == cols:
                    #print("end edge case")
                    print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
                    lowPoints.append(tubes[y][x])
                    points_loc.append((y,x))
                    basin_size.append((x,y)) #append the low point
                    basin_size = find_basins(x, y, tubes, basin_size) #find the rest of the basin
                    basins.append(len(basin_size)) #append the size of that list
                    #print(f"Basin size is: {basin_size}")
            elif low_count == 2: #corner cases
                if y == 0 and x == 0:
                    #print("top left corner")
                    print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
                    lowPoints.append(tubes[y][x])
                    points_loc.append((y,x))
                    basin_size.append((x,y)) #append the low point
                    basin_size = find_basins(x, y, tubes, basin_size) #find the rest of the basin
                    basins.append(len(basin_size)) #append the size of that list
                    #print(f"Basin size is: {basin_size}")
                elif y == 0 and x == rows:
                    #print("top right corner")
                    print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
                    lowPoints.append(tubes[y][x])
                    points_loc.append((y,x))
                    basin_size.append((x,y)) #append the low point
                    basin_size = find_basins(x, y, tubes, basin_size) #find the rest of the basin
                    basins.append(len(basin_size)) #append the size of that list
                    #print(f"Basin size is: {basin_size}")
                elif y == cols and x == 0:
                    #print("bottom left corner")
                    print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
                    lowPoints.append(tubes[y][x])
                    points_loc.append((y,x))
                    basin_size.append((x,y)) #append the low point
                    basin_size = find_basins(x, y, tubes, basin_size) #find the rest of the basin
                    basins.append(len(basin_size)) #append the size of that list
                    #print(f"Basin size is: {basin_size}")
                elif y == cols and x == rows:
                    #print("bottom right corner")
                    print(f"Low point: {tubes[y][x]} at x: {x} y: {y}")
                    lowPoints.append(tubes[y][x])
                    points_loc.append((y,x))
                    basin_size.append((x,y)) #append the low point
                    basin_size = find_basins(x, y, tubes, basin_size) #find the rest of the basin
                    basins.append(len(basin_size)) #append the size of that list
                    #print(f"Basin size is: {basin_size}")
            else:
                print(f"Ignore {tubes[y][x]}\n")
            low_count = 0

    print_low_points(lowPoints)

    #if a low point is found, immediately find the basin?
    basins.sort()
    print(f"Basins: {basins}")
    three_largest_basins = basins[len(basins)-1] * basins[len(basins)-2] * basins[len(basins)-3]
    print(f"Three largest basins multiplied are: {three_largest_basins}")

    return lowPoints

def inc_lowpoints(points):
    #increase low points value by 1 for part 1
    for i in range(0,len(points)):
        points[i] += 1

    print(sum(points))

def find_basins(x, y, tubes, size):
    """Refactor and merge with check_neighbors with a part_one = True var"""
    adjacent = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    #stay in bounds
    for offset in adjacent:
        #print(f"Current element is: {tubes[y][x]}")
        neighbor_y = y + offset[0]
        neighbor_x = x + offset[1]
        if neighbor_y in range(0,len(tubes)) and neighbor_x in range(0,len(tubes[0])):
            if tubes[neighbor_y][neighbor_x] > tubes[y][x] and tubes[neighbor_y][neighbor_x] != 9:
                if (neighbor_x,neighbor_y) not in size:
                    print(f"The current point: {tubes[y][x]} | Neighbor point: {tubes[neighbor_y][neighbor_x]}")
                    size.append((neighbor_x,neighbor_y))
                    #print(f"Current size is: {size}")
                    size = find_basins(neighbor_x, neighbor_y, tubes, size)
    return size
    
f = 'AoC-9.txt'
tubes = input_as_lines(f)
tubes = make_grid(tubes)
#print(len(tubes)) #y value
cols = len(tubes)-1
rows = len(tubes[0])-1
#print(tubes)

low_points = []
low_points = find_low_points(low_points)
#inc_lowpoints(low_points)
