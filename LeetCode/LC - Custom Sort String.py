def customSortString(order, s):
    new = ''

    for char in order:
        if char in s:
            character_count = s.count(char)
            if character_count > 1:
                new += (s.count(char) * char)
                s = s.replace(char, '')
            else:
                new += char
                s = s.replace(char, '')

    return new + s


print(customSortString('kqep', 'pekeq'))
