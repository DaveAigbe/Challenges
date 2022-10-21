def miniMaxSum(arr):
    minimum = sum(arr) - max(arr)
    maximum = sum(arr) - min(arr)
    print(minimum, maximum)


miniMaxSum([1, 3, 5, 7, 9])