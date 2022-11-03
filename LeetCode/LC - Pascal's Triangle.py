"""
1. If the row is currently empty, add the peak [1]
2. Create an empty array, with the length of the specified row count + 1 because it will cut off the last number otherwise
3. If the current index - 1 and current index from the previous array exists, both left and right exist
4. Both left and right indices exist from the previous array
5. If only the left index exists
6. If only the right index exists
"""


def pascals_triangle(num_rows):
    rowCount = 0
    triangle = []

    while rowCount < num_rows:
        if not triangle:  # 1
            row = [1]
            triangle.append(row)
            rowCount += 1
        else:
            row = [0 for _ in range(rowCount + 1)]  # 2.
            prev_row = triangle[rowCount - 1]

            for i in range(rowCount + 1):
                prev_left_exists = ((i - 1) >= 0)  # 3.
                prev_right_exists = i <= len(prev_row) - 1

                if prev_left_exists and prev_right_exists:  # 4.
                    left = prev_row[i - 1]
                    right = prev_row[i]
                    new_value = left + right

                    row[i] = new_value
                elif prev_left_exists:  # 5.
                    left = prev_row[i - 1]
                    row[i] = left

                else:  # 6.
                    right = prev_row[i]
                    row[i] = right

            triangle.append(row)
            rowCount += 1

    return triangle


print(pascals_triangle(10))
