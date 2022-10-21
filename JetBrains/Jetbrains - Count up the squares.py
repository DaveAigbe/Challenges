def one_line_method():
    scores = [int(x) for x in input(
        'Insert desired numbers with space in between: ').split()]  # if you want to insert the numbers in one line
    sum_until_zero = scores[0]  # set this value to the first number given
    final_sum = 0  # this will be the final output when the numbers are squared
    used_numbers = [scores[0]]  # set the first index to the first value in the list
    Keep_adding = True

    while Keep_adding:
        for num in scores[1:]:  # start at index 1 instead of 0 because we already accounted for first number
            if sum_until_zero != 0:  # this is where the math will be done, it will keep adding each index until the sum is equal to zero
                used_numbers.append(num)  # everytime a number is used append to a new list so we can square it later and ignore the other values
                sum_until_zero = sum_until_zero + num  # add each index until sum_until_zero == 0
            else:  # when sum_until_zero == 0
                for x in used_numbers:  # for each value that helped get sum_until_zero to 0
                    final_sum = final_sum + x ** 2  # square the index then add it onto the next one in the list
                print(final_sum)
                break  # 2 break statements because there are 2 for loops, otherwise it will run twice, because only 1 for loop exited
        break


def gradual_input_method():
    addingNums = 0  # keep adding nums until i set setZero to 0
    setZero = [1]  # a list to end the while loop, i will empty it out and compare it with addingNums() as a sum() (empty list return 0)
    static_list = []  # this is the list that will take the values that sum() is 0
    squared_sum = 0  # this will be the final output when the numbers are squared
    while addingNums != sum(setZero):  # currently 0 != 1 which is true
        x = int(input('enter : '))  # will take input each time until i set the while as 0 != 0 which is false
        if x != 0:  # if the input is anything other than 0
            static_list.append(x)  # append it to my empty list
        if sum(static_list) == 0:  # if the sum of all the appended inputs is equal to 0 clear out my list to end while loop ( 0 != 0 is false, kills while loop)
            setZero.clear()  # clear out list that had the sum of 1, it will be an empty list now which will equal 0

    for x in static_list:  # for each value that helped get sum_until_zero to 0
        squared_sum = squared_sum + x ** 2  # square the index then add it onto the next one in the list

    print(squared_sum)
