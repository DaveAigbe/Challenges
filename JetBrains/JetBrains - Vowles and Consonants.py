x = input()

separate_Characters = [i for i in x]

for i in separate_Characters:
    if i in ('a', 'e', 'i', 'o', 'u'):  # Statements with multiple "==" can be done like this if comparing to string
        print('vowel')
    elif i.isalpha() is False:  # Can use is False instead of == False for clarity
        break
    else:
        print('consonant')