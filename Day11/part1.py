import numpy as np
import bfs_search

# input = np.loadtxt("Day11/input.txt", dtype=str, delimiter=None)
# print(input)

file = open('Day11/input.txt', 'r')
lines = file.read().splitlines()

formated_lines = []

empty_rows = []
empty_columns = []

# find empty rows
for index, line_value in enumerate(lines):
    if(not line_value.__contains__('#')):
        empty_rows.append(index)
    
    new_line_array = []
    for char in line_value:
        new_line_array.append(char)
    
    formated_lines.append(new_line_array)

print("empty rows: ")
print(empty_rows)

np_array = np.asarray(formated_lines)

# find empty columns
for column_index, _ in enumerate(range(len(np_array[0]))):
    current_column = np_array[:,column_index]

    if(not current_column.__contains__('#')):
        empty_columns.append(column_index)


print("empty columns: ")
print(empty_columns)

# construct array with expanded rows
added_so_far = 0
for empty_row in empty_rows:
    formated_lines.insert(empty_row + added_so_far, formated_lines[empty_row + added_so_far].copy())
    added_so_far += 1

# add expanded columns
added_so_far = 0
for empty_column in empty_columns:
    for row in formated_lines:
        row.insert(empty_column + added_so_far, '.')
    added_so_far += 1

# replace # with numbers and store points for each galaxy
galaxy_points = []
counter = 1
for row_index, row in enumerate(formated_lines):
    for index, char in enumerate(row):
        if(char == "#"):
            row[index] = counter
            counter += 1
            galaxy_points.append(bfs_search.Point(row_index, index))

        else:
            row[index] = 0

print(formated_lines.__len__())
print(formated_lines[0].__len__())

# find shortest path for all numbers
lengths = 0
for i, galaxy1 in enumerate(galaxy_points):
    for galaxy2 in galaxy_points[i + 1:]:
        lengths += abs(galaxy1.x - galaxy2.x) + abs(galaxy1.y - galaxy2.y)
print(lengths)
# visited_pairs = []
# sum_of_paths = []
# for point in galaxy_points:
#     for other_point in galaxy_points:
#         hash1 = str(point.x) + str(point.y) + str(other_point.x) + str(other_point.y)
#         hash2 = str(other_point.x) + str(other_point.y) + str(point.x) + str(point.y)
#         if(point != other_point and not visited_pairs.__contains__(hash1) and not visited_pairs.__contains__(hash2)):
#             visited_pairs.append(hash1)
#             shortest_path = bfs_search.BFS(mat=formated_lines, src=point, dest=other_point)
#             sum_of_paths.append(shortest_path)

# print(sum(sum_of_paths))