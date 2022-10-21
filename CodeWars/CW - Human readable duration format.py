def format_duration(seconds):
    if seconds == 0:
        return 'now'
    minutes = int(seconds / 60)

    hours = int(minutes / 60)

    days = int(hours / 24)

    years = int(days / 365)

    seconds_2 = seconds - 60 * minutes
    minutes_2 = minutes - 60 * hours
    hours_2 = hours - 24 * days
    days_2 = days - 365 * years

    statement = []

    if years == 1:
        statement.append(f'{years} year')
    elif years != 0:
        statement.append(f'{years} years')

    if days_2 == 1:
        statement.append(f'{days_2} day')
    elif days_2 != 0:
        statement.append(f'{days_2} days')

    if hours_2 == 1:
        statement.append(f'{hours_2} hour')
    elif hours_2 != 0:
        statement.append(f'{hours_2} hours')

    if minutes_2 == 1:
        statement.append(f'{minutes_2} minute')
    elif minutes_2 != 0:
        statement.append(f'{minutes_2} minutes')

    if seconds_2 == 1:
        statement.append(f'{seconds_2} second')
    elif seconds_2 != 0:
        statement.append(f'{seconds_2} seconds')

    if len(statement) > 1:
        statement.insert(-1, 'and')
        if len(statement) == 3:
            return (' '.join(statement))
        elif len(statement) > 3:
            return (', '.join(statement[:-2]) + ' ' + ' '.join(statement[-2:]))
    else:
        return (statement[0])


print(format_duration(3123123))
