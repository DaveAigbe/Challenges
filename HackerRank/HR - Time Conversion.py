def timeConversion(s):
    if 'PM' in s:
        s = s.split(':')
        if s[0] != '12':
            s[0] = str(int(s[0]) + 12)
        s = ':'.join(s)
        s = s.replace('PM', '')
    else:
        s = s.split(':')
        if s[0] == '12':
            s[0] = '00'
        s = ':'.join(s)
        s = s.replace('AM', '')

    return s


print(timeConversion('7:05:45PM'))
