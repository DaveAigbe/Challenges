def contains_duplicate(nums):
    length_list = len(nums)
    length_set = len(set(x for x in nums))

    if length_list != length_set:
        return True
    else:
        return False

# too slow
def contains_duplicate2(nums):
    distinct = []
    for num in nums:
        if num not in distinct:
            distinct.append(num)
        else:
            return True
    return False


print(contains_duplicate([1, 2, 3, 4, 1]))
print(contains_duplicate2([1, 2, 3, 4, 1]))
