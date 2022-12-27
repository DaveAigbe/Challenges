def hammingWeight(n: int) -> int:
    count = 0
    string_bits = str(n)
    for i in string_bits:
        if i == 1:
            count += 1

    return count


print(hammingWeight(0o0000000000000000000000000001011))
