def breakingRecords(scores):
    top = scores[0]
    bottom = scores[0]
    broken_records = [0, 0]

    for i in scores:
        if i > top:
            top = i
            broken_records[0] += 1
        elif i < bottom:
            bottom = i
            broken_records[1] += 1

    return broken_records


print(breakingRecords([12, 24, 10, 24]))
