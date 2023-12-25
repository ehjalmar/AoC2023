import numpy as np

file = open('Day15/input.txt', 'r')
steps = file.read().split(',')

boxes = [{} for i in range(256)]

def hash_it(input: str):
    current_value = 0
    for char in input:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value

for step in steps:
    if(step.__contains__('=')):
        current_str = step.split('=')
        current_label = current_str[0]
        key = hash_it(current_label)
        print(key)
        focal_length = current_str[1]
        boxes[key][current_label] = focal_length
    elif(step.__contains__('-')):
        current_str = step.split('-')
        current_label = current_str[0]
        key = hash_it(current_str[0])
        print(key)
        focal_length = current_str[1]
        if current_label in boxes[key]:
            boxes[key].__delitem__(current_label)
    # sum += current_value

focusing_powers = []
for box_index, box in enumerate(boxes):
    for slot_index, lens_label in enumerate(box):
        current_value = box_index+1
        current_value *= slot_index+1
        current_value *= int(box[lens_label])
        focusing_powers.append(current_value)

print(sum(focusing_powers))