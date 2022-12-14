def merge_sorted_array(nums1, m, nums2, n):
    nums1[m:] = nums2

    def quicksort_interface(arr):
        start = 0
        end = len(arr)
        quicksort(arr, start, end)

    def quicksort(arr, start, end):
        if start < end:
            divider = partition(arr, start, end)
            quicksort(arr, start, divider - 1)
            quicksort(arr, divider + 1, end)

    def partition(arr, start, end):
        divider = start + 1
        pivot = arr[start]

        for i in range(start + 1, end):
            if arr[i] < pivot:
                swap(arr, divider, i)
                divider += 1

        swap(arr, start, divider - 1)
        return divider - 1

    def swap(arr, ind1, ind2):
        arr[ind1], arr[ind2] = arr[ind2], arr[ind1]

    quicksort_interface(nums1)


sample = [1, 2, 3, 0, 0, 0]

print(sample)
merge_sorted_array(sample, 3, [2, 5, 6], 3)
print(sample)