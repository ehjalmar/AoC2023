file = open('input.txt', 'r')
lines = file.read().splitlines()

def get_ways_to_win(time: int, record_distance: int) -> int:
    
    ways_to_win = 0
    hold_time = 1
    while True:
        distance = (time-hold_time) * hold_time
        hold_time += 1
        if(distance > record_distance):
            ways_to_win += 1
        elif(ways_to_win > 1 and hold_time > 2):
            break
    
    return ways_to_win

times = list(filter(None, lines[0].split(':')[1].split(' ')))
record_distances = list(filter(None, lines[1].split(':')[1].split(' ')))
races = zip(times, record_distances)

result = 1
for race in races:
    #print(get_ways_to_win(int(race[0]), int(race[1])))
    result *= get_ways_to_win(int(race[0]), int(race[1]))
    
print(result)
