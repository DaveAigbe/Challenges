def miniMaxSum(arr: list) -> None:
    sorted_arr = sorted(arr)
    smallest_sum = sum(sorted_arr[:len(arr) - 1])
    largest_sum = sum(sorted_arr[1:])

    print(smallest_sum, largest_sum)


# def miniMaxSum(arr: list) -> None:
#     smallest = arr[0]
#     largest = arr[0]
#
#     for i in arr:
#         if i < smallest:
#             smallest = i
#         elif i > largest:
#             largest = i
#
#     reduce_smallest = sum(filter(lambda x: x != largest, arr))
#     reduce_largest = sum(filter(lambda x: x != smallest, arr))
#
#     print(reduce_smallest, reduce_largest)


miniMaxSum([5, 5, 5, 5, 5])
