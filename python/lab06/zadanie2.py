def my_range(*arguments):
    start = 0
    end = 0
    step = 1

    if len(arguments) == 1:
        end = arguments[0]
    elif len(arguments) == 2:
        start = arguments[0]
        end = arguments[1]
    elif len(arguments) == 3 and (arguments[0] - arguments[1]) * arguments[2] < 0:
        start = arguments[0]
        end = arguments[1] 
        step = arguments[2]  
        if start > end:
            while start > end:
                yield start
                start += step
            return

    while start < end:
        yield start
        start += step


print([i for i in range(10, 1, -2)])
print([i for i in my_range(10, 1, -2)])