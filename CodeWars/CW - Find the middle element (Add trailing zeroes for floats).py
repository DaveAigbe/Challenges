def middle(input_array):
    add = sum(input_array)
    largest = max(input_array)
    smallest = min(input_array)
    finding = add - (largest + smallest)
    if type(finding) == float:
        finding = format(finding, '.3f')  # format 3 decimal places, but it returns a string
        finding = float(finding)  # turn it back into a float variable type

    return input_array.index(finding)


print(middle( [-0.410, -23, 4]))