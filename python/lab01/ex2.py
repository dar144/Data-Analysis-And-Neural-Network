#!/usr/bin/env python3

# a=w1 if warunek else w2

# ************** VERSION 1 ****************

# from math import sqrt, pow
# from cmath import sqrt as csqrt

# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))

# d = pow(b, 2) - 4 * a * c
# if d > 1e-6:
#     x1 = (-b + sqrt(d)) / (2 * a)
#     x2 = (-b - sqrt(d)) / (2 * a)
#     print(f'x1 = {x1:.1f}, x2 = {x2:.1f}')
# elif abs(d) <= 1e-6:
#     x = -b / (2 * a)
#     print(f'x1 = x2 = {x}')
# else:
#     x1 = (-b + csqrt(d)) / (2 * a)
#     x2 = (-b - csqrt(d)) / (2 * a)
#     print(f'x1 = {x1:.1f}, x2 = {x2:.1f}')

# ************** VERSION 2 ****************

import sys
import math
import cmath

if len(sys.argv)!=5:
    sys.exit()

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
eps = float(sys.argv[4])

if (d := pow(b, 2) - 4 * a * c) > eps:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f'{x1=:.1f}, {x2=:.1f}')
elif math.fabs(d) <= eps:
    print(f'x1 = x2 = {-b / (2 * a):.1f}')
else:
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)
    print(f'{x1=:.1f}, {x2=:.1f}')

print(d)