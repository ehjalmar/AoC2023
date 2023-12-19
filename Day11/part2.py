import numpy as np
import bfs_search # ended up only using this for the Point class... BFS was not needed

# input = np.loadtxt("Day11/input.txt", dtype=str, delimiter=None)
# print(input)

file = open('Day11/input.txt', 'r')
lines = file.read().splitlines()

formated_lines = []


# replace # with numbers and store points for each galaxy
new_lines = []
galaxy_points = []
counter = 1
for row_index, row in enumerate(lines):
    new_line = []
    for index, char in enumerate(row):
        if(char == "#"):
            new_line.append((index, row_index))
        else:
            new_line.append(None)
    new_lines.append(new_line)

multiplier = 999999

# Fix Y/Columns
galaxy_points = []
empty_rows = 0
for row_index, row in enumerate(new_lines):
    new_line = []
    if len(set(row)) > 1:
        for index, value in enumerate(row):
            if(value != None):
                row[index] = (value[0], value[1] + empty_rows * multiplier)
    else:
        empty_rows += 1

# Fix X/Rows
empty_columns = 0
for column_index in range(len(new_lines[0])):
    column = [new_lines[y][column_index] for y in range(len(new_lines))]
    if len(set(column)) > 1:
        for index, value in enumerate(column):
            if(value != None):
                new_lines[index][column_index] = (value[0] + empty_columns * multiplier, value[1])
    else:
        empty_columns += 1

galaxy_points = []
counter = 1
for row_index, row in enumerate(new_lines):
    for index, value in enumerate(row):
        if(value != None):
            galaxy_points.append(bfs_search.Point(value[0], value[1]))

# find shortest path for all numbers
lengths = 0
for i, galaxy1 in enumerate(galaxy_points):
    for galaxy2 in galaxy_points[i + 1:]:
        lengths += abs(galaxy1.x - galaxy2.x) + abs(galaxy1.y - galaxy2.y)
print(lengths)
