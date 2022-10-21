def majorityElement(nums):
    y = []
    largest = 0
    for i in nums:
        if i not in y:
            y.append(i)

    for i in y:
        if nums.count(i) > nums.count(largest):
            largest = i

    return largest


print(majorityElement([1,2,1,1,1,2,2,2,1,2,2,1,1]))