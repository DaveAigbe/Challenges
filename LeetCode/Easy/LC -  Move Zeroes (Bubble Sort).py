def optimized():
    nums = [0, 0, 1]
    x = nums.count(0)
    zeroes = []
    non_zero = []

    for i in nums:
        if i == 0:
            zeroes.append(i)
        else:
            non_zero.append(i)
    nums[:] = list(non_zero + zeroes)
    return nums


'''SOLVE THIS ALGORITHMICALLY WITH SORTING. Probably bubble sort, but instead check to see if the value next to 
 it is a zero. If the value is not a zero swap the numbers (causing 0 to move up). This can also be done as if the 
 number at x index is greater than zero swap them.'''


def using_bubble_sort():
    nums = [0, 0, 1]
    indexing_length = range(0, len(nums) - 1)
    sorted = False

    while not sorted:
        sorted = True
        for i in indexing_length:
            if nums[i] == 0 and nums[i + 1] != 0:
                sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


print(using_bubble_sort())
print(optimized())