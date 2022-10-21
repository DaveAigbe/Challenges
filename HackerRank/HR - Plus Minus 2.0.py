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

    pos_calc = format(float(pos / total), '.6f')
    neg_calc = format(float(neg / total), '.6f')
    zero_calc = format(float(zero / total), '.6f')

    print(pos_calc)
    print(neg_calc)
    print(zero_calc)


plusMinus([-4, 3, -9, 0, 4, 1])