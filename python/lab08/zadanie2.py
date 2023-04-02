# Odczytujemy wartości ze wszystkich plików, których nazwy rozpoczynają się od data i kończą na in w katalogu bieżącym. 
# Na wyjściu proszę utworzyć jeden plik z trzema kolumnami:

# -pierwsza kolumna - numer wiersza,
# -druga kolumna - uśredniona wartość z danego wiersza ze wszystkich plików (numpy.average),
# -trzecia kolumna - odchylenie standardowe wartości z danego wiersza ze wszystkich plików (numpy.std)
# (2.5)

import glob
import numpy

data = []

for file_name in glob.glob('data/*'):
    with open(file_name) as file_object:
        tmp = [float(el) for el in file_object.readlines()]
        data.append(tmp)

col1 = list(range(len(data[0])))
col2 = list(map(numpy.average, zip(*data)))
col3 = list(map(numpy.std, zip(*data)))

with open('data.out', 'w') as file_object:
    for i in range(len(col1)):
        file_object.write(f'{col1[i]}\t{col2[i]:>20}\t{col3[i]:>20}\n')
