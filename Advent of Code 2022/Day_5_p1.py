from Day_5_Data import directions

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
print(stacks)

directions = directions.split('\n')

for i in range(len(directions)):
    values = []
    for j in directions[i]:
        if j.isnumeric():
            values.append(int(j))

    directions[i] = {'move_amount': values[0], 'from': values[1], 'to': values[2]}

print(directions)

