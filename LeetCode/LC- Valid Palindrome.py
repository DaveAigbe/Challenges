def isPalindrome(s: str) -> bool:
    s = s.lower()
    fixed = []
    for char in s:
        if char.isalpha() or char.isnumeric():
            fixed.append(char)
    return ''.join(fixed) == ''.join(fixed[::-1])


print(isPalindrome("0P"))