def timeConversion(s: str) -> str:
    sectioned_time = s.split(':')
    hour, minute, second = sectioned_time
    second = second[:2]

    post_meridian = sectioned_time[2][2:]
    military_time = []

    if post_meridian == 'PM' and hour == '12':
        return ':'.join([hour, minute, second])

    if post_meridian == 'AM':
        if hour == '12':
            military_time.append('00')
            military_time.append(minute)
            military_time.append(second)
        else:
            military_time.append(hour)
            military_time.append(minute)
            military_time.append(second)
    else:
        military_time.append(str(int(hour) + 12))
        military_time.append(minute)
        military_time.append(second)

    return ':'.join(military_time)


print(timeConversion('07:05:45PM'))
