import math

def approx_sin(x, k):
    while True:
        suma = 0
        for i in range(k):
            suma += ((pow(-1, i) / math.factorial(1+2*i))) * pow(x, 1+2*i)
        yield suma



x = 1.57
k = 0

while abs(next(approx_sin(x, k)) - math.sin(x)) > 10e-8:
    k += 1


print(k)

