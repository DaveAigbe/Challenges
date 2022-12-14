nums = [1, 3, 5]
x = 0
target = 4

left = 0
right = len(nums) - 1


def insertion():
    for i in range(1, len(nums)):
        while nums[i - 1] > nums[i] and i > 0:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i -= 1
    return nums


def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        items_greater = []
        items_lower = []

        for items in sequence:
            if items > pivot:
                items_greater.append(items)
            else:
                items_lower.append(items)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


while left <= right:
    mid = (round((left + right) / 2))
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] > target:
        right = mid - 1
    elif nums[mid] < target:
        left = mid + 1
else:
    nums.insert(1, target)
    nums = quick_sort(nums)
    print(nums)
    for i in nums:
        if i == target:
            print(x)
        x += 1
