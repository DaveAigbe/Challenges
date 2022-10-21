def reverse_words(text):
    sentence = text.split(' ')

    for word in range(len(sentence)):
        sentence[word] = sentence[word][::-1]

    return ' '.join(sentence)


print(reverse_words('The quick brown fox jumps over the lazy dog.'))
