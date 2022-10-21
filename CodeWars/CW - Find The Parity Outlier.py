def find_outlier(numbers):
    even = 0  # counters to keep track of how many even and odds were found
    odd = 0
    if len(numbers) < 4:  # if the list is only 3 values, loop through all 3 to find if its an even or odd list
        for i in numbers:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    else:
        for x in range(0, 4):  # only check first 3 numbers since there is only 1 outlier
            if numbers[x] % 2 == 0:  # this checks to see if its a list of even or odds
                even += 1
            else:
                odd += 1

    if even < odd:  # if its a list of odds, find the even
        for number in numbers:
            if number % 2 == 0:
                return number
    else:  # otherwise it must be a list of evens so find the odd
        for number in numbers:
            if number % 2 == 1:
                return number

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))