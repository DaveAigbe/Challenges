def camelCase(s: str) -> str:
    destructured = s.split(';')
    if destructured[0] == 'S':
        pass
    elif destructured[0] == 'C':
        text = destructured[2].split(' ')
        text = map(lambda val: val[0].upper() + val[1:], map(lambda x: x.lower(), text))
        text = text[0].lower() + text[1:]
        return ''.join(text)


print(camelCase('C;V;mobile phone'))
