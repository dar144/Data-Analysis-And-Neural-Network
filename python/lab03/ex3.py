#!/usr/bin/env python3
import random
import string

print("*************zad1*************")
# Proszę utworzyć k-elementową listę całkowitych wartości losowych z przedziału [0,5k).
# Proszę sprawdzić ile elementów pozostaje na swoim miejscu po losowym przemieszaniu 
# listy, mieszanie proszę wykonać 100 razy a wyniki zapisywać w słowniku (2p)

k = 5
d = {f: 0 for f in range(k)}
l = [random.randrange(0, 5*k) for i in range(k)]
# print(l)

c = l[:]
for i in range(100):
    random.shuffle(c)
    # print(c)
    for j in range(k):
        if(c[j] == l[j]):
            d[j] += 1
print(d)




print("\n*************zad2*************")
# Proszę utworzyć losowy string o długości k zawierający tylko
#  małe litery, pomiędzy poszczególne litery proszę wstawić kropkę (1p) 

k = 10
s = '.'.join([string.ascii_lowercase[random.randrange(0, len(string.ascii_lowercase))] for i in range(k)])
print(s)




print("\n*************zad3*************")
# Proszę utworzyć listę stu wartości losowych z przedziału [0,20). 
# Następnie na jej podstawie proszę utworzyć słownik, w którym klucze są 
# liczbami z listy, a wartościami lista ich indeksów.
#     w rozwiązaniu proszę wykorzystać metodę setdefault i funkcjię enumerate (1p)
#     w rozwiązaniu proszę wykorzystać metody setdefault i index (1.5p)


l = [random.randrange(0, 20) for i in range(20)]
# print(l)
s = {}

print("-----a------")
for i, j in enumerate(l):
    if l.count(j) > 1:
        s.setdefault(j, []).append(i)
    else:
        s.setdefault(j, i)
print(s)

# s2 = {}

# print("-----b------")
# for i in l:
#     if l.count(i) > 1:
#         s2.setdefault(i, []).append(l.index(i))
#     else:
#         s2.setdefault(i, l.index(i))
# print(s2)




print("\n*************zad4*************")
# Proszę sprawdzić ile spośród 1000 losowych wartości całkowitych 
# składających się z n cyfr, gdzie n jest z przedziału [3,6], jest liczbami 
# palindromowymi. Wynik proszę zapisać w słowniku - jedna linijka (2.5p)

n = random.randint(3, 6)
print(n)

l = [str(random.randrange(10 ** (n - 1), 10 ** n)) for i in range(10)]
print(l)

# for i in range(n // 2):
    # if(l[i] == l[i].reverse):
    # print(l[i], l[i].reverse())




