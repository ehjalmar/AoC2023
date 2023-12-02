import bag

file=open('Day2/input.txt', 'r')
lines = file.read().splitlines()

# prepare bag with cubes
master_bag = bag.Bag(12, 14, 13)

def update_bag(bag: bag.Bag, color: str, number_of_cubes: int):
    if(color == 'red'):
        if(number_of_cubes > bag.number_of_red):
            bag.number_of_red = number_of_cubes
    elif(color == 'green'):
        if(number_of_cubes > bag.number_of_green):
            bag.number_of_green = number_of_cubes
    elif(color == 'blue'):
        if(number_of_cubes > bag.number_of_blue):
            bag.number_of_blue = number_of_cubes
    return bag

bags_per_round = []

for line in lines:
    id_of_game = line.split(':')[0].replace("Game ", "") # get this string: 'Game 123:' and take number
    
    # check each round
    rounds = line.split(':')[1].split(";")
    is_possible = True

    # get minimun number for each color for each round
    current_bag = bag.Bag(0, 0, 0) # Start with 0 on all colors
    for round in rounds:
        current_round = round.strip().split(",")

        for cube_set in current_round:
            # split into number and color and match with the original bag. Ex: "15 Blue"
            count_and_color = cube_set.strip().split(" ")
            current_bag = update_bag(current_bag, count_and_color[1], int(count_and_color[0]))
        
    # save bag with minimun number of cubes per colors
    bags_per_round.append(current_bag)

power = 0
for x in bags_per_round:        
    power += x.get_power()
print(power)

