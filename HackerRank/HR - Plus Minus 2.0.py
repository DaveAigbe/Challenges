def plusMinus(arr):
    # Write your code here
    total = len(arr)
    neg = 0
    pos = 0
    zero = 0

    for n in arr:
        if n == 0:
            zero += 1
        elif n > 0:
            pos += 1
        else:
            neg += 1

    print(pos / total)
    print(neg / total)
    print(zero / total)


plusMinus([-4, 3, -9, 0, 4, 1])