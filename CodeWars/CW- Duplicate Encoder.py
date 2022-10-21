def duplicate_encode(word):
    word = word.lower()
    new = ''
    for char in word:
        if word.count(char) > 1:
            new += ')'
        else:
            new += '('

    return new