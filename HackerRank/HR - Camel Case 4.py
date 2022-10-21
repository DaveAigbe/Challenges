user_choice = 'S;C;OrangeHighlighter'.split(';')
original_phrase = list(user_choice[2])  # create a list from the actual phrase
camel_cased = []  # Finished product will be stored here
for index in range(len(original_phrase)):
    if user_choice[0] == 'S':  # Split
        if user_choice[1] == 'M':  # Method ex. plasticCup() -> plastic cup
            if original_phrase[index] == '(' or original_phrase[index] == ')':  # ignore parentheses
                continue
            else:
                if original_phrase[index].isupper():  # if its uppercase
                    if ' ' in camel_cased:  # if there is already a space ignore
                        continue
                    else:
                        camel_cased.append(' ')  # add a space first
                        camel_cased.append(original_phrase[index].lower())  # then add the letter in lowercase format
                else:
                    camel_cased.append(original_phrase[index])  # if it's not a parentheses or uppercase just add it to the new list
        elif user_choice[1] == 'C':  # Class ex. LargeSoftwareBook -> large software book
            if original_phrase[index].isupper():  # if its uppercase
                if index == 0:  # The first letter will be uppercase, do not add a space in front of it like the rest, just add it as lowercase
                    camel_cased.append(original_phrase[index].lower())
                else:
                    camel_cased.append(' ')  # add a space first
                    camel_cased.append(original_phrase[index].lower())  # then add the letter in lowercase format
            else:
                camel_cased.append(original_phrase[index])  # if it's not a parentheses or upp
        elif user_choice[1] == 'V':  # Variable ex. pictureFrame-> picture frame
            if original_phrase[index].isupper():  # if its uppercase
                camel_cased.append(' ')  # add a space first
                camel_cased.append(original_phrase[index].lower())  # then add the letter in lowercase format
            else:
                camel_cased.append(original_phrase[index])  # if it's not a parentheses or upp
    elif user_choice[0] == 'C':  # Combine
        if user_choice[1] == 'M':  # Method ex. white sheet of paper -> whiteSheetOfPaper()
            if original_phrase[index] == ' ':  # If the index is a whitespace
                original_phrase[index + 1] = original_phrase[index + 1].upper()  # The index to the right of it becomes uppercase, do not add the whitespace to the new list
            else:
                if index == len(original_phrase) - 1:  # If loop is at last index
                    camel_cased.append(original_phrase[index])  # Add the letter to the list
                    camel_cased.append('()')  # Then add the parentheses that makes it a method
                else:
                    camel_cased.append(original_phrase[index])
        elif user_choice[1] == 'C':  # Method ex. coffee machine -> CoffeeMachine
            if original_phrase[index] == ' ':  # If the index is a whitespace
                original_phrase[index + 1] = original_phrase[index + 1].upper()  # The index to the right of it becomes uppercase, do not add the whitespace to the new list
            else:
                if index == 0:  # If loop is at last index
                    camel_cased.append(original_phrase[index].upper())  # First index does not have a space, so the condition above will ignore it. Manually make it uppercase.
                else:
                    camel_cased.append(original_phrase[index])
        elif user_choice[1] == 'V':  # Method ex. mobile phone -> mobilePhone
            if original_phrase[index] == ' ':  # If the index is a whitespace
                original_phrase[index + 1] = original_phrase[index + 1].upper()  # The index to the right of it becomes uppercase, do not add the whitespace to the new list
            else:
                camel_cased.append(original_phrase[index])


print(''.join(camel_cased))

