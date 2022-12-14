from data_list_Day2 import positions

horizontal_position = 0
aim = 0
depth = 0

numbers = []

for index in positions:
    if index.isdigit():
        numbers.append(int(index))

positions = positions.split('\n')

for index in range(len(positions)):
    if 'forward' in positions[index]:
        horizontal_position += numbers[index]
        depth += aim * numbers[index]
    elif 'down' in positions[index]:
        aim += numbers[index]
    elif 'up' in positions[index]:
        aim -= numbers[index]

print(horizontal_position * depth)
