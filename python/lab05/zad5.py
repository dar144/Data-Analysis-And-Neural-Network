# print("************* zad5 *************")

import functools
import math
import random

def fun(x_array, y_array):
    x_avg = functools.reduce(lambda x, y: x + y, x_array) / len(x)
    y_avg = functools.reduce(lambda x, y: x + y, y_array) / len(y)

    D = sum(list(map(lambda x: (x - x_avg)**2, x_array)))
    a = sum(list(map(lambda x, y: y*(x - x_avg), x_array, y_array))) / D
    b = y_avg - a* x_avg;

    delta_y = math.sqrt((sum(list(map(lambda x, y: (y - a*x - b)**2, x_array, y_array)))) / (len(x_array) - 2) )
    delta_a = delta_y / math.sqrt(D)
    delta_b = delta_y * math.sqrt(1 / len(x_array) + x_avg**2 / D)

    return a, b, delta_a, delta_b



x = [i for i in range(10)]
y = [2*i+2 for i in range(10)]
print(fun(x, y))

x = [random.uniform(1, 10) for i in range(10)]
y = [random.uniform(1, 10) for i in range(10)]
print(fun(x, y))

