strings = input()  # Paws 11 Kittens 9 Feline_world 100 MEOW
split_strings = strings.split() # PUTS EVERYTHING AFTER WHITESPACE INTO A SEPERATE LIST INDEX! USE SPLIT!
numbers_inside = []
maximum = str()
counter = 0
if 'MEOW' in split_strings:
    split_strings = split_strings[:split_strings.index('MEOW')]  # GET RID OF ITEM AFTER THE INDEX THAT CONTAINS MEOW

for i in split_strings:
    if i.isnumeric():
        numbers_inside.append(i)

numbers_inside = [int(i) for i in numbers_inside]
maximum = str(max(numbers_inside))

for i in split_strings:
    if i == maximum:
        print(split_strings[counter - 1])  # MINUS 1 TO HELP WITH THE LAST INDEX
    counter += 1  # COUNTER TO FIND INDEX

'''for index, value in enumerate(x):
    if value == '3':
        print(x[index-1])'''