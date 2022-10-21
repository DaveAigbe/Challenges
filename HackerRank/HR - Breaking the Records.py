def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]
    count_min = 0
    count_max = 0

    for score in scores:
        if score < minimum:
            minimum = score
            count_min += 1
        elif score > maximum:
            maximum = score
            count_max += 1
    records = [count_max, count_min]
    return records


print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))
