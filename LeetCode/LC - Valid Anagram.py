def isAnagram(s, t):
    if len(s) != len(t):
        return False
    for char in s:
        if char in t:
            t = t.replace(char, "", 1)
            s = s.replace(char, "", 1)
    return t == '' and s == ''


print(isAnagram(s="anagram", t="nagaram"))
