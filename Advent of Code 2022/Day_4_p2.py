from Day_4_p1 import pairs

count = 0

for pair in pairs:
    set1 = pair[0]
    set2 = pair[1]

    set1_x = set1[0]
    set1_y = set1[1]
    set2_x = set2[0]
    set2_y = set2[1]

    set1_array = [x for x in range(set1_x, set1_y + 1)]
    set2_array = [x for x in range(set2_x, set2_y + 1)]

    for i in set1_array:
        if i in set2_array:
            count += 1
            break

print(count)
