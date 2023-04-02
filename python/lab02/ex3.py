#!/usr/bin/env python3


print("****** zad1 ******")
# Korzystając z pętli for proszę usunąć wszystkie 
# wystąpienia określonej wartości z listy

k = [8, 0, 17, 17, 1, 10, 13, 19, 13, 10, 3, 17,]
print(k)
num=17

for i in range(len(k)):
    if num in k:
        k.remove(num)

print(k)
print("\n")





print("****** zad2 ******")
# j.w. ale korzystając z pętli while

k = [8, 0, 17, 17, 1, 10, 13, 19, 13, 10, 3, 17,]
print(k)
num=17
i=0

while i < len(k):
    if num in k:
        k.remove(num)
    i+=1

print(k)
print("\n")





print("****** zad3 ******")
# Korzystając z pętli for oraz funkcji range proszę wypisać 
# co drugi element listy począwszy od elementu o indeksie 1 (bez instrukcji warunkowej)

k = [8, 0, 17, 17, 1, 10, 13, 19, 13, 10, 3, 17,]
print(k)

for i in range(1, len(k), 2):
    print(k[i])
print("\n")




print("****** zad4 ******")
# j.w. ale bez range

k = [8, 0, 17, 17, 1, 10, 13, 19, 13, 10, 3, 17,]
print(k)

for i in k[1::2]:
    print(i)

print("\n")




print("****** zad5 ******")
# Korzystając z pętli for oraz funkcji range 
# proszę wypisać co drugi element listy od końca (bez instrukcji warunkowej)
k = [8, 0, 17, 17, 1, 10, 13, 19, 13, 10, 3, 17,]
print(k)

for i in range(len(k) - 1, -1, -2):
    print(k[i])
print("\n")




print("****** zad6 ******")
# j.w. ale bez range
k = [8, 0, 17, 17, 1, 10, 13, 19, 13, 10, 3, 17,]
print(k)

for i in k[len(k) - 1::-2]:
    print(i)
print("\n")




print("****** zad7 ******")
# Proszę utworzyć nową listę, której elementami 
# są krotki (indeks, element) na podstawie istniejącej listy <- lista składana
k = [8, 0, 17, 17, 1, ]
k=[(i, k[i]) for i in range(len(k))]  
print(k)
print("\n")



print("****** zad8 ******")
# Proszę posortować listę z poprzedniego punktu wg drugiego elementu krotek
c=k[:]
c.sort(key=lambda x: x[1])
print(k)
print(c)
print("\n")




print("****** zad9 ******")
# Proszę utworzyć nową listę, której elementami są krotki (indeks, element) 
# na podstawie istniejącej listy, przy czym dodajemy krotkę tylko,
#  jeśli wartość pobrana z listy jest wartością parzystą <- lista składana
k = [8, 0, 17, 17, 1, 2, ]
print(k)

c = [(i, k[i]) for i in range(len(k)) if k[i]%2 == 0]
print(c)
print("\n")




print("****** zad10 ******")
# Proszę utworzyć nową listę, której elementami są krotki (indeks, element) 
# lub (element, indeks) na podstawie istniejącej listy,
#  tak, aby pierwszy element krotki był mniejszy od drugiego <- lista składana
print(k)

c = [(i, k[i]) if i <= k[i] else (k[i], i) for i in range(len(k))]
print(c)
print("\n")




print("****** zad10 ******")
# Proszę utworzyć listę 2D (lista składana) wypełnioną zerami oraz jedynkami, przy czym jedynki występują:
# w kwadracie o boku mniejszym od rozmiaru listy na jej "środku"
# na przekątnej od lewego górnego rogu do prawego dolnego
# na przekątnej od prawego górnego rogu do lewego dolnego
# na obu przekątnych
# w szachownicę

n = 5

print("a)")
k = [[1 if i > 0 and i < n - 1 and j > 0 and j < n - 1 else 0 for j in range(n)] for i in range(n)]
print(k)
print("\n")

print("b)")
k = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print(k)
print("\n")

print("c)")
k = [[1 if i + j == n - 1 else 0 for j in range(n)] for i in range(n)]
print(k)
print("\n")

print("d)")
k = [[1 if i + j == n - 1 or i == j else 0 for j in range(n)] for i in range(n)]
print(k)
print("\n")

print("e)")
k = [[1 if (i + j) % 2 == 0 else 0 for j in range(n)] for i in range(n)]
print(k)
print("\n")



