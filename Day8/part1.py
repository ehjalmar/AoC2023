import string

file = open('Day8/input.txt', 'r')
lines = file.read().splitlines()

class Mapping:
    def __init__(self, index: str, left: str, right: str) -> None:
        self.index = index
        self.left = left
        self.right = right

directions = lines[0]
mappings = {}

for line in lines[2:]:
    a = line.split('=')
    b = a[0].strip()[0:3]
    left = a[1].strip()[1:4]
    right = a[1].strip()[6:9]
    mappings[b] = (Mapping(b, left, right))

current_position = 'AAA'
current_index = -1
turn = 0

while current_position != 'ZZZ':
    current_index += 1
    current_direction = directions[current_index]

    if(current_direction == 'L'):
        current_position = mappings[current_position].left
    elif(current_direction == 'R'):
        current_position = mappings[current_position].right
    
    if(current_index == len(directions)-1):
        current_index = -1

    turn += 1

print(str(turn))