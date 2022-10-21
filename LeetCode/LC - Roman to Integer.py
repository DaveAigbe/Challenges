def romanToInt(self, s: str) -> int:
    skip = []
    last_index = len(s) - 1
    total = 0
    for numeral in range(len(s)):
        if numeral in skip:
            continue
        else:
            if s[numeral] == 'I':
                if numeral != last_index:
                    if s[numeral + 1] == 'V':
                        total += 4
                        skip.append(numeral + 1)
                    elif s[numeral + 1] == 'X':
                        total += 9
                        skip.append(numeral + 1)
                    else:
                        total += 1
                else:
                    total += 1
            elif s[numeral] == 'V':
                total += 5
            elif s[numeral] == 'X':
                if numeral != last_index:
                    if s[numeral + 1] == 'L':
                        total += 40
                        skip.append(numeral + 1)
                    elif s[numeral + 1] == 'C':
                        total += 90
                        skip.append(numeral + 1)
                    else:
                        total += 10
                else:
                    total += 10
            elif s[numeral] == 'L':
                total += 50
            elif s[numeral] == 'C':
                if numeral != last_index:
                    if s[numeral + 1] == 'D':
                        total += 400
                        skip.append(numeral + 1)
                    elif s[numeral + 1] == 'M':
                        total += 900
                        skip.append(numeral + 1)
                    else:
                        total += 100
                else:
                    total += 100
            elif s[numeral] == 'D':
                total += 500
            elif s[numeral] == 'M':
                total += 1000

    return total


print(romanToInt('MCMXCIV'))
