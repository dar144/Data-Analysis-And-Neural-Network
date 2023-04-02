#!/usr/bin/env python3


# ************************* LISTA SKLADANA ************************

k = [8, 0, 17, 1, 10, 13, 19, 13, 10, 3,]
# np=[i for i in k if i%2]
# np=[1 for i>0 else -1 for i in k]

k=[(k[i], k[-i-1]) for i in range(len(k)//2)]  # // -> liczba calkowita


N=3
k=[]
for i in range(N):
    tmp=[]
    for j in range(N):
        tmp.append((i,j))
    k.append(tmp)
print(k)

#nie mozna
k, tmp=[], []
for i in range(N):
    for j in range(N):
        tmp.append((i,j))
    k.append(tmp)
    tmp.clear()
print(k)
print(tmp)




k =[(89, 34), (92, 31), (96, 0), (48, 30), (38, 10), ]

c=k[:]
c.sort()
print(c)

c=k[:]
c.sort(key=lambda x: x[1])
print(c)

c=k[:]
c.sort(reverse=True)
print(c)
c.reverse()
print(c)

c=k[:]
for i,j in sorted(c):
    print(i, j)
print(c)