def f1(func):
    def wrapper(*args, **kwargs):  # pass arguments through wrapper
        print('started')
        val = func(*args, **kwargs)  # pass arguments through the func in f1, allowes f() to pass arguments
        # store the value returned by this function inside of a variable so that the program doesent auto-end
        print('ended')
        return val  # return the value to wrapper function

    return wrapper  # return wrapper function to f1()


@f1  # decorator
def f(a, b='succeed'):
    print(a)
    print()
    print(b)


@f1
def add(x, y):
    return x + y


print(add(4, 5))

f('and')
