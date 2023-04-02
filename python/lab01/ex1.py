#!/usr/bin/env python3
import keyword
import builtins
import math

# print(keyword.kwlist)
# print(dir(builtins))
# print(dir(math))
# help(builtins.complex)

# print(dir(''))
# help(''.strip)
# ''.strip.__doc__

print(type(''))
print(type(""))

a, b = 7, '2'
print(type(a), type(b))

a = 1, 5   #krotka/tuple
print(type(a))

a, *b = 1, '2', 3., 4, 5
print(type(a), type(b))

print(1 / 2, 1 // 2)
print(1. / 2, 1. // 2)

print(2 ** 3, pow(2, 3), math.pow(2, 3))
print(pow(2, 3, 4), pow(2, 3, 5))

print(math.ceil(1/3), math.floor(1/3), round(1/3), round(1/3, 3))
print(math.ceil(2/3), math.floor(2/3), round(2/3), round(2/3, 3))

print(min(2, 11, 3, 4, 2), max(2, 11, 3, 4, 2))

a = -1.7
print(abs(a), math.fabs(a))
a = -1
print(abs(a), math.fabs(a))

