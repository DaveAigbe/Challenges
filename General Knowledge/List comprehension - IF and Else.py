old_list = [int(num) for num in input().split(" ")]
binary_list = [x * 0 if x <= 0 else int(x / x) for x in old_list]

print(binary_list)