from data_list_Day1 import depths
increased = 0

current = 0
for depth in range(1, len(depths) - 1):
    if depths[depth] > depths[current]:
        increased += 1
        current += 1
    else:
        current += 1

print(increased + 1)  # The plus one takes into account the last 2 numbers
