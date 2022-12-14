def quicksort_interface(arr):
    copyArr = arr.copy()
    start = 0
    end = len(arr) - 1
    quicksort(arr, start, end)
    return compareDifferences(arr, copyArr)


def quicksort(arr, start, end):  # Does not handle negative indexing, which exists and messes with the algorithm
    if start < end:
        divider = partition(arr, start, end)
        quicksort(arr, start, divider - 1)
        quicksort(arr, divider + 1, end)


def partition(arr, start, end):
    pivot_value = arr[start]
    divider = start + 1

    for i in range(start + 1, end + 1):
        if arr[i] < pivot_value:
            swap(arr, i, divider)
            divider += 1

    swap(arr, start, divider - 1)
    return divider - 1


def swap(arr, ind1, ind2):
    arr[ind1], arr[ind2] = arr[ind2], arr[ind1]


def compareDifferences(arr1, arr2):
    count = 0

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            count += 1

    return count


sample = [1, 1, 4, 2, 1, 3]
print(quicksort_interface(sample))

print(sample)




