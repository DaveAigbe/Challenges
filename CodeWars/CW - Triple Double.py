def triple_double(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    triple = []
    double = []
    for index in range(0, len(num1) - 2):
        if num1[index] == num1[index + 1]:
            if num1[index] == num1[index + 2]:
                triple.append(num1[index])

    if not triple:
        return 0

    for index in range(0, len(num2) - 1):
        if num2[index] == num2[index + 1] and num2[index] in triple:
            double.append(num2[index])

    if triple == double:
        return 1
    else:
        return 0


print(triple_double(12345, 12345))