file=open('Day1/input.txt', 'r')
lines = file.readlines()

first_digit = 0
last_digit = 0
calibration_values = []

for line in lines:
    for char in line:
        if char.isdigit():
            first_digit = char
            break

    for char in line[::-1]:
        if char.isdigit():
            last_digit = char
            break

    calibration_values.append(int(first_digit + last_digit))

print(calibration_values)

result = 0

for number in calibration_values:
    result += number

print(result)