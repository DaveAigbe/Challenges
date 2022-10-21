distances = "Rkbs,5453; Wdqiz,1245; Rwds,3890; Ujma,5589; Tbzmo,1303;"
numbers = []
distances = distances.replace(';', '')
distances = distances.replace(',', ' ')
distances = distances.split(' ')

for i in distances:
    if i.isnumeric():
        numbers.append(i)

numbers = [int(x) for x in numbers]
numbers.sort()
final = [numbers[0]]

for i in range(0, len(numbers) - 1):
    j = numbers[i + 1] - numbers[i]
    final.append(str(j))

final[0] = str(final[0])
final = ', '.join(final)

print(final)
