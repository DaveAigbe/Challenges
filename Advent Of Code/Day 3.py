from data_list_Day3 import binary_numbers

binary = ''
iteration = 11
string_index = 0
while iteration >= 0:
    zeroes = 0
    ones = 0
    for numbers in range(len(binary_numbers)):
        if binary_numbers[numbers][string_index] == '1':
            ones += 1
        else:
            zeroes += 1
    if ones > zeroes:
        binary += '1'
    else:
        binary += '0'
    string_index += 1
    iteration -= 1

print(binary)

print(1836 * 2259)