def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    def quicksort(arr):
        arr_len = len(arr)

        if arr_len <= 1:
            return arr
        else:
            current_partition = 0

            for pos in range(1, arr_len):
                if arr[pos] <= arr[0]:
                    current_partition += 1
                    arr[pos], arr[current_partition] = arr[current_partition], arr[pos]

            arr[0], arr[current_partition] = arr[current_partition], arr[0]

            left = quicksort(arr[:current_partition])
            right = quicksort(arr[current_partition + 1:])

            arr[:] = left + [arr[current_partition]] + right
        return arr

    nums[:] = quicksort(nums)

nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))
