from Day_5_Data import directions

"""
Separate stacks
"""

keys = [x for x in range(1, 10)]
values = [[['N'], ['W'], ['B']],
          [['B'], ['M'], ['D'], ['T'], ['P'], ['S'], ['Z'], ['L']],
          [['R'], ['W'], ['Z'], ['H'], ['Q']],
          [['R'], ['Z'], ['J'], ['V'], ['D'], ['W']],
          [['B'], ['M'], ['H'], ['S']],
          [['B'], ['P'], ['V'], ['H'], ['J'], ['N'], ['G'], ['L']],
          [['S'], ['L'], ['D'], ['H'], ['F'], ['Z'], ['Q'], ['J']],
          [['B'], ['Q'], ['G'], ['J'], ['F'], ['S'], ['W']],
          [['J'], ['D'], ['C'], ['S'], ['M'], ['W'], ['Z']]
          ]
stacks = {k: v for k, v in zip(keys, values)}
# print(stacks)

""""""

"""
Separate directions
"""

directions = directions.split('\n')


# print(directions)

def findDigits(char: str):
    if char.isnumeric():
        return True
    else:
        return False


for i, direction in enumerate(directions):
    filteredDirection = list(filter(findDigits, direction))

    if len(filteredDirection) == 4:
        directions[i] = {'move_amount': int(filteredDirection[0] + filteredDirection[1]), 'from': int(filteredDirection[2]),
                         'to': int(filteredDirection[3])}
    else:
        directions[i] = {'move_amount': int(filteredDirection[0]), 'from': int(filteredDirection[1]),
                         'to': int(filteredDirection[2])}

# print(directions)

""""""

"""
Organize stacks
"""
for direction in directions:
    #  They are placed 1 by 1, so the list is always flipped when being stacked
    move = stacks[direction['from']][:direction['move_amount']][::-1]

    stacks[direction['to']] = move + stacks[direction['to']]

    stacks[direction['from']] = stacks[direction['from']][direction['move_amount']:]

# print(stacks)


"""
Find top crates
"""
top_crates = []

for stack in stacks:
    top_crates.append(stacks[stack][0][0])

print(''.join(top_crates))
