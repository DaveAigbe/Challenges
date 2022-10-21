def title_case(title, minor_words=''):
    if title == '':
        return title
    else:
        title = title.lower().split(' ')
        minor_words = minor_words.lower().split(' ')
        for word in range(len(title)):
            if title[word] not in minor_words or word == 0:
                title[word] = title[word][0].upper() + title[word][1:]

        return ' '.join(title)


print(title_case('', ''))
