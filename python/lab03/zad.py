#!/usr/bin/env python3
def fun1(a, *b):
    print(a, b)

fun1(1, 2, 3, 4)

def fun2(**d):
    print(d)


fun2()
fun2(a=1, b=2, c=3)


def fun3(a, b, c=4):
    print(a, b, c)

fun3(1, 2)
fun3(1, 2, 3)


def fun4(a, /, b, *, c=4):
    print(a, b, c)

fun4(1, 2)
fun4(1, 2, c=3)
fun4(1, b=2, c=3)
# fun4(a=1, b=2, c=3))

def fun5(a, /, *b, c=4, **d):
    print(a, b, c, d)

fun5(1, 2)
fun5(1, 2, c=3)
fun5(1, b=2, c=3)
fun5(1, c=2, b=2)

def fun6(a=1, b=2):
    print(a, b)

fun6()
fun6(1)
fun6(b=1)
fun6(a=3, b=4)

fun6(*(4,))
fun6(*(4, 5))

fun6(**{'a':3})

def fun7(el, p=[]):
    p.append(el)
    print(p)

fun7(1)
fun7(2)

def fun8(n, li, s, sl):
    n=3
    li[1]=3
    s='3'
    sl[1]=3

zn=1
zli=[1, 2, 3, 4]
zs='1'
zsl={1:1, 2:2, 3:3, 4:4}

fun8(zn, zli, zs, zsl)

print(zn)
print(zli)
print(zs)
print(zsl)


print(eval('2+7'))

