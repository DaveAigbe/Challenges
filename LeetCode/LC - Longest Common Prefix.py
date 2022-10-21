def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]

    longest_word = max(strs, key=len)
    prefixes = []
    first_letter = 0

    for letter in range(len(longest_word)):
        if longest_word[first_letter:letter + 1] == '':
            continue
        else:
            prefixes.append(longest_word[first_letter:letter + 1])

    commons = []
    commons[:] = prefixes
    for prefix in prefixes:
        for string in strs:
            if string[:len(prefix)] != prefix:
                if prefix in commons:
                    commons.remove(prefix)
                else:
                    continue

    if commons:
        longest_prefix = max(commons, key=len)
        return longest_prefix
    else:
        return ""


print(longestCommonPrefix(["flower", "flow", "flight"]))
