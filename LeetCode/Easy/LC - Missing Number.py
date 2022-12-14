def missingNumber(nums: [int]) -> int:
    missing_sum = sum(nums)
    largest_int = max(nums)

    true_sum = sum([x for x in range(largest_int + 1)])
    missing_value = true_sum - missing_sum

    if 0 not in nums:
        return 0
    elif missing_value == 0:
        return largest_int + 1
    else:
        return missing_value


print(missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))
