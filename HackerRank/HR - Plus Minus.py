def plusMinus(arr):
    positive = 0
    negative = 0
    zeroes = 0
    for number in arr:
        if number == 0:
            zeroes += 1
        elif number > 0:
            positive += 1
        else:
            negative += 1
    length = len(arr)
    print(float(positive / length))
    print(float(negative / length))
    print(float(zeroes / length))


print(plusMinus([1, 1, 0, -1, -1]))
