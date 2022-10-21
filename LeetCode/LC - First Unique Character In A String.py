def firstUniqChar(s):
    for char in range(len(s)):
        if char == 0:
            if s[char] not in s[char + 1:]:
                return char
        elif char == len(s) - 1:
            if s[char] not in s[:char]:
                return char
        elif (s[char] not in s[char + 1:]) and (s[char] not in s[:char]):
            return char
    return -1


s = "a"

print(firstUniqChar(s))
