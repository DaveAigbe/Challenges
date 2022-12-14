nums = [-4, -1, 0, 3, 10]
new = []

for i in nums:
    x = pow(i, 2)
    new.append(x)

print(new)

list_indexes = len(new) - 1


def selection():
    for i in range(0, list_indexes):
        min_value = i

        for j in range(i + 1, len(new)):
            if new[j] < new[min_value]:
                min_value = j
        if min_value != i:
            new[min_value], new[i] = new[i], new[min_value]
    return new


def bubble():
    list_indexes = len(new) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, list_indexes):
            if new[i] > new[i + 1]:
                sorted = False
                new[i], new[i + 1] = new[i + 1], new[i]
    return new


print(new)
