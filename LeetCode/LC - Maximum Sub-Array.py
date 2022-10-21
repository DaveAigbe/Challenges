def maxSubArray(nums):
    length = len(nums)
    if length == 1:
        return nums[0]
    sub_arrays = [nums[-1]]
    index = 0
    next_value = 1
    while index != length - 1:
        for endpoint in range(next_value, length + 1):
            sub_arrays.append(sum(nums[index:endpoint]))
        index += 1
        next_value += 1

    return max(sub_arrays)


print(maxSubArray([-2, 1]))

# -- ITS TOO SLOW!!!!!!!!
