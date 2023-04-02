# Proszę utworzyć
#     Klasę implementującą stos, który można zainicjalizować przekazując zmienną liczbę parametrów, listę lub inny stos. Sprawdzenie typu i odpowiednią inicjalizację proszę wykonać 
#     korzystając z konstrukcji match-case. W klasie proszę zdefiniować metodę pozwalającą na dodanie elementu do stosu oraz metodę pozwalającą na jego wypisanie. Proszę przetestować działanie klasy (2p).

#     Klasę implementującą stos posortowany, dziedziczącą po wcześniej zdefiniowanej klasie. Inicjalizacja jak wcześniej oraz posortowanym stosem, przy 
#     czym przed sortowaniem proszę zachować elementy typu najliczniej reprezentowanego.
#     W klasie proszę zdefiniować metodę pozwalającą na dodanie elementu pod warunkiem, że zachowa to porządek sortowania.
#     Proszę sprawdzić jaki jest średni rozmiar posortowanego stosu, który wypełniamy całkowitymi liczbami losowymi z przedziału [0,100] losując 100 wartości (średnia po 100 powtórzeniach) (2p).

import random

class Stack:
    def __init__(self, *p):
        match str(type(p[0])):
            case "<class 'list'>":
                # print('list init')
                self.data = list(p[0])
            case "<class '__main__.Stack'>":
                # print('stack init')
                self.data = p[0].data
            case _:
                # print('all')
                self.data = [i for i in p]

    def add(self, to_add):
        self.data.append(to_add)

    def delete(self):
        self.data = self.data[:-1]



class Stack_Sort(Stack):
    def __init__(self, *p):
        self.data = sorted(Stack(*p).data)

    def add_sort(self, to_add):
        if to_add >= self.data[-1]:
            self.data.append(to_add)

            


st1 = Stack([1, 2, 3])
st2 = Stack(st1)
st3 = Stack(1, 2, 3)

st3.add(4)
print(st3.data)
st3.delete()
print(st3.data)

st4 = Stack_Sort(5, 2, 8, 0)
print(st4.data)
st4.add_sort(9)
print(st4.data)

