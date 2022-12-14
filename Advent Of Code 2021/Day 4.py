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

# TODO: Make nested lists for each of the rows in a board. Split each value inside the rows by their spaces. When a number matches, swap out for an X. Each iteration check to see if a board has won.

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
            for value2 in range(40):  # mess with this range to find winner, the close the winner is to zero (range wise), the faster they won
                if organized_boards[lists][line][value1] == numbers_to_call[value2]:
                    organized_boards[lists][line][value1] = 'X'


# for x in organized_boards:
#     print(x, '\n')

for lists in range(len(organized_boards)): # for each board out of the 100
    for line in range(5): # for each line in the board
        if organized_boards[lists][line].count('X') == 5: # if a line in the board has 6 X's in a row, its the one
            print(organized_boards[lists])
        else:
            for index in range(len(organized_boards[lists][line])):  # for each index in the line
                if organized_boards[lists][0][index] == 'X' and organized_boards[lists][1][index] == 'X' and organized_boards[lists][2][index ] == 'X' and organized_boards[lists][3][index] == 'X' and organized_boards[lists][4][index] == 'X':
                    # Line Above: If each line in the board, at the same exact index equals X, then a row of X's has been created vertically, its the one
                    print(organized_boards[lists])  #print the winning board


print(numbers_to_call[69]) # grab the last index that was input (Used 29 as range above, but range ignores last value, so its 28)
# output was 14, so 14 was the last number that cause that bingo board to win
remaining_numbers = [28, 67, 45, 59, 51, 92, 6, 68, 8, 69, 84, 26]  # list of all the numbers that were not marked out
print(sum(remaining_numbers) * 14)  # sum of the remaining numbers multiplied by the value that cause the board to win

