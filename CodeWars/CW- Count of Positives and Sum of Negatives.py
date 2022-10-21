def count_positives_sum_negatives(arr):
    positives = 0
    negatives = 0
    numbers = []
    if not arr:
        return numbers
    else:
        for value in arr:
            if value > 0:
                positives += 1
            elif value < 0:
                negatives += value

    numbers.append(positives)
    numbers.append(negatives)

    return numbers


print(count_positives_sum_negatives([]))
