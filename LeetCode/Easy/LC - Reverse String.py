string_list = ['h', 'e', 'l', 'l', 'o']


def complicated_form(s: list[str]):
    em = []
    current_index = len(s) - 1
    for i in s:
        em.append(s[current_index])
        current_index -= 1

    s = em[:]
    return s

def simple(s: list[str]):
    s = s[::-1]
    return s


print(complicated_form(string_list))
print(simple(string_list))
