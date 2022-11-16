def remove_duplicates(arr: list[int]) -> int:
    arr = list(set(arr))
    return len(arr)


print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
