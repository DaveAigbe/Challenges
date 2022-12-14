def binary(arr, target):
    left = 0
    right = arr.length-1

    while left <= right:
        mid = (left+right)/2
        if arr[mid] == target:
            return mid
        elif target<arr[mid]:
            right = mid-1
        elif arr[mid]<target:
            left = mid+1
    else:
        return(-1)