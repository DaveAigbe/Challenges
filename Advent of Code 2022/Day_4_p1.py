from Day_4_Data import pairs

pairs = pairs.split('\n')

count = 0

for i in range(len(pairs)):
    pairs[i] = pairs[i].split(',')

    for j in range(len(pairs[i])):
        pairs[i][j] = pairs[i][j].split('-')
        pairs[i][j][0] = int(pairs[i][j][0])
        pairs[i][j][1] = int(pairs[i][j][1])


for pair in pairs:
    set1 = pair[0]
    set2 = pair[1]

    set1_x = set1[0]
    set1_y = set1[1]
    set2_x = set2[0]
    set2_y = set2[1]

    if (set1_x <= set2_x) and (set1_y >= set2_y):
        count += 1
    elif (set2_x <= set1_x) and (set2_y >= set1_y):
        count += 1


print(count)
"""
- Check the first value, and last value of one pair in a set
- If a pairs smallest value is less than or equal to AND* greatest value is larger than its corresponding pair smallest/greatest
  values then it is fully contained
- If a pairs smallest value is less than AND* greatest value is larger than or equal to its corresponding pair smallest/greatest
  values then it is fully contained
"""
