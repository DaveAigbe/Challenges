from data_list_Day3 import binary_numbers

binary = []
iteration = 7
string_index = 0
while iteration >= 0:
    print(iteration)
    zeroes = 0
    ones = 0
    for numbers in range(len(binary_numbers)):
        if binary_numbers[numbers][string_index] == '1':
            ones += 1
        else:
            zeroes += 1
    print(f'zeroes: {zeroes} ones: {ones}')
    if zeroes < ones:
        for numbers in range(len(binary_numbers)):
            if binary_numbers[numbers][string_index] == '0':
                binary.append(binary_numbers[numbers])
    else:
        for numbers in range(len(binary_numbers)):
            if binary_numbers[numbers][string_index] == '1':
                binary.append(binary_numbers[numbers])
    string_index += 1
    iteration -= 1
    print(binary)
    binary_numbers[:] = binary[:]
    binary = []


# Code for checking least common :     if zeroes < ones:
#         for numbers in range(len(binary_numbers)):
#             if binary_numbers[numbers][string_index] == '0':
#                 binary.append(binary_numbers[numbers])
#     else:
#         for numbers in range(len(binary_numbers)):
#             if binary_numbers[numbers][string_index] == '1':
#                 binary.append(binary_numbers[numbers])


# Code for checking most common:     if ones > zeroes:
#         for numbers in range(len(binary_numbers)):
#             if binary_numbers[numbers][string_index] == '1':
#                 binary.append(binary_numbers[numbers])
#     else:
#         for numbers in range(len(binary_numbers)):
#             if binary_numbers[numbers][string_index] == '0':
#                 binary.append(binary_numbers[numbers])

# Oxygen = 010110010011 ~ 1427

# CO2 = 10011110100 ~ 1268
# Trial and error between a list of these ['100111000110', '100111010100', '100111010110', '100111001010', '100111101000', '100111111010', ]
print(1427*1268)