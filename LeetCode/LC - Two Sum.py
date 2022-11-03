def two_sum(nums: list[int], target: int) -> list[int]:
    sum_arr = []

    for i, v in enumerate(nums):
        for p, j in enumerate(nums):
            if (v + j) == target and p != i:
                sum_arr.append(i)
                sum_arr.append(p)

                return sum_arr


print(two_sum([-1, -2, -3, -4, -5], -8))
