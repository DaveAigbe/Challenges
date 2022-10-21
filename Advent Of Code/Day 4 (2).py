from data_list_Day4 import bingo_boards, numbers_to_call

seperated_boards = bingo_boards.split('\n')
organized_boards = []

for lines in seperated_boards:  # take the whitespaces out from the seperated boards
    if lines == '':
        seperated_boards.remove(lines)

first = 0
second = 1
third = 2
fourth = 3
fifth = 4

for lines in range(0, len(seperated_boards), 5):  # put the boards together
    join_board = [seperated_boards[first].split(' '), seperated_boards[second].split(' '),
                  seperated_boards[third].split(' '), seperated_boards[fourth].split(' '),
                  seperated_boards[fifth].split(' ')]

    organized_boards.append(join_board)
    first += 5
    second += 5
    third += 5
    fourth += 5
    fifth += 5

for lists in range(len(organized_boards)):  # take out all the leftover whitespaces inside of the nested lists, caused by single digit numbers
    for line in range(5):
        for x in organized_boards[lists][line]:
            if x == '':
                organized_boards[lists][line].remove('')


for lists in range(len(organized_boards)):  # test to see if any list with extra whitespace are left, if nothing prints, the lists are formatted properly
    for line in range(5):
        if len(organized_boards[lists][line]) == 6:
            print(organized_boards[lists][line])

for number in range(len(numbers_to_call)):  # Make all the numbers in the bingo list strings so they can be compared
    numbers_to_call[number] = str(numbers_to_call[number])
##############################################################################################################################################################################################
# Above was all the setup work. Below is all the work to actually find the answer.


for lists in range(len(organized_boards)):  # take out all the leftover whitespaces inside of the nested lists, caused by single digit numbers
    for line in range(5):
        for value1 in range (len(organized_boards[lists][line])):
            for value2 in range(68):  # mess with this range to find winner, the close the winner is to zero (range wise), the faster they won
                if organized_boards[lists][line][value1] == numbers_to_call[value2]:
                    organized_boards[lists][line][value1] = 'X'

horizontal = []
vertical = []
won = []


for lists in range(len(organized_boards)):  # for each board out of the 100
    for line in range(5): # for each line in the board
        if organized_boards[lists][line].count('X') == 5: # if a line in the board has 6 X's in a row, its the one
            if organized_boards[lists] in won:
                continue
            else:
                horizontal = []
                horizontal.append(organized_boards[lists])
                won.append(organized_boards[lists])
        else:
            for index in range(len(organized_boards[lists][line])):  # for each index in the line
                if organized_boards[lists][0][index] == 'X' and organized_boards[lists][1][index] == 'X' and organized_boards[lists][2][index ] == 'X' and organized_boards[lists][3][index] == 'X' and organized_boards[lists][4][index] == 'X':
                    # Line Above: If each line in the board, at the same exact index equals X, then a row of X's has been created vertically, its the one
                        vertical = []
                        vertical.append(organized_boards[lists])
                        won.append(organized_boards[lists])# print the winning board


print(horizontal)
print('\n\n')
print(vertical)


winning_number = int(numbers_to_call[51])
print(winning_number)
remaining_numbers = [26,54, 94,80,24,78,34,98,89,10]
print(sum(remaining_numbers) * winning_number)  
