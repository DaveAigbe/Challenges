x = int(input())

if 1 < x:
    if x % 2 == 0 or x % 3 == 0:
        print('This number is not prime')
    else:
        print('This number is prime')
else:
    print('This number is not prime')