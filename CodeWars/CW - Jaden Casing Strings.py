def to_jaden_case(x):
    x = list(x)
    x[0] = x[0].upper()
    for j in range(1, len(x)):
        x[j] = x[j].lower()

    for i in range(len(x) - 1):
        if x[i] == ' ':
            x[i + 1] = x[i + 1].upper()

    x = ''.join(x)

    return x


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
