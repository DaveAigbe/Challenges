def majorityElement(nums: [int]):
    unique_values = set(nums)
    values_map = {}

    for i in unique_values:
        if i not in values_map:
            values_map[i] = 0

    for i in nums:
        values_map[i] = values_map[i] + 1

    majority_element = 0
    max_value = 0

    for i in values_map:
        if values_map[i] > max_value:
            max_value = values_map[i]
            majority_element = i

    return majority_element



print(majorityElement([1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 1]))

