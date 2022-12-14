"""
Original implementation
def two_sum(nums: list[int], target: int) -> list[int]:
   sum_arr = []

   for i, v in enumerate(nums):
       for p, j in enumerate(nums):
           if (v + j) == target and p != i:
               sum_arr.append(i)
               sum_arr.append(p)

               return sum_arr


print(two_sum([-1, -2, -3, -4, -5], -8))
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    hashmap = {}

    for i, v in enumerate(nums):
        only_solution = target - v

        if hashmap.get(only_solution) is not None:
            return [hashmap[only_solution], i]

        hashmap[v] = i



print(two_sum([2,7,11,15], 9))
