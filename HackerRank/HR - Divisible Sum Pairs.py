def divisible_sum_paris(n: int, k: int, ar: [int]) -> int:
    pairs = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                total = ar[i] + ar[j]
                if (total % k) == 0:
                    pairs += 1

    return pairs // 2


# print(divisible_sum_paris(6, 3, [1, 3, 2, 6, 1, 2]))


def divisible_sum_paris_stdin():
    size_and_divisor = input().split(' ')
    n, k = size_and_divisor

    ar = input().split(' ')

    pairs = 0
    for i in range(int(n)):
        for j in range(int(n)):
            if i != j:
                total = int(ar[i]) + int(ar[j])
                if (total % int(k)) == 0:
                    pairs += 1

    return pairs // 2


print(divisible_sum_paris_stdin())
