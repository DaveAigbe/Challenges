from Day_1_Data import all_calories

all_calories = all_calories.split('\n')
all_totals = []

new_elf_pos = 0

for i, v in enumerate(all_calories):
    if v == '':
        current_total = sum([int(x) for x in all_calories[new_elf_pos:i]])
        all_totals.append(current_total)
        new_elf_pos = i + 1

# print(all_totals)
# print(max(all_totals))
