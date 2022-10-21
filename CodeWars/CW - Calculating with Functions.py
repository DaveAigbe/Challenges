def zero(*info):  # your code here
    if info:
        full_info = [n for n in info]
        operation = full_info[0][0]
        number = full_info[0][1]
        if operation == '+':
            return 0 + number
        elif operation == '-':
            return 0 - number
        elif operation == '*':
            return 0 * number
        elif operation == '/':
            return int(0 / number)
    else:
        return 0


def one(*info):  # your code here
    if info:
        full_info = [n for n in info]
        operation = full_info[0][0]
        number = full_info[0][1]
        if operation == '+':
            return 1 + number
        elif operation == '-':
            return 1 - number
        elif operation == '*':
            return 1 * number
        elif operation == '/':
            return int(1 / number)
    else:
        return 1


def two(*info):  # your code here
    if info:
        full_info = [n for n in info]
        operation = full_info[0][0]
        number = full_info[0][1]
        if operation == '+':
            return 2 + number
        elif operation == '-':
            return 2 - number
        elif operation == '*':
            return 2 * number
        elif operation == '/':
            return int(2 / number)
    else:
        return 2


def three(*info):  # your code here
    if info:
        full_info = [n for n in info]
        operation = full_info[0][0]
        number = full_info[0][1]
        if operation == '+':
            return 3 + number
        elif operation == '-':
            return 3 - number
        elif operation == '*':
            return 3 * number
        elif operation == '/':
            return int(3 / number)
    else:
        return 3


def four(*info):  # your code here
    if info:
        full_info = [n for n in info]
        operation = full_info[0][0]
        number = full_info[0][1]
        if operation == '+':
            return 4 + number
        elif operation == '-':
            return 4 - number
        elif operation == '*':
            return 4 * number
        elif operation == '/':
            return int(4 / number)
    else:
        return 4


def five(*info):  # your code here
    if info:
        full_info = [n for n in info]
        operation = full_info[0][0]
        number = full_info[0][1]
        if operation == '+':
            return 5 + number
        elif operation == '-':
            return 5 - number
        elif operation == '*':
            return 5 * number
        elif operation == '/':
            return int(5 / number)
    else:
        return 5


def six(*info):  # your code here
    if info:
        full_info = [n for n in info]
        operation = full_info[0][0]
        number = full_info[0][1]
        if operation == '+':
            return 6 + number
        elif operation == '-':
            return 6 - number
        elif operation == '*':
            return 6 * number
        elif operation == '/':
            return int(6 / number)
    else:
        return 6


def seven(*info):  # your code here
    if info:
        full_info = [n for n in info]
        operation = full_info[0][0]
        number = full_info[0][1]
        if operation == '+':
            return 7 + number
        elif operation == '-':
            return 7 - number
        elif operation == '*':
            return 7 * number
        elif operation == '/':
            return int(7 / number)
    else:
        return 7


def eight(*info):  # your code here
    if info:
        full_info = [n for n in info]
        operation = full_info[0][0]
        number = full_info[0][1]
        if operation == '+':
            return 8 + number
        elif operation == '-':
            return 8 - number
        elif operation == '*':
            return 8 * number
        elif operation == '/':
            return int(8 / number)
    else:
        return 8


def nine(*info):  # your code here
    if info:
        full_info = [n for n in info]
        operation = full_info[0][0]
        number = full_info[0][1]
        if operation == '+':
            return 9 + number
        elif operation == '-':
            return 9 - number
        elif operation == '*':
            return 9 * number
        elif operation == '/':
            return int(9 / number)
    else:
        return 9


def plus(num):  # your code here
    return ['+', int(num)]


def minus(num):  # your code here
    return ['-', int(num)]


def times(num):  # your code here
    return ['*', int(num)]


def divided_by(num):  # your code here
    return ['/', int(num)]


print(seven(times(five())))  # 35
print(four(plus(nine())))  # 13
print(eight(minus(three())))  # 5
print(six(divided_by(two())))  # 3
