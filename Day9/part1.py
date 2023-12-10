from collections import Counter


file = open('Day9/input.txt', 'r')
lines = file.read().splitlines()

def finddiffs(numbers):
    diffs = []
    for previous, current in zip(numbers, numbers[1:]):
        diffs.append(current-previous)
    
    if(len(Counter(diffs).values()) == 1): # If all divs are the same, traverse back up
        return diffs[0]
    
    last_number = diffs[-1]
    next_number = last_number + finddiffs(diffs)
    return next_number

total = 0
for line in lines:
    string_numbers = line.split(' ')
    numbers = [eval(i) for i in string_numbers]

    next_number = finddiffs(numbers)
    print(next_number)
    print(numbers[-1] + next_number)
    total += numbers[-1] + next_number

print('<<<<<<<<< ' + str(total) + ' >>>>>>>>>')
        
    
    