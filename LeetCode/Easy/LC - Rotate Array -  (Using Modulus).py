d = [1, 2, 3, 4, 5, 6, 7]
a = 3


def solution_needs_update(num, k):
    for i in range(0, k):  # run through each index
        num.insert(0, num[-1])  # insert the last value in the list to the front of the same list
        num.pop()  # after the value has been inserted, pop that same value from the end so the length doesnt grow
    return num


def modulus_solution(num, k):
    dog = num[:]  # make a copy of the list that i will basically use to grab my values from
    for i in range(0, len(num)):  # i == each index in the list starting at 0, loop through the this
        num[(i + k) % len(num)] = dog[i]  # take the i index and add it to the amount of spaces you want to move to the right
        # divide that by the length of nums so that the number wont go out of index range
        # set index that you just found to the first index in the other list we created
    return num


print(modulus_solution([1, 2, 3, 4, 5, 6, 7], 3))
print(solution_needs_update([1, 2, 3, 4, 5, 6, 7], 3))
