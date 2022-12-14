from Day_3_p1 import rucksacks, alphabet_vals

total = 0

for i in range(0, len(rucksacks), 3):
    first = rucksacks[i]
    second = rucksacks[i + 1]
    third = rucksacks[i + 2]

    for j in first:
        if (j in second) and (j in third):
            total += alphabet_vals[j]
            break

print(total)
