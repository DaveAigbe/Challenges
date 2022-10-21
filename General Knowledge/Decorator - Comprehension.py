def f1(func):  # defined function, i will pass another function through this as a parameter
    def wrapper():  # wrapper function that will be returned to f1()
        print("This is for testing")
        func()  # call the seperate function im using, which will be passed as an argument
        print("understanding")

    return wrapper  # return the strings that were printed to f1()


@f1  # this is the same thing as line 21, this is a DECORATOR
def f2():  # seperate function
    print("my")


f1(f2)()  # The extra () will call the wrapper function, without it, the wrapper function will never be called
# f1(f2) will print nothing because the wrapper function went unused

print(f1(f2))  # returns f1.<locals>.wrapper at 0x0000022E0816C790
# when you call f1, you got back a value which was another function

x = f1(f2)  # this is the same thing as the f1(f2)()  because when you call 'x' you have to use that extra ()
# which calls wrapper
x()  # () calls the wrapper function
f2()  # uses the decorator to have the same use as line 21
