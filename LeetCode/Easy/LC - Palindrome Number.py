def isPalindrome(x: int) -> bool:
    x = str(x)

    for i in range(len(x) // 2):
        corresponding = len(x) - (i + 1)
        if x[i] != x[corresponding]:
            return False

    return True


print(isPalindrome(-121))
