import numpy as np

file = open('Day15/input.txt', 'r')
steps = file.read().split(',')

sum = 0
for step in steps:
    current_value = 0
    for char in step:
       current_value += ord(char)
       current_value *= 17
       current_value = current_value % 256
    print(current_value)
    sum += current_value

print(sum)