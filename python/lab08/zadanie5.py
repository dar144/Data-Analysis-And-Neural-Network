# Proszę sporządzić histogram słów rozpoczynających się na daną literę alfabetu ze wszystkich plików ,
# których nazwy pasują do określonego wzorca w katalogu bieżącym, opcje wyświetlenia: sortowanie alfabetyczne bądź po liczbie słów (2.5p)

import matplotlib.pyplot as plt
import glob
import string


f = []
t = {}

x = []
y = []


for file_name in glob.glob('zad5*.in'):
    with open(file_name) as file_object:
        for line in file_object:
            f.extend([el for el in line.title() if el in string.ascii_uppercase])


for el in f:
    if el not in t:
        t[el] = 1
    else:
        t[el] += 1


l = [(i, j) for i, j in t.items()]
l = sorted(l)


for el in l:
    x.append(el[0])
    y.append(el[1])

plt.plot(x,y)
plt.savefig('histogram.pdf')