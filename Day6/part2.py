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

time = lines[0].split(':')[1].replace(' ','')
record_distance = lines[1].split(':')[1].replace(' ','')
result = get_ways_to_win(int(time), int(record_distance))
    
print(result)
