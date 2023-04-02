def real_number():
    i = 1
    while True:
        yield i
        i += 1


def ideal_num(seq):
    for el in seq:
        suma = sum(list(filter(lambda i : el % i == 0, range(1, el // 2 + 1))))
        if el == suma:
            yield el


def stop(seq, val):
    for i in seq:
        if i <= val:
            yield i
        else:
            return


list_real = list(stop(real_number(), 10000))

for i in ideal_num(list_real):
    print(i, end=' ')

print()