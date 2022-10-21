from data_list_Day1 import depths

first = 0
second = 1
third = 2

by_three = []

for values in range(len(depths) - 2):  # exclude that last 2 numbers because they will not have pairs of 3
    current = depths[first] + depths[second] + depths[third]
    by_three.append(current)
    first += 1
    second += 1
    third += 1

increased = 0

current = 0
for summed in range(1, len(by_three) - 1):
    if by_three[summed] > by_three[current]:
        increased += 1
        current += 1
    else:
        current += 1

print(increased + 1)
