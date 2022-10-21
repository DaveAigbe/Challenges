def rot13(message):
    alpha_upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    alpha_lower = list('abcdefghijklmnopqrstuvwxyz')
    decipher = []
    for letter in message:
        if letter.isalpha() and letter.isupper():
            decipher.append(alpha_upper[((alpha_upper.index(letter)) + 13) % (len(alpha_upper))])
        elif letter.isalpha() and letter.islower():
            decipher.append(alpha_lower[((alpha_lower.index(letter)) + 13) % (len(alpha_lower))])
        else:
            decipher.append(letter)

    return ''.join(decipher)


print(rot13('EBG13 rknzcyr.'))
