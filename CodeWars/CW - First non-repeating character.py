def first_non_repeating_letter(string):
    if string == '':
        return string

    string_copy = list(string)
    string = list(string.lower())
    single_chars = []

    try:
        over_1 = []

        for letter in string:
            if string.count(letter) > 1:
                over_1.append(letter)

        for letter in string:
            if letter not in over_1:
                single_chars.append(letter)

    except IndexError:
        return ''
    else:
        if len(over_1) == len(string):
            return ''
        else:
            try:
                if single_chars[0].upper() == string_copy[string_copy.index(single_chars[0].upper())]:
                    return single_chars[0].upper()
            except ValueError:
                return single_chars[0]
            else:
                return single_chars[0]


print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))