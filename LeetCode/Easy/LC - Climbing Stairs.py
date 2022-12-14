def climbStairs(n):
    first = 0
    second = 1

    for i in range(1, n + 1):
        total = first + second
        if i == n:
            return total
        first = second
        second = total

    # 1 2 3 4 5 6 7 8
    # 1 2 3 5 8 13 21 34


print(climbStairs(3))
