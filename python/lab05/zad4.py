# print("************* zad4 *************")

import random

def myreduce(fun, seq):
    result = seq[0]

    for i in range(1, len(seq)):
        result = fun(result, seq[i])

    return result



seq = [random.randrange(1, 10) for i in range(5)]
print(seq)

add = lambda x, y: x + y
multiply = lambda x, y: x * y


print(myreduce(add, seq))
print(myreduce(multiply, seq))

