def fibonacci(n):


    x=0
    y=1
    next_sum=0
    print("Initial Numbers:",x,y,end=' ')

    while next_sum in range(n):

        next_sum=x+y
        print(next_sum, end=' ')
        x=y
        y=next_sum


fibonacci(20)

