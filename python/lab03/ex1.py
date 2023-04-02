#!/usr/bin/env python3



print("*************zad1*************")
# Proszę utworzyć string składający się z elementów listy argv z wyłączeniem nazwy
#  programu. Jeżeli program został uruchomiony bez podania parametrów proszę 
#  wypisać na ekran komunikat informujący o właściwym sposobie uruchomienia programu (1p)

import sys
import string
import copy


s = []

if len(sys.argv) != 1:
    s=' '.join(sys.argv[1:])
    print(s)
else:
    print("Nie ma elementow listy argv")



print("\n*************zad2*************")
# Na podstawie wcześniej utworzonego stringa proszę utworzyć cztery listy:
#  zawierającą małe litery, zawierającą duże litery, 
# zawierającą cyfry oraz zawierającą wszystko co nie jest literą (2p)

small_l = [i for i in s if i in string.ascii_lowercase]
print(small_l)
big_l = [i for i in s if i in string.ascii_uppercase]
print(big_l)
num = [i for i in s if i in string.digits]
print(num)
other = [i for i in s if i not in string.ascii_letters]
print(other)



print("\n*************zad3*************")
# Na podstawie utworzonej listy zawierającej małe litery proszę utworzyć 
# listę małych liter bez powtórzeń (bez użycia typu set). Następnie proszę utworzyć 
# nową listę, w której każdy element jest dwuelementową krotką (litera, krotność jej
#  wystąpienia w liście oryginalnej), proszę wykorzystać konstrukcję listy składanej (2p)
small_no_dupl = []

for i in small_l:
    if small_l.count(i) == 1:
        small_no_dupl.append(i)
    elif i not in small_no_dupl:
        small_no_dupl.append(i)

print(small_no_dupl)

small_tuple = [(small_l[i], small_l.count(small_l[i])) for i in range(len(small_l)) if small_l.index(small_l[i]) == i]
print(small_tuple)



print("\n*************zad4*************")
# Otrzymaną w powyższym punkcie listę proszę wyświetlić w kolejności
# od najwyższej krotności (bez sortowania listy oryginalnej) (1p)
print(sorted(small_tuple, key = lambda x : x[1], reverse = True))



print("\n*************zad5*************")
# Proszę utworzyć listę dwuelementowych krotek, w których pierwszy element 
# jest liczbą pobraną z listy cyfr, drugi natomiast wartością funkcji liniowej
#  ax+b dla danej liczby; wartości współczynników proszę ustalić w następujący
#   sposób: a równa się liczbie samogłosek w stringu z punktu pierwszego, 
#   a b - liczbie spółgłosek tamże (2p)

samogloski = 'aeiouyAEIOUY'
a, b = 0, 0

for i in s:
    if i in samogloski:
        a+=1
    elif i in string.ascii_letters and i not in samogloski:
        b+=1

lista = [(int(num[i]), a*int(num[i])+b) for i in range(len(num))]
print(lista)