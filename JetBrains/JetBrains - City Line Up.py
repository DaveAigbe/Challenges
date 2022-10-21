citys = []
check = True

while check:
    enter = str(input('Please enter city: '))
    if enter == 'quit':
        print(citys)
        check = False
    else:
        citys.append(enter)