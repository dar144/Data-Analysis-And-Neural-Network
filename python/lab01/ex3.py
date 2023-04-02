#!/usr/bin/env python3

import copy

# # ************** KTOTKA / TUPLE ****************

# k=()
# print(type(k))

# k=(2)
# print(type(k))

# k=(2, )
# print(type(k))

# k=(1, 2.3, '3', (4, 7), [2, 3, 4])
# print(len(k))

# print(k[0], k[len(k)-1], k[-1], k[-len(k)])

# # k[-1] = 'a'
# # can't change elements in a tuple

# k[-1][1] = 'a'
# print(k[-1])

# # ************** LISTA /LIST ****************


# k=[]
# print(type(k))

# k=[2]
# print(type(k))

# k=[2, ]
# print(type(k))

# k=[1, 2.3, '3', (4, 7), [2, 3, 4]]
# print(len(k))

# print(k[0], k[len(k)-1], k[-1], k[-len(k)])

# # k[-2][1] = 'a'

# # wycinki list

k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

# print(k[:])
# print(k[2:-3]) # element -3 nie wchodzi do wycinku
# print(k[2:-3:2]) # :2 to krok / w tym przypadku kazdy drugi
# print(k[2:])
# print(k[:-3]) 
# print(k[::-1]) # obrocona lista

# k = [1, 2, [3, 4, 5], 6]
# c = k  #kopiowanie referencji
# c[1] = [7, 8, 9]
# print(k)
# print(c)
# # print(id(c), id(k))

# c = k[:] 
# c[1] = '7, 8, 9'
# print(k)
# print(c)
# # print(id(c), id(k))

# c[-2][1] = '11, 12, 13'
# print(k)
# print(c)

# c = copy.copy(k)
# c[1] = '7, 8, 9'
# print(k)
# print(c)
# print(id(c), id(k))

# c = copy.deepcopy(k)
# c[1] = '7, 8, 9'
# print(k)
# print(c)
# print(id(c), id(k))

print(k.count(13))
print(k.count(1))

# print(k.index(13))  BLAD
print(k.index(1))

print(13 in k)
print(13 not in k)

if 13 in k:
    print('ala')

if 13 not in k:
    pass

k.insert(4, -3) #dzie co
k.insert(34, -5)
print(k)

k[1:4] = [33, 44, 55, 66]
print(k)

k[1:4] = [[33, 44,],]
print(k)


# # ************** BOOL ****************

# print(bool(0), bool(1))
# print(bool([]), bool([1]))
# print(bool(''), bool('a'))


