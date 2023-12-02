import bag

file=open('Day2/input.txt', 'r')
lines = file.read().splitlines()

# prepare bag with cubes
master_bag = bag.Bag(12, 14, 13)

def holds_enough_cubes(color: str, number_of_cubes: int):
    if(color == 'red'):
        return number_of_cubes <=master_bag.number_of_red
    elif(color == 'green'):
        return number_of_cubes <=master_bag.number_of_green
    elif(color == 'blue'):
        return number_of_cubes <=master_bag.number_of_blue

valid_games = []

for line in lines:
    id_of_game = line.split(':')[0].replace("Game ", "") # get this string: 'Game 123:' and take number
    
    # check each round
    rounds = line.split(':')[1].split(";")
    is_possible = True

    # check each color for each round
    for round in rounds:
        current_round = round.strip().split(",")

        for cube_set in current_round:
            # split into number and color and match with the original bag. Ex: "15 Blue"
            count_and_color = cube_set.strip().split(" ")
            is_possible = holds_enough_cubes(count_and_color[1], int(count_and_color[0]))

            if (is_possible == False):
                break
        
        if (is_possible == False):
                break
    # save game id´s that would have been possible with the give bag
    if (is_possible):
        valid_games.append(int(id_of_game))
        
print(valid_games)
print("Sum of valid game id´s: " + str(sum(valid_games)))

