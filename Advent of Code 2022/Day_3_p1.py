from Day_3_Data import rucksacks

rucksacks = rucksacks.split('\n')
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_vals = {}
total = 0

for i in range(len(characters)):
    alphabet_vals[characters[i]] = i + 1

for v in rucksacks:
    mid = len(v) // 2
    compartment1 = v[:mid]
    compartment2 = v[mid:]

    for j in compartment1:
        if j in compartment2:
            total += alphabet_vals[j]
            break



# print(alphabet_vals)
# print(rucksacks)
print(total)
