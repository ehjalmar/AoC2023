file=open('Day1/input.txt', 'r')
lines = file.read().splitlines()

numbers = "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" 
numbersMapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine" : "9" 
}

def convertSpelledDigits(line, take_last_item):
    index_of_number = {}
    for number in numbers:
        current_index = -1
        if(take_last_item):
            current_index = line.rfind(number) # Take last index if we´re search from back, otherwise strings with multiple occurences of the same splled number will not work
        else:
            current_index = line.find(number)

        if current_index > -1:
            index_of_number[number] = current_index
    
    if(len(index_of_number) < 1): # No spelled numbers found
        return line

    sorted_index_of_numbers = sorted(index_of_number.items(), key=lambda x:x[1])
    spelled_number = None
    if(take_last_item):
        spelled_number = sorted_index_of_numbers[-1:][0][0]
    else:
        spelled_number = sorted_index_of_numbers[0][0]
    mapped_number = numbersMapping[spelled_number]
    new_string = line.replace(spelled_number, mapped_number)
    return new_string
    
first_digit = 0
last_digit = 0
calibration_values = []

for line in lines:
    for char in convertSpelledDigits(line, False):
        if char.isdigit():
            first_digit = char
            break

    for char in convertSpelledDigits(line, True)[::-1]:
        if char.isdigit():
            last_digit = char
            break

    calibration_values.append(int(first_digit + last_digit))

print(calibration_values)

result = 0

for number in calibration_values:
    result += number

print(result)