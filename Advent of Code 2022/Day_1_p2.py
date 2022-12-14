from Day_1_p1 import all_totals


def quicksort_interface(arr):
    start = 0
    end = len(arr) - 1

    quicksort(arr, start, end)


def quicksort(arr, start, end):
    if start < end:
        d = divide(arr, start, end)
        quicksort(arr, start, d - 1)
        quicksort(arr, d + 1, end)


def divide(arr, start, end):
    create_best_pivot(arr, start, end)

    pivot_value = arr[start]
    divider_index = start + 1

    for j in range(start + 1, end + 1):
        if arr[j] < pivot_value:
            swap(arr, j, divider_index)
            divider_index += 1

    swap(arr, start, divider_index - 1)
    return divider_index - 1


def swap(arr, ind1, ind2):
    arr[ind1], arr[ind2] = arr[ind2], arr[ind1]


def create_best_pivot(arr, start, end):
    mid = (start + end) // 2

    if arr[start] < arr[mid]:
        if arr[mid] < arr[start]:
            swap(arr, start, mid)
    elif arr[end] < arr[start]:
        swap(arr, start, end)


quicksort_interface(all_totals)
print(all_totals)
print(sum(all_totals[-3:]))
