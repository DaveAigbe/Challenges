def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for val in nums:
        if nums.count(val) == 1:
            return val


print(singleNumber([2,2,1]))
