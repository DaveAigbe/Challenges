nums = [0]
maximum = len(nums) + 1


def first_solution(n, m):
    for i in range(0,
                   m):  # take the range according to the max number in the list+1 because range excludes the last value
        if i not in n:  # if a number in that range is not inside of the orginal list, return that number
            return i


def faster_solution(n):
    return sum(range(len(n) + 1)) - sum(n)


'''take the sum of the range of the list+1, this will all the numbers up
    until the maximum value in the list. Subtract that from the original list sum.
    For example in [3,0,1] it will take 3(length)+1(range ignores last value) = 4. The range will be
    [0,1,2,3] find the sum of this which is 6 and subtract that from the sum of the original list which is 4.
    6-4 = 2 which is the missing value'''

print(first_solution(nums, maximum))
print(faster_solution(nums))
